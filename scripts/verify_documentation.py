#!/usr/bin/env python3
"""Check site routes, assets, preserved legal text and real example content."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import html, json, re, subprocess

ROOT=Path(__file__).resolve().parent.parent
class Document(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.h1=0;self.stack=[];self.paragraphs=[];self.current=None
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.add(d['id'])
        if tag=='h1':self.h1+=1
        if tag=='a':self.links.append(d.get('href',''))
        if tag in ('img','script','iframe') and d.get('src'):self.links.append(d['src'])
        if tag=='link' and d.get('href'):self.links.append(d['href'])
        if tag=='p':self.current=[]
    def handle_data(self,data):
        if self.current is not None:self.current.append(data)
    def handle_endtag(self,tag):
        if tag=='p' and self.current is not None:
            self.paragraphs.append(' '.join(''.join(self.current).split()));self.current=None

def parse(path):
    p=Document();p.feed(path.read_text());return p

def main():
    pages=[ROOT/'index.html',ROOT/'web-demo/index.html',ROOT/'privacy-policy/index.html',*sorted((ROOT/'guide').rglob('index.html')),ROOT/'design-comparison/index.html']
    for page in pages:
        doc=parse(page)
        assert doc.h1==1,(page,'expected exactly one page heading')
        for link in doc.links:
            parts=urlsplit(link)
            if parts.scheme or not parts.path:continue
            target=(page.parent/unquote(parts.path)).resolve()
            assert target.is_relative_to(ROOT),(page,link,'outside site')
            assert target.exists(),(page,link,'missing target')
            if target.is_dir():target=target/'index.html'
            if parts.fragment and target.suffix=='.html':
                assert unquote(parts.fragment) in parse(target).ids,(page,link,'missing anchor')
    legal=json.loads((ROOT/'content/privacy.json').read_text())
    policy=parse(ROOT/'privacy-policy/index.html')
    for raw in [legal['introduction'],*[s['html'] for s in legal['sections']]]:
        expected=' '.join(html.unescape(re.sub('<[^>]+>','',raw)).split())
        assert expected in policy.paragraphs,('changed privacy text',expected)
    baseline=subprocess.check_output(['git','show','aa766ea:privacy-policy/index.html'],cwd=ROOT,text=True)
    old=Document();old.feed(baseline)
    old_legal=[p for p in old.paragraphs if p not in ('My Lyrics','Open live web demo')]
    for paragraph in old_legal:assert paragraph in policy.paragraphs,('policy baseline changed',paragraph)
    for p in (ROOT/'assets/fonts').glob('*.woff2'):assert p.read_bytes()[:4]==b'wOF2',p
    assert len(list((ROOT/'assets/fonts').glob('LICENSE-*.md')))==2
    example=json.loads((ROOT/'downloads/my-lyrics-example.json').read_text())
    original=json.loads((ROOT/'web-demo/app/assets/assets/static_book.json').read_text())
    assert example['songs']==original['songs'] and example['title']==original['title']
    for p in ('web-demo/app/main.dart.js','web-demo/app/index.html','web-demo/app/assets/AssetManifest.bin'):
        assert (ROOT/p).read_bytes()==subprocess.check_output(['git','show','aa766ea:'+p],cwd=ROOT),('compiled app changed',p)
    for css in (ROOT/'assets').glob('*.css'):
        for url in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css.read_text()):
            assert (css.parent/url).exists(),(css,url)
    print(f'PASS: {len(pages)} static pages; all local links/assets/anchors; unchanged legal paragraphs and app bundle; fonts/licenses; authentic guidebook download.')
if __name__=='__main__':main()

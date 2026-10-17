#!/usr/bin/env python3
"""Build the visual comparison using unedited browser captures and the approved board."""
from pathlib import Path
import json
from build_documentation import page

ROOT=Path(__file__).resolve().parent.parent
DEST=ROOT/'design-comparison'
DEST.mkdir(exist_ok=True)
(DEST/'images').mkdir(exist_ok=True)
PAGES=[('home','Etusivu','',18,51,508),('demo','Web-demon esittely','web-demo/',776,51,508),('guide','Käyttöohje','guide/',18,583,430),('privacy','Tietosuoja','privacy-policy/',776,583,430)]
sections=[]
origins=[]
for name,label,route,x,y,height in PAGES:
    for variant in ('reference','desktop','mobile-full'):
        source=ROOT/f'.impeccable/review/{name}-{variant}.png'
        if source.exists():
            assert source.read_bytes()[:2]==b'\xff\xd8', source
            target=DEST/f'images/{name}-{variant}.jpg'
            origin=f'Browser screenshot of the My Lyrics documentation website, captured 2026-10-17 through the Codex in-app browser at http://127.0.0.1:5193/my-lyrics/{route}. Variant: {name}-{variant}. Own implementation of the user-approved Laulukirja concept. Unedited browser pixels, not an AI-generated screenshot.'
            comment=b'impeccable:prompt\0'+origin.encode()
            segment=b'\xff\xfe'+(len(comment)+2).to_bytes(2,'big')+comment
            data=source.read_bytes()
            target.write_bytes(data[:2]+segment+data[2:])
            origins.append({'file':target.name,'origin':origin})
    sections.append(f'''<section class="comparison-section" id="{name}"><h2>{label}</h2><div class="comparison-pair">
<figure><figcaption>Hyväksytty luonnos</figcaption><a class="comp-crop" style="--panel-height:{height};--offset-x:{-x/744*100:.6f}%;--offset-y:{-y/height*100:.6f}%" href="../docs/design-2026-10-17/images/02-laulukirja.png"><img src="../docs/design-2026-10-17/images/02-laulukirja.png" alt="Hyväksytty Laulukirja-luonnos: {label}" width="1536" height="1024" loading="lazy"></a></figure>
<figure><figcaption>Toteutus · sama leveys ja korkeus</figcaption><a href="images/{name}-reference.jpg"><img src="images/{name}-reference.jpg" alt="Toteutettu {label}, 744 pikselin leveydellä" width="744" height="{height}" loading="lazy"></a></figure></div>
<p class="comparison-links"><a href="../{route}">Avaa toteutettu sivu</a><a href="images/{name}-desktop.jpg">Työpöytä · 1440 × 900</a><a href="images/{name}-mobile-full.jpg">Puhelin · koko sivu</a></p></section>''')
mobile=''.join(f'<figure><figcaption>{label}</figcaption><a href="images/{name}-mobile-full.jpg"><img src="images/{name}-mobile-full.jpg" alt="{label} puhelimen näytöllä" width="390" loading="lazy"></a></figure>' for name,label,*_ in PAGES)
body='''<main id="main" class="site-shell comparison-main"><h1>Lämmin paperi · toteutusvertailu</h1><p class="comparison-intro">Valittu Laulukirja-luonnos ja selaimesta otetut kuvat rinnakkain. Jokainen pari käyttää samaa kuvakokoa. Kuvan napsautus avaa sen suurempana.</p><nav class="comparison-nav" aria-label="Vertailun päänäkymät">'''+''.join(f'<a href="#{name}">{label}</a>' for name,label,*_ in PAGES)+'''<a href="#mobile">Puhelin</a></nav>'''+''.join(sections)+'''<section class="comparison-section" id="mobile"><h2>Puhelimen päänäkymät</h2><p>Sama paperiteema, yhdelle palstalle sovitettu sisältö ja avattavat valikot. Kuvat näyttävät sivut kokonaisina.</p><div class="mobile-comparison">'''+mobile+'''</div></section><section class="comparison-notes"><h2>Sisältöä koskevat erot</h2><p>Tietosuojasivulla säilytettiin nykyinen seloste kokonaisuudessaan. Siksi se on pidempi kuin luonnoksen lyhennetty esimerkki. Ohjeessa on kymmenen lukua nykyisistä toiminnoista. Demon esimerkkiteksti on sovelluksen omasta englanninkielisestä käyttöohjekirjasta; käynnistyspainike avaa oikean verkkosovelluksen.</p><p>Vertailu dokumentoi sivuston ulkoasun. Sovelluksen oma käyttöliittymä säilyy erillisenä.</p></section></main>'''
html=page('Laulukirja — toteutusvertailu','Hyväksytyn luonnoksen ja toteutetun My Lyrics -sivuston visuaalinen vertailu.',body,'../',extra_head='<link rel="stylesheet" href="../assets/comparison.css">').replace('<html lang="en">','<html lang="fi">')
(DEST/'index.html').write_text(html+'\n')

if origins:
    (DEST/'images/origins.json').write_text(json.dumps(origins,indent=2)+'\n')

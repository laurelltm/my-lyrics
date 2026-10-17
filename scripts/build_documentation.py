#!/usr/bin/env python3
"""Build the static, self-hosted Laulukirja documentation pages."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parent.parent
CONTRACT = """<!--
THESIS: A songbook-shaped documentation site: cover, contents, chapters, usable live example.
OWN-WORLD: Warm #faf7f0 paper, #fcf9f2 reading surfaces, forest-green rounded actions, Source Serif and Source Sans, fine rules and botanical watercolor.
STORY: Understand My Lyrics, open the web app, read practical guidance, inspect the unchanged privacy policy.
FIRST VIEWPORT: Large serif masthead left, authentic guide-song illustration with olive sprigs right, four numbered contents columns below. Mobile stacks cover, illustration and chapter rows.
FORM: User-selected Laulukirja concept 2; approved reference docs/design-2026-10-17/images/02-laulukirja.png. User-pinned direction supersedes a new roll.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
-->"""
ICONS = {
 'arrow':'<path d="M4 12h15m-5-5 5 5-5 5"/>',
 'expand':'<path d="M14 4h6v6M20 4l-9 9M10 20H4v-6"/>',
 'book':'<path d="M12 5c-3-2-7-2-9-1v15c3-1 6-1 9 1 3-2 6-2 9-1V4c-3-1-6-1-9 1Zm0 0v15"/>',
 'library':'<path d="M5 3h15v17H5zM2 6v16h15M8 7h9M8 10h9M8 13h6"/>',
 'search':'<circle cx="10" cy="10" r="6.5"/><path d="m15 15 6 6"/>',
 'collections':'<path d="m12 3 10 6-10 6L2 9l10-6ZM3 13l9 6 9-6M3 17l9 5 9-5"/>',
 'settings':'<path d="m9 3-1 3-3 1 1 3-2 2 2 2-1 3 3 1 1 3h6l1-3 3-1-1-3 2-2-2-2 1-3-3-1-1-3H9Z"/><circle cx="12" cy="12" r="3"/>',
 'more':'<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
 'menu':'<path d="M4 6h16M4 12h16M4 18h16"/>',
 'download':'<path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/>',
 'copy':'<rect x="8" y="3" width="12" height="15" rx="1"/><path d="M16 21H4V7"/>',
 'play':'<path d="m8 4 12 8-12 8V4Z"/>',
 'check':'<path d="m5 12 5 5L20 6"/>',
}
def icon(name):
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'
def nav(base,active):
    labels=[('demo','Try online','web-demo/'),('guide','Guide','guide/'),('privacy','Privacy','privacy-policy/')]
    return ''.join(f'<a href="{base}{route}"'+(' aria-current="page"' if key==active else '')+f'>{label}</a>' for key,label,route in labels)
def header(base,active=None,fullscreen=False):
    button='Open full screen' if fullscreen else 'Open web version'
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header site-shell"><a class="wordmark" href="{base}">My Lyrics</a>
<nav class="site-nav" aria-label="Main navigation">{nav(base,active)}</nav>
<details class="mobile-menu"><summary>Menu {icon('menu')}</summary><nav class="site-nav" aria-label="Mobile navigation">{nav(base,active)}</nav></details>
<a class="button header-action" href="{base}web-demo/app/?demo=true">{button} {icon('expand' if fullscreen else 'arrow')}</a></header>'''
def footer(base):
    return f'''<footer class="site-footer site-shell"><span class="footer-brand">My Lyrics</span><a href="{base}guide/">User guide</a><a href="{base}privacy-policy/">Privacy</a><a href="mailto:laurelltm@gmail.com">Contact support</a></footer>'''
def page(title,description,body,base='./',active=None,scripts='',fullscreen=False,extra_head=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{html.escape(description,quote=True)}"><meta name="theme-color" content="#faf7f0"><title>{html.escape(title)}</title><link rel="icon" href="{base}web-demo/app/favicon.png"><link rel="preload" href="{base}assets/fonts/SourceSerif4-Regular.otf.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="{base}assets/site.css">{extra_head}</head><body>{CONTRACT}{header(base,active,fullscreen)}{body}{footer(base)}{scripts}</body></html>'''
def preview(base,linked=True):
    tag='a' if linked else 'div'
    attrs=f' href="{base}web-demo/app/?demo=true" aria-label="Open the My Lyrics web app"' if linked else ' role="img" aria-label="Example guide song, Song of Creation, in My Lyrics"'
    tabs=''.join(f'<span class="sample-tab'+(' active' if name=='Book' else '')+f'">{icon(ico)}<span>{name}</span></span>' for name,ico in [('Library','library'),('Search','search'),('Book','book'),('Collections','collections'),('Settings','settings')])
    return f'''<{tag} class="sample-book"{attrs}><div class="sample-header"><span>My Lyrics</span>{icon('search')}{icon('more')}</div><div class="sample-content"><p class="sample-number">1</p><h2 class="sample-title">Song of Creation</h2><div class="sample-verse"><span>1.</span><p class="sample-lines"><span class="sample-line">This app is empty, it starts off bare,</span><span class="sample-line">The content is yours, create if you dare.</span><span class="sample-line">Fill it with stories, melodies, and more,</span><span class="sample-line">The journey’s just started, what are you waiting for?</span></p></div><div class="sample-verse"><span>2.</span><p class="sample-lines"><span class="sample-line">Compose your own tunes, write lyrics that flow,</span><span class="sample-line">There’s no wrong answer, just give it a go.</span><span class="sample-line">The app is your canvas, your stage, your song,</span><span class="sample-line">Express what you feel, you can’t go wrong.</span></p></div></div><div class="sample-tabs" aria-hidden="true">{tabs}</div></{tag}>'''
def write(path,content):
    dest=ROOT/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(content+'\n')
def home():
    chapters=[('01','Get started','Learn the basics and take a quick tour.','guide/get-started/'),('02','Try online','Open the web app and explore a sample.','web-demo/'),('03','Books and files','Import, edit and share your songbooks.','guide/files/'),('04','Privacy and support','Read our privacy policy and get help.','privacy-policy/')]
    contents=''.join(f'<a class="chapter-link" href="{link}"><span class="chapter-number">{number}</span><h2>{title}</h2><p>{text}</p>{icon("arrow")}</a>' for number,title,text,link in chapters)
    body=f'''<main id="main" class="site-shell"><section class="home-hero" aria-labelledby="home-title"><div class="hero-copy"><h1 id="home-title" class="hero-title">My Lyrics</h1><p class="hero-subtitle">A simple songbook for<br class="desktop-break"> reading, searching and more.</p><p class="hero-description">Import, read and search songbooks. Build collections with sections, edit songs and share files — all in one place.</p><a class="button" href="web-demo/app/?demo=true">Open web version {icon('arrow')}</a></div><div class="book-illustration"><img class="botanical left" src="assets/images/botanical-sprig.png" alt="" width="1024" height="1536"><img class="botanical right" src="assets/images/botanical-sprig.png" alt="" width="1024" height="1536">{preview('./')}</div></section><nav class="chapter-contents" aria-label="Explore My Lyrics">{contents}</nav></main>'''
    write('index.html',page('My Lyrics — Your songbook, wherever you are','Read, search, edit and share your own songbooks. Try My Lyrics online or explore the user guide.',body))

def demo():
    steps=[('Read songs','Open the sample guidebook with Try example book.'),('Search lyrics','Go to Search to find a word or phrase.'),('Try collections','See how sections help organise your songs.'),('Make your own','Import songbooks, edit lyrics and share your own files.')]
    rows=''.join(f'<li><span class="step-badge">{i}</span><div><h2>{title}</h2><p>{text}</p></div></li>' for i,(title,text) in enumerate(steps,1))
    body=f'''<main id="main" class="site-shell"><div class="demo-layout"><section class="demo-intro" aria-labelledby="demo-title"><div class="chapter-title"><span class="chapter-number" aria-hidden="true">02</span><h1 id="demo-title">Try online</h1></div><p>Here you can try My Lyrics in your browser. Explore the sample songbook and see how it works.</p><ol class="step-list">{rows}</ol></section><section class="demo-stage" data-started="false" aria-label="My Lyrics web app"><div class="demo-static">{preview('../',False)}<button class="button demo-start" id="start-demo" type="button">{icon('play')} Start demo</button></div><div class="demo-live" id="live-demo" hidden><iframe id="app-demo-frame" title="My Lyrics web app" data-src="app/?demo=true" allow="clipboard-read; clipboard-write"></iframe></div><p class="demo-feedback" id="demo-feedback" role="status" aria-live="polite"></p></section></div><section class="demo-note" aria-label="About the browser version"><p>Your library is saved in this browser. Keep an exported backup before clearing browser data or changing devices. Native cloud backup options depend on the platform.</p><a class="inline-link" href="../guide/get-started/">Next: bring your own songbooks {icon('arrow')}</a><noscript><p>JavaScript is needed to run the app. <a href="app/?demo=true">Open the web app directly</a> or read the guide.</p></noscript></section></main>'''
    write('web-demo/index.html',page('Try My Lyrics online','Try the real My Lyrics web app with the built-in example book. Read, search, create collections and edit songs.',body,'../','demo','<script src="demo.js" defer></script>',True))

TOPICS=[
('get-started','01','Get started','Get started', 'Start with the built-in guidebook, or bring a songbook of your own.',[
 ('Try the example book','Choose Try example book on the welcome screen. If you already have a library, open the Library menu and choose Try the example book.'),
 ('Import a book','In Library, open the top-right menu and choose Import a file. Select a .books or JSON file. A backup can also be imported here when you only want its books.'),
 ('Review before importing','Check the preview and confirm the books to add. When a matching book exists, Replace current is the first default option; choose Keep both to retain a separate copy.'),
 ('Keep your content safe','Imported books remain available on your device. Export a .mylyrics backup somewhere you can find after changing devices. In the browser, do not clear site data before exporting.')],None),
('reading','02','Reading and navigation','Reading and navigation','The Library shows your songbooks. Open a book, then use the tabs below to move around the app.',[
 ('Open a book','Use Library to open a songbook. Book returns to your current book.'),
 ('Read and move between songs','Swipe sideways to change songs. Tap the song number to jump directly.'),
 ('Search for lyrics','Search the current book or all books, then open a matching result.'),
 ('Use collections','Organise songs into sections. Book and Collections keep separate reading positions.')],None),
('files','03','Books and files','Books and files','A book contains songs, and each song contains verses or choruses. Plain JSON is a good starting point when creating your own files.',[], 'files'),
('collections','04','Collections and sections','Collections and sections','Keep frequently used songs together, or arrange a program with sections in a specific order.',[
 ('Create a collection','Open Collections and choose the plus button. Create a new collection or import an existing .collection.books file. Free song list, Singalong and Choir practice offer different starting structures.'),
 ('Add songs','Open a song’s top-right action menu and choose Add to collection. Select a collection and section. Your last destination is remembered for the next addition.'),
 ('Read or organise','A collection opens in preview. Tap Start or a song row to read it. To organise it, open the preview menu and choose Edit. Drag songs within or between sections, then choose Done.'),
 ('Use Favorites','Favorites is a flat list of links to songs in their source books. It has no sections or Start button. Removing a favorite removes only its link; the song stays in the book.')],'<h2>Keep your place</h2><p>Swipe sideways through a collection, including across section boundaries. The top-left arrow returns to that collection’s preview. After a full app restart, Collections returns to the overview.</p><h2>Remove a song</h2><p>When reading from an open collection, the song menu offers Remove from collection. Undo restores the same entry, section and position.</p>'),
('editing','05','Editing songs','Editing songs and drafts','Write new songs or adjust an existing song without losing unfinished work.',[
 ('Create or edit','Go to Settings → Drafts → New song, or choose Edit song from a song’s top-right menu. The title and song number are optional.'),
 ('Build the song','Add verses and choruses as separate parts. Edit, copy and reorder those parts. Changes are saved in a draft while you work.'),
 ('Preview and save','Choose Preview → Save to book, then select the destination book. Saving a draft alone does not add the finished version to the book.'),
 ('Continue later','When leaving, choose Keep draft to return later under Settings → Drafts. Continue editing or discard changes only when that is what you intend.')],None),
('sharing','06','Sharing files','Sharing songs, books and collections','Share structured text in a message, or send a file that another My Lyrics user can import.',[
 ('Share a song','From Song actions, choose Share song. Text is useful for a message or notes. A .mylyricsong file lets the recipient import the song into a collection.'),
 ('Share books','The Library menu’s Share library action lets you select books. Sharing books creates a .books file; it does not include your collections or settings.'),
 ('Share a collection','Use the collection preview’s menu, or press and hold a collection in the overview. A text share includes sections and lyrics; a .collection.books file includes the collection and its songs.'),
 ('Receive a file','Open the file in My Lyrics or select the matching import action. Review the preview before confirming. Imported collections are created separately and preserve your existing collections.')],None),
('appearance','07','Reading preferences','Reading preferences','Choose a comfortable reading style for your eyes and the place where you sing.',[
 ('Adjust the text','Open Settings → Text appearance. Change size, weight, alignment and line spacing. The preview shows a first-verse number so you can see the effect of the verse-number setting.'),
 ('Choose a theme','Settings → Theme offers eight visual theme families. Within a family, choose light, dark or the device appearance. Warm paper and Parchment are two of the choices.'),
 ('Show song titles','Press and hold a book cover and choose Show song titles. Enabled titles appear below the normal tappable song number. The title is always optional.'),
 ('Use full-screen reading','Tap the lyrics to hide the top and bottom bars. Tap again or scroll to the start or end to restore them. The song heading remains visible. Turn off tap-to-full-screen in Text appearance if you prefer.')],None),
('backup','08','Backup and restore','Backup and restore','Keep a transferable copy of your books, collections, settings and drafts.',[
 ('Create a backup','Open Settings → Backup. Back up now creates a copy; Export file saves a .mylyrics file you can move or keep elsewhere. Browser libraries should also be backed up before site data is cleared.'),
 ('Use platform cloud options','The iPhone app supports iCloud. On Android, explicitly connect Google Drive from Backup settings. Browser cloud options differ; use file export for a transferable backup.'),
 ('Inspect and compare','Opening backup or restore reads the available copies and shows a loading indicator. You can cancel the inspection. Identical-content indicators ignore reading position and history.'),
 ('Restore deliberately','Review the restore preview before confirming. Merge with current keeps existing content. Replace current first creates a local safety copy. Nothing is restored automatically at app startup.')],'<h2>Moving between platforms</h2><p>The same .mylyrics backup file works on iPhone and Android. Transfer it yourself and review restoration. Cloud copies do not provide live synchronization or automatic transfer between platforms.</p><h2>Import only the books</h2><p>Use Library → Library menu → Import a file and choose the backup. Full backup restoration is a separate action under Settings → Backup. The legacy .mylyricsbackup format is also readable.</p>'),
('language','09','App language','App language','My Lyrics supports 40 interface languages. Your song content stays in the language in which it was written.',[
 ('Follow the device language','System default chooses the first supported language in your device’s preferred-language list. If none matches, My Lyrics uses English.'),
 ('Choose a language','Open Settings → Language and choose the language you want. The interface changes immediately and the choice is kept after restarting.'),
 ('Keep your own words','Changing the interface language does not translate lyrics, book names or collection content. Bundled app translations and the in-app guide remain available offline.')],None),
('support','10','Troubleshooting','Troubleshooting and support','A few checks solve the most common issues. Keep a backup before removing the app or clearing browser data.',[
 ('A song is missing','Check that the correct book has been imported. Search all books with a few words from the lyrics. Number navigation always uses the open book.'),
 ('A file will not open','Save it to your device first, then select it in the app’s import flow. Check the extension below. If the file is damaged, ask the sender to share it again.'),
 ('The text is hard to read','Adjust Text appearance and Theme in Settings. Try a larger size, stronger weight or a higher-contrast theme.'),
 ('Ask for help','Email laurelltm@gmail.com. Describe what you were doing, the platform and the app version. Avoid sending private songbook content unless you want to include it.')],'<h2>Browser storage</h2><p>Your web library belongs to this browser and site. Private browsing, browser cleanup or site-data removal may erase it. Export a backup before changing browsers or clearing data.</p>'),
]
def topic_link(topic,base):
    return base+'guide/'+('' if topic[0]=='reading' else topic[0]+'/')
def guide_nav(current,base):
    return '<nav class="guide-nav" aria-label="Guide chapters">'+''.join(f'<a href="{topic_link(t,base)}"'+(' aria-current="page"' if t[0]==current else '')+f'><span>{t[1]}</span><span>{t[2]}</span></a>' for t in TOPICS)+'</nav>'
def code_sample():
    sample={'title':'My Lyrics','songs':[{'number':1,'title':'Song of Creation','verses':[{'number':1,'sentences':['This app is empty, it starts off bare,','The content is yours, create if you dare.']}]}]}
    return json.dumps(sample,indent=2)
def highlighted_code(text):
    import re
    safe=html.escape(text)
    return re.sub(r'(&quot;[^\n]*?&quot;)(\s*:)?',lambda m:f'<span class="json-key"'+'>'+m[1]+'</span>'+m[2] if m[2] else '<span class="json-string">'+m[1]+'</span>',safe)
def example_aside(base):
    code=code_sample()
    return f'''<aside class="guide-example" aria-label="Example songbook file"><h2>Example songbook file</h2><p>Songbooks are simple JSON files. Here is a small example with one song from the My Lyrics guidebook.</p><div class="code-box"><button class="copy-button" type="button" data-copy="sample-json" aria-label="Copy example JSON">{icon('copy')}<span>Copy</span></button><pre tabindex="0"><code id="sample-json">{highlighted_code(code)}</code></pre></div><a class="guide-download" download href="{base}downloads/my-lyrics-example.json">{icon('download')} Download example songbook</a><p class="copy-feedback" role="status" aria-live="polite"></p></aside>'''
def files_content(base):
    types=[('.books','One or more books','Library → Library menu → Import a file'),('.json / .zip','Book content and compatible legacy archives','Import books'),('.collection.books','A collection, its sections and songs','Collections → plus → Import collection from file'),('.mylyricsong','One transferable song','Open the received file and choose a collection'),('.mylyrics','A complete backup','Settings → Backup → Restore from a file')]
    rows=''.join(f'<tr><td><code>{ext}</code></td><td>{what}</td><td>{where}</td></tr>' for ext,what,where in types)
    fields=[('title','string','Book name. A song title is optional.'),('songs','array','The songs in a book.'),('number','number','Optional song or verse number.'),('verses','array','The parts of a song.'),('sentences','array of strings','The lines in a verse or chorus.'),('coverImage','string','Optional base64-encoded book cover.'),('headingStyle','numbers / titles','Optional book setting; titles adds the title below the number.')]
    fs=''.join(f'<tr><td><code>{field}</code></td><td>{kind}</td><td>{meaning}</td></tr>' for field,kind,meaning in fields)
    return f'''<div class="guide-text"><h2>Choose the right file</h2><table class="field-table"><thead><tr><th>File</th><th>Contains</th><th>Where to open</th></tr></thead><tbody>{rows}</tbody></table><h2>Create a JSON songbook</h2><p>Start with the downloadable example. Change its book title, songs and sentences in a plain-text editor. Save it as UTF-8 JSON, then import it through the Library menu. You can share the imported book from My Lyrics to produce a .books package.</p><table class="field-table"><thead><tr><th>Field</th><th>Type</th><th>Meaning</th></tr></thead><tbody>{fs}</tbody></table><h2>Use the app for packaged files</h2><p>Book, song, collection and backup exports have different structures. Use the app’s share or export actions to create them. Renaming a file does not convert its contents.</p><p>The legacy <code>.mylyricsbackup</code> format remains readable. Import a backup through Library when you want only its books, or use Backup settings for a full restore.</p><p><a href="{base}lorem_ipsum_songbook.json" download>Download the original JSON format example</a></p></div>'''
def guides():
    for index,t in enumerate(TOPICS):
        slug,number,label,title,intro,steps,extra=t
        base='../' if slug=='reading' else '../../'
        tabs=''
        if slug=='reading':
            tabs='<div class="reading-tabs" role="img" aria-label="The app tabs are Library, Search, Book, Collections and Settings">'+''.join(f'<span class="sample-tab'+(' active' if name=='Library' else '')+f'">{icon(ico)}<span>{name}</span></span>' for name,ico in [('Library','library'),('Search','search'),('Book','book'),('Collections','collections'),('Settings','settings')])+'</div>'
        rows=''.join(f'<li><span class="step-badge">{i}</span><div><h2>{h}</h2><p>{text}</p></div></li>' for i,(h,text) in enumerate(steps,1))
        content=files_content(base) if extra=='files' else f'<ol class="step-list">{rows}</ol>'+(f'<div class="guide-text">{extra}</div>' if extra else '')
        prev=TOPICS[index-1] if index else None; nxt=TOPICS[index+1] if index<len(TOPICS)-1 else None
        pager='<nav class="chapter-pager" aria-label="Previous and next chapters">'+(f'<a href="{topic_link(prev,base)}">{icon("arrow")} {prev[2]}</a>' if prev else '<span></span>')+(f'<a href="{topic_link(nxt,base)}">{nxt[2]} {icon("arrow")}</a>' if nxt else '')+'</nav>'
        nav_html=guide_nav(slug,base)
        body=f'''<main id="main" class="site-shell"><div class="guide-layout"><aside class="guide-sidebar">{nav_html}</aside><article class="guide-article"><details class="mobile-guide-contents"><summary>Guide contents {icon('menu')}</summary>{nav_html}</details><div class="chapter-title"><span class="chapter-number" aria-hidden="true">{number}</span><h1>{title}</h1></div><p class="intro">{intro}</p>{tabs}{content}{pager}</article>{example_aside(base)}</div></main>'''
        path='guide/index.html' if slug=='reading' else f'guide/{slug}/index.html'
        write(path,page(f'{title} — My Lyrics guide',intro,body,base,'guide',f'<script src="{base}assets/site.js" defer></script>'))
def privacy():
    data=json.loads((ROOT/'content/privacy.json').read_text())
    rows=''.join(f'<section class="policy-row"><h2>{s["title"]}</h2><p>{s["html"]}</p></section>' for s in data['sections'])
    body=f'''<main id="main" class="site-shell legal-page"><h1>Privacy Policy</h1><p class="effective-date">Effective date: {data['effectiveDate']}</p><p class="legal-intro">{data['introduction']}</p><div class="policy-sections">{rows}</div></main>'''
    write('privacy-policy/index.html',page('Privacy Policy — My Lyrics','Privacy policy for the My Lyrics app and support website.',body,'../','privacy'))
def downloads():
    source=json.loads((ROOT/'web-demo/app/assets/assets/static_book.json').read_text())
    source['headingStyle']='titles'
    write('downloads/my-lyrics-example.json',json.dumps(source,ensure_ascii=False,indent=2))
if __name__=='__main__':
    home(); demo(); guides(); privacy(); downloads()

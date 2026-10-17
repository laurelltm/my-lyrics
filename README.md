# My Lyrics — documentation and web demo

My Lyrics is a songbook reader for your own books and lyrics. Read and search songs, create collections with sections, edit drafts, share books and songs, and export backups.

- [Open the website](https://laurelltm.github.io/my-lyrics/)
- [Try the web app](https://laurelltm.github.io/my-lyrics/web-demo/)
- [Read the user guide](https://laurelltm.github.io/my-lyrics/guide/)
- [Songbook files and JSON format](https://laurelltm.github.io/my-lyrics/guide/files/)
- [Privacy policy](https://laurelltm.github.io/my-lyrics/privacy-policy/)
- [Approved design and visual comparison](https://laurelltm.github.io/my-lyrics/design-comparison/)

Support: [laurelltm@gmail.com](mailto:laurelltm@gmail.com).

## Documentation website

The site uses static HTML, shared CSS and small progressive enhancements. Adobe Source Serif 4 and Source Sans 3 are served locally with their OFL licenses. No external font or analytics service is added.

The warm-paper Laulukirja design was selected from [five proposals](docs/design-2026-10-17/README.md). The approved visual reference is [concept 2](docs/design-2026-10-17/images/02-laulukirja.png). `DESIGN.md` records the implemented design system.

To regenerate the committed pages after changing their source:

```bash
python3 scripts/build_documentation.py
python3 scripts/verify_documentation.py
```

The generator creates the homepage, demo introduction, ten guide chapters and the privacy page. The original privacy paragraphs and date are preserved in `content/privacy.json`. The comparison page is generated separately from verified browser captures:

```bash
python3 scripts/build_design_comparison.py
```

Preview the entire website with the GitHub Pages path prefix:

```bash
./scripts/preview_web_demo.sh
```

Open `http://127.0.0.1:5179/my-lyrics/`. The server is local to this Mac. Stop it with Ctrl-C.

## Real web app

`web-demo/app/` contains the Flutter app, separate from the documentation site. The introduction loads it only after **Start demo**; the header also links directly to the full-screen app. There is no decorative phone camera covering the app.

To rebuild the app bundle from the adjacent Flutter checkout:

```bash
./scripts/build_web_demo.sh
```

The current bundle is version 2.0.0 from app commit `21bae6d1a2f413a4b1b9c1a32a58c89a118ad0fe`. The website redesign does not change that bundle. Browser content is stored locally; export a backup before clearing browser data.

## Example files

[Download the app’s own English guidebook](downloads/my-lyrics-example.json), or inspect the older [JSON format example](lorem_ipsum_songbook.json). The guide explains `.books`, JSON, song, collection and backup files. Use the app’s export actions to create packaged files; renaming a file does not convert it.

## Publishing

The existing GitHub Pages workflow publishes the static artifact on a push to `main`. It copies the site, guide, assets, downloads, visual comparison and unchanged web app. Publishing this documentation site is explicitly authorized by the repository owner; native app releases remain a separate process.

# My Lyrics documentation website

<!-- impeccable:product-schema 1 -->

## Platform

web

## Product Purpose

The GitHub Pages site provides My Lyrics documentation and a publicly usable web version of the current application. The user has explicitly requested that the published web version follow the latest app implementation.

## Operating Context

The website lives in `laurelltm/my-lyrics`. The Flutter application source lives in the sibling `open_songbook_3` checkout. The site is deployed as static files through GitHub Pages. Its current main surfaces are the support homepage, web-demo introduction with an embedded app, book-file documentation, and privacy policy.

## Capabilities and Constraints

- Five alternative designs are requested as images of all four main surfaces, hosted in a GitHub Pages gallery and embedded into the Markdown proposals. This visual format was confirmed by the user on 2026-10-17.
- The application’s internal Library, Search, Book, Collections and Settings views are outside this design proposal. This boundary was confirmed by the user on 2026-10-17.
- A design is to be selected before any website redesign is implemented.
- Updating the compiled web application is a separately authorized publication task.
- Preserve working document URLs and the application's GitHub Pages base path.
- Changes to store privacy-policy links are deferred; the old Amazon S3 PDF must remain untouched.

## Brand Commitments

The public product name is My Lyrics. The application's existing logo and real example-book content are available; do not invent customer endorsements, adoption figures or performance benchmarks.

## Evidence on Hand

- `index.html`: support homepage.
- `README.md`: book-file documentation and build instructions.
- `web-demo/index.html`, `styles.css`, `demo.js`: demo presentation.
- `web-demo/app/`: compiled Flutter application.
- `privacy-policy/index.html`: current privacy policy.
- `lorem_ipsum_songbook.json`: downloadable example content.

## Open Decisions

The user has not selected the site's future visual direction. Intended audience priorities and the scope of future website localization are not separately confirmed. The proposals label these as design assumptions, rather than product commitments.

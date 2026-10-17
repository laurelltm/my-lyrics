# Laulukirja Website Implementation Plan

> **For agentic workers:** Execute the approved direction in this session. Use the Impeccable asset producer, finish reviewer and documenter at their required gates.

**Goal:** Reproduce the user-approved Laulukirja concept across the homepage, live demo, guide and privacy page, then provide a visual comparison and publish the verified site.

**Architecture:** Static semantic HTML and one shared stylesheet preserve GitHub Pages routes. The existing Flutter bundle is reused unchanged; the homepage uses a semantic noninteractive illustration of the actual English guide song, and the demo offers an explicitly started real iframe. A static comparison page pairs the approved reference with browser captures.

**Tech Stack:** HTML, CSS, small progressive-enhancement JavaScript, self-hosted Adobe Source Serif 4 and Source Sans 3, Python standard-library verification, existing GitHub Pages workflow.

## Global Constraints

- Approved authority: `docs/design-2026-10-17/images/02-laulukirja.png`; preserve its paper, forest-green, serif, editorial topology.
- Retain `/`, `/web-demo/`, `/web-demo/app/`, `/privacy-policy/` and downloadable example URLs.
- Native app code and compiled Flutter bundle remain unchanged in this redesign.
- Preserve the existing privacy policy text and date; store privacy links and S3 remain out of scope.
- No new tracking, invented claims or user songbook content. Use only the application's own English guide lyrics.
- Desktop reference panel: 744 × 508; also verify desktop 1440 px and mobile 390 px, plus overflow at 320 px.
- Real demo runs only after user starts it, without trapping parent-page scrolling. Frameless app surface has no camera overlay.

## Tasks

### 1. Establish approved visual material

- [x] Record concept 2 approval in PRODUCT.md and its prompt sidecar.
- [x] Inventory reference: paper ground, serif wordmark/display, green pills, hairline dividers, botanical sprig, sample-song preview, chapter navigation.
- [x] Obtain self-hosted fonts and OFL licenses; asset producer supplies one transparent botanical sprig with exact-prompt provenance.

### 2. Build the four principal surfaces

- [x] Shared `assets/site.css`: paper `#faf7f0`, reading `#fcf9f2`, ink `#23231e`, forest `#2f604b`, pale olive step badges and warm rules; derive final token values from reference pixel sampling.
- [x] Homepage: two-column book-cover composition, large My Lyrics masthead, actual sample song preview with botanical frame, four-column chapter contents becoming rows on mobile.
- [x] Demo: numbered chapter introduction and four short steps left; restrained app surface right; direct full-screen link and working start/load/fallback controls.
- [x] Guide: desktop chapter sidebar, current reading article and JSON example column; useful complete anchored chapters and separate file-format reference; mobile native contents disclosure.
- [x] Privacy: header, date, unchanged complete policy text styled as editorial rows; mobile single-column document.

### 3. Verify content and working paths

- [x] All internal links, local image/font/script references and downloads resolve in a Pages-shaped local preview.
- [x] Confirm policy paragraphs/date equal baseline, published app bundle byte-for-byte unchanged, no third-party font requests.
- [x] Browser: start demo, navigate sample song, test full-screen link, copy JSON, navigate guide chapters and mobile contents. Inspect loading and no-JS paths.

### 4. Compare and close visual review

- [x] Capture each page at reference panel dimensions, desktop and mobile; inspect all four pages together before batching corrections.
- [x] Build comparison page with approved panels and actual renders side-by-side; include mobile captures.
- [x] Run mechanical detector once; send reference, captures, source and known limits to fresh Impeccable finish reviewer. Apply one batch and confirm the reviewer's fixes.
- [x] Run documenter over completed site to record DESIGN.md, leaving concepts unselected except concept 2.

### 5. Publish verified result

- [x] Update Pages artifact paths for shared assets, guide and visual comparison.
- [ ] Commit and push feature source, fast-forward main after successful checks, verify Pages job and live asset hashes.
- [ ] Verify live homepage/demo and comparison URL; send final notification and user links with image proof.

## Review evidence

The Impeccable finish reviewer scored all three material corrections resolved (`ship`, fix-list scope). See `.impeccable/review/finish-review.md` and `finish-verdict.md`. `DESIGN.md` and `.impeccable/design.json` record the completed world. Static verification covers 14 pages; original legal paragraphs and compiled app are unchanged. Browser captures and responsive checks are recorded under `.impeccable/review/`, with publishable image copies under `design-comparison/images/`. Publication is verified after this source commit by the Pages workflow and live URL/hash checks.

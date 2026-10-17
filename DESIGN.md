---
name: My Lyrics documentation
description: A warm-paper songbook publication with forest-green actions and practical numbered chapters.
colors:
  paper: "#faf7f0"
  reading: "#fcf9f2"
  ink: "#23231e"
  muted: "#655f53"
  forest: "#2f604b"
  forest-hover: "#214c39"
  sage: "#d8e2cf"
  line: "#c7c3b9"
  soft-line: "#e3ded2"
  action-text: "#ffffff"
  code-paper: "#f7f2e9"
typography:
  display:
    fontFamily: "Source Serif, Georgia, serif"
    fontSize: "clamp(80px, 11.8vw, 136px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Source Serif, Georgia, serif"
    fontSize: "clamp(36px, 5vw, 64px)"
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Source Serif, Georgia, serif"
    fontSize: "clamp(18px, 2.35vw, 28px)"
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "-0.03em"
  body:
    fontFamily: "Source Serif, Georgia, serif"
    fontSize: "clamp(16px, 1.4vw, 20px)"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Source Sans, Arial, sans-serif"
    fontSize: "clamp(14px, 1.15vw, 17px)"
    fontWeight: 400
    lineHeight: 1.55
  action:
    fontFamily: "Source Sans, Arial, sans-serif"
    fontSize: "clamp(14px, 1.2vw, 18px)"
    fontWeight: 600
    lineHeight: 1.25
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Consolas, monospace"
    fontSize: "clamp(9px, 0.84vw, 12px)"
    fontWeight: 400
    lineHeight: 1.65
rounded:
  action: "16px"
  reading: "10px"
  download: "8px"
  inset: "6px"
  control: "4px"
  badge: "50%"
spacing:
  small: "8px"
  compact: "12px"
  regular: "16px"
  comfortable: "20px"
  section: "24px"
  wide: "32px"
  chapter: "48px"
  gutter: "clamp(20px, 5.35vw, 80px)"
components:
  button-primary:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.action-text}"
    typography: "{typography.action}"
    rounded: "{rounded.action}"
    padding: "10px 20px"
  button-primary-hover:
    backgroundColor: "{colors.forest-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.forest}"
    typography: "{typography.action}"
    rounded: "{rounded.action}"
    padding: "10px 20px"
  button-secondary-hover:
    backgroundColor: "{colors.sage}"
  guide-navigation-active:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.action-text}"
    padding: "10px 12px"
  step-badge:
    backgroundColor: "{colors.sage}"
    rounded: "{rounded.badge}"
    size: "30px"
  reading-panel:
    backgroundColor: "{colors.reading}"
    rounded: "{rounded.reading}"
  code-panel:
    backgroundColor: "{colors.code-paper}"
    typography: "{typography.code}"
    rounded: "{rounded.inset}"
    padding: "16px 12px"
---

# Design System: My Lyrics documentation

## Overview

**Creative North Star: "Laulukirja — the warm-paper songbook"**

This website reads as a small edited publication: a confident serif cover, numbered contents, useful chapters and a quiet legal document. Warm paper, botanical watercolor and restrained green actions give the practical material a familiar, literary character. The user selected concept 2 in `docs/design-2026-10-17/images/02-laulukirja.png`; that image remains the visual authority.

This system covers the homepage, demo introduction, ten guide pages and privacy policy. It describes the built documentation site, not the independent Flutter application inside `web-demo/app/`. Its source of truth is `assets/site.css` and the generated pages from `scripts/build_documentation.py`; the surface brief owns page-specific composition.

**Key Characteristics:**

- Oversized serif masthead, ordinary sentence case and numbered chapters.
- Pale paper fields, fine rules and sparse forest-green emphasis.
- A real guide-song reading illustration framed by watercolor sprigs.
- Spacious full-size reading layouts, an intentional compact reference spread and stacked mobile pages.

## Colors

The palette pairs warm neutral paper with a single forest accent and soft sage support.

### Primary

- **Forest:** primary actions, links, chapter numbers and selected guide navigation. Forest Hover deepens filled actions on hover.
- **Sage:** numbered instruction badges, text selection and quiet secondary hover surfaces.

### Neutral

- **Paper:** the uninterrupted page field. **Reading:** the slightly lighter song panel, mobile menu and small copy control.
- **Ink:** serif content and ordinary navigation. **Muted:** secondary notes and footer text.
- **Line:** structural dividers and secondary control borders. **Soft Line:** inset panels, tables and subsidiary separation.
- **Action Text:** white text on filled forest controls and selected guide rows. **Code Paper:** the warmer JSON inset.

**The Paper First Rule.** Large page regions stay on paper; color blocks identify an action or current chapter rather than enclosing every section.

## Typography

**Display Font:** self-hosted Adobe Source Serif 4, registered as `Source Serif`, with Georgia and serif fallbacks. **Body Font:** the same serif. **Label Font:** self-hosted Adobe Source Sans 3, registered as `Source Sans`, with Arial and sans-serif fallbacks. Regular and semibold WOFF2 files and their OFL licenses live in `assets/fonts/`; no external font service is used.

The hierarchy is intentionally broad: a large literary masthead, medium serif chapter headings, readable serif prose, and small sans navigation/action labels. Headings use regular weight and slight negative tracking; semibold marks instruction titles and selected supporting content. JSON uses the platform monospace stack.

- **Display:** the homepage masthead uses the frontmatter display role; mobile changes it to `clamp(68px, 19vw, 100px)`.
- **Headline:** ordinary page titles inherit the headline role; chapter, guide and legal titles apply their observed surface scales. Mobile guide titles are 32px and legal titles 42px.
- **Title:** contents headings use the title role, with 23px mobile headings and the compact spread adjustment described below.
- **Body:** the base role becomes 17px on mobile. Guide prose reaches 18px on a wide desktop; legal text uses a generous line height and roughly 76ch maximum measure.
- **Label / Action:** sentence-case sans navigation, buttons, feedback and small controls; action weight is 600.
- **Code:** compact JSON preserves whitespace and scrolls within its own panel. Mobile code is 11px with a taller copy-control clearance.

**The Two Voices Rule.** Serif carries the publication and its reading content; sans identifies controls. Do not turn the whole site into an application toolbar.

## Layout

The centered page shell is capped at 1280px, with the fluid gutter in frontmatter on each side. Repeated gaps follow the recorded spacing steps. Thin horizontal rules divide major regions; vertical rules separate desktop contents, chapter numbering and guide columns.

Above 680px, the home cover uses a left copy column and right reading illustration, followed by four contents columns. The demo uses an introduction beside a taller reading panel. Guides use a sticky chapter rail, central article and JSON example column. Privacy sections pair a short label with longer prose.

**The Compact Spread Rule.** Between 681px and 900px, preserve the explicitly selected reference composition as a distinct density mode: the home contents headings are 16px; the guide is an intentionally small three-column spread with 11–12px article text and compressed spacing. The 744px reference captures are the acceptance evidence for this mode. These values are not the general reading scale for new pages or wider/mobile layouts; inspect legibility separately when extending this range.

At 680px and below, use one column: home copy precedes the framed song, contents become ruled rows, demo introduction precedes its stage, and policy labels sit above their paragraphs. Native disclosures replace the header links and guide rail; the guide example follows the article. The home illustration clips its decorative overflow within its own region, keeping recognizable leaf groups visible without page overflow. At 390px, navigation and direct app access both remain in the header.

## Elevation & Depth

Depth is mostly tonal: pale reading paper, restrained outlines and fine rules. Soft shadows belong to the reading panel and its live-demo replacement, the mobile navigation overlay and the overlaid Start demo action. Ordinary chapters and legal rows remain flat.

- **Reading panel:** `0 5px 15px #33281820`.
- **Mobile menu:** `0 8px 16px #33281812`.
- **Demo launch control:** `0 4px 16px #33281818`.

**The Reading Surface Rule.** Preserve the light physical separation of the song panel; do not spread its shadow to every content section.

## Shapes

Rounded rectangles soften controls and reading surfaces without implying device hardware. Primary actions use the action radius; the smaller mobile header action uses 14px. Reading and live-demo panels share the reading radius, while JSON/tab insets and downloads use the smaller recorded corners. Numbered sage badges are circles. Chapter rails and editorial rows stay square. Borders are thin, generally one pixel. Icons are consistent stroked inline SVGs, usually 18–20px, with rounded caps and joins.

## Components

**Buttons.** Forest fill, white semibold sans text, 10px by 20px padding and a minimum 44px target. Hover deepens forest over 160ms ease-out. Secondary actions use a line border, forest text and sage hover. Mobile cover actions have a 50px minimum height. Disabled actions reduce opacity and use a progress cursor.

**Navigation.** Desktop header links are plain ink sans labels, with a fine green underline for the current page. The mobile Menu is a native disclosure over reading paper. Guide navigation uses serif numbered rows and a square forest/white active row; unselected hover is sage. The mobile chapter disclosure keeps the same labels and selection.

**Chapter and instruction patterns.** Contents use large green two-digit numbers and fine dividers. Chapter headings pair number and title across a vertical rule. Ordered instruction lists use small sage circular numbers with serif headings and explanations. Privacy rows reuse the ruled editorial structure without card containers.

**Reading illustration.** A pale, softly raised song panel contains the real English “Song of Creation” guidebook content and five labelled SVG tabs. It is an illustration rather than invented hardware; the homepage panel links to the app. Botanical sprigs are decorative images with empty alt text. Preserve their asset provenance and keep foliage clear of lyrics and adjacent copy.

**Demo stage.** Start demo explicitly replaces the static illustration with the real app iframe. The direct full-screen route is also available in the header. A polite status message communicates loading, browser storage and fallback access; the parent page does not trap scrolling.

**Code example.** A softly outlined, warm JSON panel preserves indentation and internal scrolling. A labelled Copy button provides status feedback and a persistent download follows it. Table rows use light rules rather than a grid of heavy boxes.

**Interaction floor.** Keyboard focus uses a 3px forest outline with 5px offset; the linked song panel increases its offset to 8px. The skip link appears on focus. Reduced-motion preference removes transitions; print removes controls, ornament and the guide rail while preserving reading content. The prior regex-only detector is not a computed contrast verdict.

## Do's and Don'ts

### Do:

- **Do** preserve the user-selected Laulukirja reference and the self-hosted serif/sans pairing.
- **Do** use thin rules, numbered structure and paper fields to organise reading.
- **Do** keep decorative foliage recognizable, within page width and clear of text.
- **Do** retain explicit demo launch, visible keyboard focus and native mobile disclosures.
- **Do** preserve the real guide example, all privacy text and its date when restyling.

### Don't:

- **Don't** inherit this website's typography or colors into the independent Flutter app.
- **Don't** replace the simple reading surface with a fake phone camera or hardware frame.
- **Don't** promote the compact reference spread's small guide type into the default body scale.
- **Don't** introduce external font requests, tracking or a parent-page scroll lock.
- **Don't** replace the established inline SVG icon system with glyph icons or add decorative eyebrows and hard offset shadows.

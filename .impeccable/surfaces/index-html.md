---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["web-demo/index.html","guide/index.html","privacy-policy/index.html"]
---

# Laulukirja documentation website

Scope: homepage, demo introduction, ten guide chapters and privacy page. Homepage persuades by demonstrating the real guide song; guide and privacy are Read surfaces. Demo introduction helps a new visitor start the web app.

Audience: songbook readers and people preparing their own files. Primary action: open the web app. Secondary action: find practical guidance. Use only the app's English example guidebook in illustrations and downloadable examples.

Pinned direction: user approved concept 2, Laulukirja / Lämmin paperi · toimitettu julkaisu, from `docs/design-2026-10-17/images/02-laulukirja.png`. Its editorial cover, botanical sprigs, serif typography, forest actions and numbered chapter structure govern the implementation. The comp outranks earlier prose proposals. The mobile cover stacks; native disclosure menus keep chapter navigation compact.

Constraints: retain public routes and compiled Flutter bundle. Preserve all privacy paragraphs and date. No new analytics or font-service calls. Real app is loaded on explicit Start demo; direct full-screen link remains immediately available. Browser storage and backup limitations are stated. No fake phone camera or parent scroll lock.

Proof: `/design-comparison/` pairs all four main views with the approved comp and includes complete mobile captures. No unresolved creative decisions; only implementation and verified publication remain.

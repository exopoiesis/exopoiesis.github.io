# exopoiesis.space

Website for the Third Matter / Exopoiesis research project.

**Live:** [https://exopoiesis.space](https://exopoiesis.space)

## About the project

We are designing a minimal chemical system — built from iron sulfide minerals — that maintains its own boundary, drives its own metabolism, and persists without being alive. A "Third Matter" at the boundary between chemistry and biology.

## Tech

Jekyll site hosted on GitHub Pages. No JavaScript, no external dependencies.

- Dark theme with iron sulfide–inspired color palette
- Responsive (mobile-friendly)
- Multilingual: English, Russian, Chinese
- Custom domain via CNAME

## Structure

```
_config.yml          — Jekyll config
_data/i18n.yml       — UI strings (en/ru/zh)
_layouts/            — default, post, vision
_includes/           — head, nav, footer
_posts/              — blog posts (lang in front matter)
_visions/            — vision pieces (lang in front matter)
en/                  — English pages
ru/                  — Russian pages
zh/                  — Chinese pages
assets/css/style.css — all styles
```

## Adding content

**Blog post:** create `_posts/YYYY-MM-DD-slug.md` with front matter:
```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD
lang: en          # en, ru, or zh
categories: [en]  # must match lang
---
```

**Vision:** create `_visions/slug.md` with front matter:
```yaml
---
layout: vision
title: "Title"
subtitle: "Optional subtitle"
lang: en
permalink: /en/visions/slug/
---
```

## Related repositories

- [sulfide-proton-barriers](https://github.com/exopoiesis/sulfide-proton-barriers) — NEB/MD calculations of proton diffusion in iron sulfide minerals

## AI Collaboration Disclosure

This project is developed through human–AI collaboration using Claude (Anthropic). Site content, design, and code were co-created with Claude Code.

## License

Code: MIT. Content: CC-BY-4.0.

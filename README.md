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

**Blog post:** create `_posts/YYYY-MM-DD-slug.md` (one file per language) with front matter:
```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD
lang: en          # en, ru, or zh
ref: my-post      # SAME ref across all 3 language versions — drives the language switcher
categories: [en]  # must match lang; controls the /<lang>/blog/... permalink
---
```
The language switcher (`_includes/nav.html`) links the three versions by matching
`ref` + `lang` across `site.documents`. Omit `ref` and the switch falls back to the
language home page instead of the translated post.

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

## Local preview (Docker)

No Ruby/Jekyll is installed on the host — preview runs in the `jekyll/jekyll:4.2.2`
Docker image (already present locally; Docker Hub login is expired, so don't expect to
pull new images).

```bash
docker run -d --name tm-jekyll -p 4000:4000 \
  -v "D:\home\ignat\project-third-matter\git\exopoiesis.github.io:/srv/jekyll" \
  jekyll/jekyll:4.2.2 \
  sh -c "gem install webrick --no-document && jekyll serve --host 0.0.0.0 --watch --force_polling"
```

Then open <http://localhost:4000/en/blog/> (or `/ru/`, `/zh/`). Stop with
`docker rm -f tm-jekyll`.

Gotchas (learned the hard way):
- **Do NOT add a `Gemfile`.** A Gemfile triggers the image's `bundle install` wrapper,
  which runs `chown -R /usr/gem` — on Docker Desktop/WSL2 that hangs for many minutes.
  The image already bundles `jekyll-sitemap` and `jekyll-seo-tag`; install only `webrick`
  (Ruby 3 dropped it from stdlib, and `jekyll serve` needs it) with plain `gem install`.
- `--force_polling` is required on a Windows bind-mount, otherwise `--watch` misses edits.
- Publish the port with `-p 4000:4000` (the sibling `arxiv-jekyll` container omits it and is
  therefore not reachable in a browser).

## Related repositories

- [sulfide-proton-barriers](https://github.com/exopoiesis/sulfide-proton-barriers) — NEB/MD calculations of proton diffusion in iron sulfide minerals

## AI Collaboration Disclosure

This project is developed through human–AI collaboration using Claude (Anthropic). Site content, design, and code were co-created with Claude Code.

## License

Code: MIT. Content: CC-BY-4.0.

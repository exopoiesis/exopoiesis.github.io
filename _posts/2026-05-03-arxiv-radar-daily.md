---
layout: post
title: "arXiv Radar — daily feeds that watch the literature"
date: 2026-05-03
lang: en
ref: arxiv-radar-daily
categories: [en]
description: "We opened arXiv Radar: a set of curated, self-updating arXiv feeds with a strong relevance filter — for chemistry, physics, electrochemistry, chemical engineering, and polymers."
---

A single independent researcher can't read arXiv by hand across a fast-moving, cross-disciplinary field. So we built **arXiv Radar** — curated feeds that scan arXiv every day and keep only what's relevant. Today we're opening the first layer: five public, self-updating feeds.

- [**Chemistry**](https://exopoiesis.space/arxiv-radar-chemistry/)
- [**Physics**](https://exopoiesis.space/arxiv-radar-physics/)
- [**Electrochemistry & Mineral Surfaces**](https://exopoiesis.space/arxiv-radar-electrochemistry/)
- [**Chemical Engineering**](https://exopoiesis.space/arxiv-radar-chem-eng/)
- [**Polymers**](https://exopoiesis.space/arxiv-radar-polymer/)

**The point is the filter, not the firehose.** Each feed runs a curated set of per-topic queries that are deliberately *narrow* — with AND-conditions — so a greedy keyword (a generic "battery" or generic-ML paper) can't flood the feed with noise. What survives is sorted into named topic buckets: for the electrochemistry feed, for example, CO₂ reduction, sulfide electrocatalysts, mineral–water interfaces, ion transport and gradients, and prebiotic mineral catalysis.

On top of keywords, each feed carries **author whitelists** — a set of researchers we follow by name, so their new work surfaces even when the abstract doesn't trip a keyword. Everything is tagged, and the [GitHub Pages](https://exopoiesis.space/arxiv-radar-electrochemistry/) site lets you filter by **date** or **tag** and browse the full feed — a rolling two-year window, with older work rotating out so it always reflects the current literature.

It all refreshes automatically every day (GitHub Actions), with monthly archives keeping the history. These daily feeds are the public face of a larger reading system — more on that soon.

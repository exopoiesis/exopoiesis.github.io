---
layout: post
title: "Our reading system: corpus-core + two MCP servers"
date: 2026-05-17
lang: en
ref: corpus-mcp
categories: [en]
description: "Three new open-source repos — corpus-core, arxiv-radar-mcp, lab-corpus-mcp — that let an AI assistant search, fetch, and read the literature with us through the Model Context Protocol."
---

In the [daily-feeds post]({% post_url 2026-05-03-arxiv-radar-daily %}) we called those feeds "the public face of a larger reading system." Here it is — three new open-source repositories that let an AI assistant actually *read* alongside us, over the [Model Context Protocol](https://modelcontextprotocol.io) (MCP).

**[corpus-core](https://github.com/exopoiesis/corpus-core)** — the shared engine. Embeddings for semantic search, plain text search, a section-aware chunker, a job registry, throttled fetching, and a generic MCP-server scaffold. It carries no project-specific logic; the two servers below are both built on it.

**[arxiv-radar-mcp](https://github.com/exopoiesis/arxiv-radar-mcp)** — a local MCP server over the daily arXiv feeds. Search the abstracts — semantically or by text, across science domains — and when a paper looks promising, **pull its full text on demand**: the server fetches and indexes it, so you can then search *inside* it ("found in the Methods of paper X"). Abstracts stay in memory; full texts are added to the corpus only when you ask.

**[lab-corpus-mcp](https://github.com/exopoiesis/lab-corpus-mcp)** — the broader research workspace. It ingests *any* literature, not just arXiv — PDFs and presentation slides — parsed with MinerU and made searchable through the same embedding stack. Lecture videos and slide decks are on the roadmap.

All three were born for our own needs: keeping one independent researcher (and an AI partner) on top of a fast-moving, cross-disciplinary literature. We use them every day, keep improving them, and we're sharing the whole stack with the community. **Open source (MIT) — and we're open to collaboration.**

[corpus-core](https://github.com/exopoiesis/corpus-core) · [arxiv-radar-mcp](https://github.com/exopoiesis/arxiv-radar-mcp) · [lab-corpus-mcp](https://github.com/exopoiesis/lab-corpus-mcp)

---
layout: post
title: "Prodromos — a $0 pre-flight gate before expensive DFT"
date: 2026-06-01
lang: en
ref: prodromos
categories: [en]
description: "Prodromos runs cheap checks ahead of costly DFT saddle-point searches — catching the failure modes that otherwise burn GPU-days on a meaningless barrier. Built on TM-Spec, CLI + MCP."
---

*πρόδρομος — "the one who runs ahead."*

A DFT [nudged-elastic-band](https://en.wikipedia.org/wiki/Nudged_elastic_band) (NEB) or saddle-point search can cost days of GPU time and hundreds of dollars. And a dispiriting number of them are **doomed before they start.**

We learned the failure modes the expensive way:

- endpoints that quietly relax into the *same* basin, so the "barrier" is fiction;
- the **wrong structure** silently sitting on disk — a 44-hour run on a cell that had lost the very vacancy it was supposed to study;
- a migrating proton that lands on the **wrong host** mid-path, so the run measures a different mechanism than intended;
- endpoints sitting on two different **magnetic sheets**, making a single-path NEB ill-posed;
- foundation machine-learning geometries that look fine locally but carry tens of eV of hidden lattice error.

**[Prodromos](https://github.com/exopoiesis/prodromos)** is the answer: a **$0 pre-flight gate** that runs *ahead* of the costly calculation and reports whether the path is worth taking. It's an evidence ladder — cheapest test first, stop at the first hard diagnosis — and it is *not* a replacement for Quantum ESPRESSO / ABACUS / jDFTx, just a thin, cheap layer of checks *around* them.

It is built on **[TM-Spec]({% post_url 2026-05-10-tm-spec %})** — the "support layer" we said we were starting to build. A case *is* a TM-Spec document; Prodromos converts a raw QE/ABACUS input into one automatically, and pulls structures and magnetic ground states from OPTIMADE / NOMAD / Materials Project / MAGNDATA to cross-check before a single GPU is touched.

It ships as a CLI **and** an MCP server, so an AI assistant can call each gate directly and get back a structured verdict — **GO**, route to a cheaper test, or **NO-GO** with reasons and next actions. 544 tests; the search-method prototypes are validated on analytic potentials.

MIT-licensed, built for our own Fe–S campaigns and shared in the open.

[Prodromos on GitHub &rarr;](https://github.com/exopoiesis/prodromos)

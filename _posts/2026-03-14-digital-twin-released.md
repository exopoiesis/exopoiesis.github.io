---
layout: post
title: "The Digital Twin: 262,000 Simulations of Third Matter"
date: 2026-03-14
lang: en
ref: digital-twin
categories: [en]
description: "We completed ORACLE — a comprehensive computational exploration of the Third Matter parameter space using 262,000 Sobol-sampled Gillespie simulations."
---

After months of computational work, we have completed **ORACLE** — our global sensitivity analysis of the Third Matter system. The numbers tell a clear story.

## What we did

We sampled the 16-dimensional parameter space of our G3c membrane model using Sobol sequences, running 262,000 stochastic (Gillespie) simulations. A Random Forest classifier (AUC = 0.982) then mapped the boundary between "alive" and "dead" states.

## What we found

The system is **transport-limited, not reaction-limited**. The catalytic rate constant `k_cat` is completely decoupled — varying it over 7 orders of magnitude (10⁻⁸ to 10⁻¹) changes the steady-state formate concentration by less than 0.01 mM. The mackinawite layer thickness `L_mack` is the only real control knob:

- 20 nm → 0.9 mM formate
- 50 nm → 3.2 mM
- 100 nm → 6.5 mM

The three critical parameters are formate degradation rate (`kd_A`, importance 0.36), formate production rate (`k1`, 0.13), and membrane degradation rate (`kd_m`, 0.10). Six parameters have no detectable threshold at all.

## What this means

The membrane *is* the metabolism. Third Matter doesn't need a fast catalyst — it needs a good membrane. This simplifies the experimental design considerably: we can focus on mackinawite layer thickness and membrane stability rather than chasing catalytic efficiency.

The digital twin is complete. Now we build the real thing.

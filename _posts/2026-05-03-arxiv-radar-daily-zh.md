---
layout: post
title: "arXiv Radar——每日监看文献的信息流"
date: 2026-05-03
lang: zh
ref: arxiv-radar-daily
categories: [zh]
description: "我们上线了 arXiv Radar：一组人工策展、自动更新的 arXiv 信息流，配备强力的相关性过滤——涵盖化学、物理、电化学、化学工程与高分子。"
---

单枪匹马的独立研究者无法靠人工通读快速演进、跨学科的 arXiv。于是我们做了 **arXiv Radar**——每天扫描 arXiv、只保留相关内容的策展信息流。今天先开放第一层：五个公开、自动更新的信息流。

- [**化学**](https://exopoiesis.space/arxiv-radar-chemistry/)
- [**物理**](https://exopoiesis.space/arxiv-radar-physics/)
- [**电化学与矿物表面**](https://exopoiesis.space/arxiv-radar-electrochemistry/)
- [**化学工程**](https://exopoiesis.space/arxiv-radar-chem-eng/)
- [**高分子**](https://exopoiesis.space/arxiv-radar-polymer/)

**关键在于过滤，而非信息洪流。** 每个信息流都运行一组人工策展的分主题查询，刻意保持*狭窄*——并使用 AND 条件——以免某个贪婪的关键词（泛泛的"电池"论文或通用机器学习论文）把信息流淹没在噪声里。通过筛选的论文被归入命名主题：以电化学流为例，包括 CO₂ 还原、硫化物电催化剂、矿物–水界面、离子输运与梯度，以及前生命矿物催化。

在关键词之上，每个流还带有**作者白名单**——一组我们按姓名追踪的研究者，使他们的新作即便摘要未命中关键词也能浮现。所有内容均带标签，[GitHub Pages](https://exopoiesis.space/arxiv-radar-electrochemistry/) 站点支持按**日期**或**标签**筛选，并可浏览整个信息流——一个滚动的两年窗口，较旧的论文会轮替移出，因此始终反映当前的文献。

一切由 GitHub Actions 每日自动刷新，月度归档保存历史。这些每日信息流是一个更大阅读系统的公开门面——稍后详述。

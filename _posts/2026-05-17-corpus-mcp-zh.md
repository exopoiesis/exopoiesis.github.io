---
layout: post
title: "我们的阅读系统：corpus-core + 两个 MCP 服务器"
date: 2026-05-17
lang: zh
ref: corpus-mcp
categories: [zh]
description: "三个新的开源仓库——corpus-core、arxiv-radar-mcp、lab-corpus-mcp——让 AI 助手通过 Model Context Protocol 与我们一起检索、抓取和阅读文献。"
---

在[每日信息流那篇新闻]({% post_url 2026-05-03-arxiv-radar-daily-zh %})里，我们把这些信息流称为"一个更大阅读系统的公开门面"。它来了——三个新的开源仓库，让 AI 助手通过 [Model Context Protocol](https://modelcontextprotocol.io)（MCP）真正与我们一起*阅读*。

**[corpus-core](https://github.com/exopoiesis/corpus-core)** —— 共享引擎。用于语义搜索的向量嵌入、文本搜索、分节感知的切块器、任务注册表、限速抓取，以及一个通用的 MCP 服务器骨架。它不含任何项目专有逻辑；下面两个服务器都构建在它之上。

**[arxiv-radar-mcp](https://github.com/exopoiesis/arxiv-radar-mcp)** —— 架设在每日 arXiv 信息流之上的本地 MCP 服务器。可对摘要进行检索——按语义或按文本、跨多个学科领域——当某篇论文看起来有价值时，**按需抓取其全文**：服务器会下载并索引它，随后便可在论文*内部*检索（"在论文 X 的 Methods 中找到"）。摘要常驻内存；全文仅在你请求时才加入语料库。

**[lab-corpus-mcp](https://github.com/exopoiesis/lab-corpus-mcp)** —— 更广阔的研究工作空间。它可摄取*任何*文献，不仅是 arXiv——PDF 与演示幻灯片——经 MinerU 解析后，通过同一套嵌入栈进行检索。讲座视频与幻灯片已列入路线图。

这三者都源于我们自身的需求：让一位独立研究者（与一位 AI 伙伴）跟得上快速演进、跨学科的文献。我们每天都在使用、持续改进，并把整个技术栈分享给社区。**开源（MIT）——并欢迎合作。**

[corpus-core](https://github.com/exopoiesis/corpus-core) · [arxiv-radar-mcp](https://github.com/exopoiesis/arxiv-radar-mcp) · [lab-corpus-mcp](https://github.com/exopoiesis/lab-corpus-mcp)

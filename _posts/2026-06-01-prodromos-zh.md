---
layout: post
title: "Prodromos——昂贵 DFT 之前的 $0 预检门"
date: 2026-06-01
lang: zh
ref: prodromos
categories: [zh]
description: "Prodromos 在昂贵的 DFT 鞍点搜索之前先跑廉价检查——拦住那些否则会在无意义势垒上烧掉数日 GPU 的失败模式。构建于 TM-Spec 之上，CLI + MCP。"
---

*πρόδρομος——"跑在前面的人"。*

一次 DFT [微动弹性带](https://en.wikipedia.org/wiki/Nudged_elastic_band)（NEB）或鞍点搜索可能耗费数日 GPU 时间和数百美元。而其中令人沮丧的相当一部分，**在开始之前就注定失败。**

这些失败模式，我们都是付了昂贵学费才学会的：

- 路径两端悄悄弛豫进*同一个*势阱——于是"势垒"纯属虚构；
- **错误的结构**默默躺在磁盘上——一次 44 小时的计算，跑的却是丢掉了那个本该研究的空位的晶胞；
- 迁移的质子在中途落到了**错误的宿主**上——于是计算测的是另一个机制；
- 路径两端落在两个不同的**磁性片层**上——单路径 NEB 因此是病态的；
- 基础机器学习给出的几何，局部看起来没问题，却携带数十 eV 的隐藏晶格误差。

**[Prodromos](https://github.com/exopoiesis/prodromos)** 就是答案：一个 **$0 预检门**，跑在昂贵计算*之前*，告诉你这条路值不值得走。它是一架证据阶梯——最便宜的测试先行，遇到第一个硬性诊断即止——它*不是* Quantum ESPRESSO / ABACUS / jDFTx 的替代品，而是环绕它们的一层薄而廉价的检查。

它构建于 **[TM-Spec]({% post_url 2026-05-10-tm-spec-zh %})** 之上——正是我们说过要开始搭建的那层"支撑层"。一个案例*本身*就是一份 TM-Spec 文档；Prodromos 会自动把原始的 QE/ABACUS 输入转换成它，并从 OPTIMADE / NOMAD / Materials Project / MAGNDATA 拉取结构与磁性基态进行交叉核对——在动用任何一块 GPU 之前。

它既是 CLI **也是** MCP 服务器，因此 AI 助手可以直接调用每个门控并取回结构化裁定——**GO**、转去更便宜的测试，或带原因与后续步骤的 **NO-GO**。544 项测试；搜索方法的原型在解析势上得到验证。

MIT 许可证，为我们自己的 Fe–S 计算而生，并向社区开放。

[在 GitHub 上查看 Prodromos &rarr;](https://github.com/exopoiesis/prodromos)

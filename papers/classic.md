# 📚 经典论文完整清单

> LLM 领域奠基性工作，按主题分类 · 共 35 篇必读

**最后更新**: 2026-03-25 | **总数**: 35 篇

---

## 🏆 Transformer 架构 (2017-2020)

> Transformer 是 LLM 的基石，建议优先阅读

| # | 论文 | 年份 | 机构 | 引用 | 链接 | 必读理由 |
|---|------|------|------|------|------|----------|
| 1 | **Attention Is All You Need** | 2017 | Google | 100k+ | [📄 arXiv:1706.03762](https://arxiv.org/abs/1706.03762) | Transformer 开山之作，必须精读 |
| 2 | **BERT** | 2018 | Google | 70k+ | [📄 arXiv:1810.04805](https://arxiv.org/abs/1810.04805) | 双向编码器，NLP 里程碑 |
| 3 | **GPT-2** | 2019 | OpenAI | 20k+ | [📄 arXiv:1906.03762](https://arxiv.org/abs/1906.03762) | 纯解码器架构，零样本学习 |
| 4 | **T5** | 2019 | Google | 15k+ | [📄 arXiv:1910.10683](https://arxiv.org/abs/1910.10683) | 统一文本到文本框架 |
| 5 | **GPT-3** | 2020 | OpenAI | 50k+ | [📄 arXiv:2005.14165](https://arxiv.org/abs/2005.14165) | 175B 参数，涌现能力 |
| 6 | **Scaling Laws** | 2020 | OpenAI | 10k+ | [📄 arXiv:2001.08361](https://arxiv.org/abs/2001.08361) | 大模型训练指导原则 |

---

## ⚡ 高效训练与微调 (2021-2023)

> 让大模型训练更经济、更高效

| # | 论文 | 年份 | 机构 | 引用 | 链接 | 核心价值 |
|---|------|------|------|------|------|----------|
| 7 | **LoRA** | 2021 | Microsoft | 15k+ | [📄 arXiv:2106.09685](https://arxiv.org/abs/2106.09685) | 低秩适配，微调标配 |
| 8 | **Prefix Tuning** | 2021 | Stanford | 3k+ | [📄 arXiv:2101.00190](https://arxiv.org/abs/2101.00190) | 连续前缀优化 |
| 9 | **P-Tuning** | 2021 | Tsinghua | 2k+ | [📄 arXiv:2103.10385](https://arxiv.org/abs/2103.10385) | 离散 prompt 优化 |
| 10 | **QLoRA** | 2023 | UW | 8k+ | [📄 arXiv:2305.14314](https://arxiv.org/abs/2305.14314) | 4bit 量化微调 |
| 11 | **AdaLoRA** | 2023 | Microsoft | 1k+ | [📄 arXiv:2303.10512](https://arxiv.org/abs/2303.10512) | 自适应秩分配 |

---

## 🎯 对齐与指令微调 (2022-2023)

> 让模型更安全、更有用

| # | 论文 | 年份 | 机构 | 引用 | 链接 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 12 | **InstructGPT** | 2022 | OpenAI | 20k+ | [📄 arXiv:2203.02155](https://arxiv.org/abs/2203.02155) | RLHF 对齐方法详解 |
| 13 | **RLHF Survey** | 2022 | Various | 2k+ | [📄 arXiv:2212.05368](https://arxiv.org/abs/2212.05368) | 全面综述 |
| 14 | **DPO** | 2023 | Stanford | 8k+ | [📄 arXiv:2305.18290](https://arxiv.org/abs/2305.18290) | 直接偏好优化，RLHF 替代 |
| 15 | **Constitutional AI** | 2022 | Anthropic | 5k+ | [📄 arXiv:2212.08073](https://arxiv.org/abs/2212.08073) | 自监督对齐 |
| 16 | **HHH** | 2021 | DeepMind | 3k+ | [📄 arXiv:2112.00861](https://arxiv.org/abs/2112.00861) | Helpful, Honest, Harmless |

---

## 🧠 推理与能力扩展 (2022-2023)

> 让模型更聪明、更能推理

| # | 论文 | 年份 | 机构 | 引用 | 链接 | 关键突破 |
|---|------|------|------|------|------|----------|
| 17 | **Chain-of-Thought** | 2022 | Google | 12k+ | [📄 arXiv:2201.11903](https://arxiv.org/abs/2201.11903) | 思维链推理开创 |
| 18 | **Self-Consistency** | 2022 | Google | 5k+ | [📄 arXiv:2203.11171](https://arxiv.org/abs/2203.11171) | 多路径推理投票 |
| 19 | **ReAct** | 2022 | Princeton | 6k+ | [📄 arXiv:2210.03629](https://arxiv.org/abs/2210.03629) | 推理 + 行动框架 |
| 20 | **Toolformer** | 2023 | Meta | 4k+ | [📄 arXiv:2302.04761](https://arxiv.org/abs/2302.04761) | 自主工具使用 |
| 21 | **Tree of Thoughts** | 2023 | Princeton | 4k+ | [📄 arXiv:2305.10601](https://arxiv.org/abs/2305.10601) | 树状思维搜索 |

---

## 🏗️ 架构优化 (2021-2023)

> 让模型更快、更长、更强

| # | 论文 | 年份 | 机构 | 引用 | 链接 | 优化方向 |
|---|------|------|------|------|------|----------|
| 22 | **RoPE** | 2021 | Meta | 8k+ | [📄 arXiv:2104.09864](https://arxiv.org/abs/2104.09864) | 旋转位置编码 |
| 23 | **ALiBi** | 2021 | AI2 | 3k+ | [📄 arXiv:2108.12409](https://arxiv.org/abs/2108.12409) | 外推位置编码 |
| 24 | **FlashAttention** | 2022 | Princeton | 10k+ | [📄 arXiv:2205.14135](https://arxiv.org/abs/2205.14135) | IO 感知注意力加速 |
| 25 | **FlashAttention-2** | 2023 | Princeton | 3k+ | [📄 arXiv:2307.08691](https://arxiv.org/abs/2307.08691) | 进一步优化 |
| 26 | **MoE** | 2021 | Google | 5k+ | [📄 arXiv:2101.03961](https://arxiv.org/abs/2101.03961) | 稀疏专家混合 |
| 27 | **Switch Transformer** | 2021 | Google | 4k+ | [📄 arXiv:2101.03961](https://arxiv.org/abs/2101.03961) | 万亿参数模型 |

---

## 🔍 检索与知识增强 (2020-2023)

> 让模型更有知识、更准确

| # | 论文 | 年份 | 机构 | 引用 | 链接 | 核心思路 |
|---|------|------|------|------|------|----------|
| 28 | **RAG** | 2020 | Meta | 8k+ | [📄 arXiv:2005.11401](https://arxiv.org/abs/2005.11401) | 检索增强生成 |
| 29 | **RETRO** | 2021 | DeepMind | 2k+ | [📄 arXiv:2112.04426](https://arxiv.org/abs/2112.04426) | 检索式预训练 |
| 30 | **REALM** | 2020 | Google | 3k+ | [📄 arXiv:2002.08909](https://arxiv.org/abs/2002.08909) | 知识增强预训练 |
| 31 | **DPR** | 2020 | Meta | 5k+ | [📄 arXiv:2004.04906](https://arxiv.org/abs/2004.04906) | 稠密段落检索 |

---

## 🌟 开源模型里程碑 (2023-2024)

> 推动开源生态发展的关键工作

| # | 论文/报告 | 年份 | 机构 | 引用 | 链接 | 意义 |
|---|----------|------|------|------|------|------|
| 32 | **LLaMA** | 2023 | Meta | 15k+ | [📄 arXiv:2302.13971](https://arxiv.org/abs/2302.13971) | 开源模型起点 |
| 33 | **LLaMA 2** | 2023 | Meta | 10k+ | [📄 arXiv:2307.09288](https://arxiv.org/abs/2307.09288) | 可商用开源 |
| 34 | **Mistral** | 2023 | Mistral AI | 5k+ | [📄 arXiv:2310.06825](https://arxiv.org/abs/2310.06825) | 小尺寸高性能 |
| 35 | **Qwen** | 2023 | Alibaba | 3k+ | [📄 arXiv:2309.16609](https://arxiv.org/abs/2309.16609) | 中文能力突出 |

---

## 📖 阅读建议

### 入门路线 (必读 10 篇)
```
1. Attention Is All You Need → 理解基础架构
2. BERT / GPT-3 → 理解预训练范式
3. LoRA → 掌握微调方法
4. InstructGPT → 理解对齐
5. Chain-of-Thought → 理解推理
6. FlashAttention → 理解优化
7. RAG → 理解知识增强
8. LLaMA → 了解开源生态
```

### 进阶路线 (选读 15 篇)
根据研究方向选择对应分类深入阅读

### 研究路线 (全读 35 篇)
全面掌握领域发展脉络

---

## 🔗 相关资源

- [Papers With Code](https://paperswithcode.com) - 论文与代码实现
- [HuggingFace](https://huggingface.co/papers) - 每日论文推荐
- [arXiv Sanity](http://arxiv-sanity-lite.com) - 论文检索
- [Connected Papers](https://connectedpapers.com) - 论文关系图

---

<div align="center">

**💡 提示**: 论文引用数据来自 Google Scholar，截至 2026-03

[← 返回主页](../README.md)

</div>

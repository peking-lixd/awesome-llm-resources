# 🚀 Awesome LLM Resources

<div align="center">

![License](https://img.shields.io/badge/License-MIT-green.svg)
![Update](https://img.shields.io/badge/update-weekly-blue)
![Stars](https://img.shields.io/github/stars/peking-lixd/awesome-llm-resources?color=yellow)
![Issues](https://img.shields.io/github/issues/peking-lixd/awesome-llm-resources?color=red)

**大语言模型领域最全面的资源指南**

📚 经典论文 · 🔥 前沿研究 · 🛠️ 开源项目 · 📖 学习路线

[快速开始](#-快速开始) · [经典论文](#-经典论文必读) · [热门前沿](#-热门前沿) · [开源项目](#-开源项目) · [学习路线](#-学习路线)

</div>

---

## 📌 关于本项目

> **目标**：帮助研究者和开发者快速掌握 LLM 核心技术，少走弯路。
>
> **原则**：只收录精品 · 持续更新 · 高度 curated

这是一个**精心策划**的 LLM 资源清单，涵盖：
- 📚 **经典论文** — 奠基性工作，必读清单
- 🔥 **热门前沿** — 最新突破，每周更新
- 🛠️ **开源项目** — 实用工具、框架、应用
- 📖 **学习路线** — 从入门到精通

---

## 🎯 快速开始

### 如果你是...

| 角色 | 建议路径 | 预计时间 |
|------|----------|----------|
| **初学者** | [学习路线](#-学习路线) → [经典论文](#-经典论文必读) | 4-6 周 |
| **研究者** | [经典论文](#-经典论文必读) → [热门前沿](#-热门前沿) | 2-3 周 |
| **工程师** | [开源项目](#-开源项目) → [实践指南](./projects/README.md) | 1-2 周 |
| **产品经理** | [应用案例](./projects/applications.md) → [技术概览](#-核心概念) | 1 周 |

---

## 📚 经典论文必读

> 按重要性分级，建议按顺序阅读

### 🏆 基石级 (必读 Top 10)

| # | 论文 | 年份 | 引用 | 核心价值 |
|---|------|------|------|----------|
| 1 | **[Attention Is All You Need](https://arxiv.org/abs/1706.03762)** | 2017 | 100k+ | Transformer 开山之作 |
| 2 | **[BERT](https://arxiv.org/abs/1810.04805)** | 2018 | 70k+ | 预训练语言模型里程碑 |
| 3 | **[GPT-3](https://arxiv.org/abs/2005.14165)** | 2020 | 50k+ | 大模型涌现能力 |
| 4 | **[InstructGPT](https://arxiv.org/abs/2203.02155)** | 2022 | 20k+ | RLHF 对齐方法 |
| 5 | **[LLaMA](https://arxiv.org/abs/2302.13971)** | 2023 | 15k+ | 开源模型里程碑 |
| 6 | **[LoRA](https://arxiv.org/abs/2106.09685)** | 2021 | 15k+ | 高效微调标配 |
| 7 | **[Chain-of-Thought](https://arxiv.org/abs/2201.11903)** | 2022 | 12k+ | 思维链推理 |
| 8 | **[FlashAttention](https://arxiv.org/abs/2205.14135)** | 2022 | 10k+ | 注意力加速 |
| 9 | **[DPO](https://arxiv.org/abs/2305.18290)** | 2023 | 8k+ | RLHF 替代方案 |
| 10 | **[RAG](https://arxiv.org/abs/2005.11401)** | 2020 | 8k+ | 检索增强生成 |

### 📖 完整分类清单

| 类别 | 论文数 | 链接 |
|------|--------|------|
| Transformer 架构 | 6 | [papers/classic.md#transformer](papers/classic.md) |
| 高效微调 | 5 | [papers/classic.md#efficient](papers/classic.md) |
| 对齐与安全 | 5 | [papers/classic.md#alignment](papers/classic.md) |
| 推理能力 | 5 | [papers/classic.md#reasoning](papers/classic.md) |
| 架构优化 | 5 | [papers/classic.md#architecture](papers/classic.md) |
| 开源模型 | 4 | [papers/classic.md#open-source](papers/classic.md) |

📌 **完整 30+ 篇经典论文** → [papers/classic.md](papers/classic.md)

---

## 🔥 热门前沿

### 本周最受关注 (2026-W13)

| 论文 | 机构 | 亮点 | arXiv |
|------|------|------|-------|
| **Mamba-2** | CMU | 状态空间模型新突破 | [2405.xxxx](https://arxiv.org) |
| **GPT-4o Technical Report** | OpenAI | 多模态实时交互 | [2405.xxxx](https://arxiv.org) |
| **Claude 3.5 System Card** | Anthropic | 推理能力大幅提升 | [2406.xxxx](https://arxiv.org) |
| **Llama 3.1** | Meta | 405B 开源最强 | [2407.xxxx](https://arxiv.org) |
| **Gemini 1.5 Pro** | Google | 百万 token 上下文 | [2403.xxxx](https://arxiv.org) |

📌 **本周完整榜单** → [papers/hot_this_week.md](papers/hot_this_week.md)

### 本月趋势

- 📈 **长上下文** - 百万 token 处理成为新标配
- 📈 **多模态** - 图文音视频统一理解
- 📈 **Agent** - 自主规划与工具使用
- 📈 **小模型** - 端侧部署效率优化

📌 **本月完整榜单** → [papers/hot_this_month.md](papers/hot_this_month.md)

---

## 🛠️ 开源项目

### 🔧 开发框架

| 项目 | Stars | 简介 | 链接 |
|------|-------|------|------|
| **LangChain** | 100k+ | LLM 应用开发框架 | [GitHub](https://github.com/langchain-ai/langchain) |
| **LlamaIndex** | 30k+ | 数据索引与检索 | [GitHub](https://github.com/run-llama/llama_index) |
| **Haystack** | 15k+ | 生产级 RAG 框架 | [GitHub](https://github.com/deepset-ai/haystack) |
| **vLLM** | 50k+ | 高吞吐推理引擎 | [GitHub](https://github.com/vllm-project/vllm) |

### 🎯 微调工具

| 项目 | Stars | 简介 | 链接 |
|------|-------|------|------|
| **PEFT** | 20k+ | 参数高效微调库 | [GitHub](https://github.com/huggingface/peft) |
| **LLaMA-Factory** | 15k+ | 一站式微调平台 | [GitHub](https://github.com/hiyouga/LLaMA-Factory) |
| **Axolotl** | 10k+ | 分布式微调框架 | [GitHub](https://github.com/OpenAccess-AI-Collective/axolotl) |

### 🚀 部署方案

| 项目 | Stars | 简介 | 链接 |
|------|-------|------|------|
| **Ollama** | 80k+ | 本地模型运行 | [GitHub](https://github.com/ollama/ollama) |
| **LM Studio** | - | 桌面端推理 GUI | [官网](https://lmstudio.ai) |
| **Text Generation Inference** | 5k+ | HuggingFace 推理服务 | [GitHub](https://github.com/huggingface/text-generation-inference) |

📌 **完整项目列表** → [projects/README.md](projects/README.md)

---

## 📖 学习路线

### 阶段 1: 基础入门 (2 周)

```
Week 1: Transformer 基础
├── Attention Is All You Need (必读)
├── 理解 Self-Attention 机制
└── 动手实现 Transformer

Week 2: 预训练语言模型
├── BERT / GPT 系列论文
├── 理解预训练 + 微调范式
└── 使用 HuggingFace Transformers
```

### 阶段 2: 进阶提升 (3 周)

```
Week 3: 大模型基础
├── GPT-3 / Scaling Laws
├── 理解涌现能力
└── Prompt Engineering

Week 4: 高效微调
├── LoRA / QLoRA
├── 实践微调流程
└── 资源优化技巧

Week 5: 对齐技术
├── InstructGPT / RLHF
├── DPO 等新方法
└── 安全对齐
```

### 阶段 3: 专业深入 (3 周)

```
Week 6: 推理与 Agent
├── Chain-of-Thought
├── ReAct / Tool Use
└── Agent 系统设计

Week 7: 架构优化
├── FlashAttention / RoPE
├── 长上下文处理
└── 推理加速

Week 8: 前沿探索
├── 跟踪最新论文
├── 参与开源项目
└── 实践个人项目
```

📌 **详细学习资源** → [learning/roadmap.md](learning/roadmap.md)

---

## 📊 统计

| 类别 | 数量 | 最后更新 |
|------|------|----------|
| 经典论文 | 30+ | 2026-03-25 |
| 本周热门 | 10 | 2026-03-25 |
| 本月热门 | 20 | 2026-03-25 |
| 开源项目 | 50+ | 2026-03-25 |
| 学习资源 | 100+ | 2026-03-25 |

---

## 🤝 贡献

欢迎推荐优质资源！提交 PR 时请确保：

- ✅ 是真正值得关注的精品
- ✅ 提供简要说明和链接
- ✅ 正确分类到对应目录
- ✅ 遵循 [贡献指南](CONTRIBUTING.md)

### 贡献者

<!-- 这里会自动显示贡献者头像 -->
<a href="https://github.com/peking-lixd/awesome-llm-resources/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=peking-lixd/awesome-llm-resources" />
</a>

---

## 📅 更新计划

| 内容 | 频率 | 时间 |
|------|------|------|
| 本周热门 | 每周 | 周一 9:00 |
| 本月热门 | 每月 | 1 日 9:00 |
| 开源项目 | 每周 | 周三 9:00 |
| 经典论文 | 每月 | 15 日审核 |

---

## 🔗 相关资源

- [HuggingFace](https://huggingface.co) - 模型与数据集
- [Papers With Code](https://paperswithcode.com) - 论文与代码
- [arXiv](https://arxiv.org) - 最新论文
- [AI Twitter](https://twitter.com) - 社区动态

---

## 📄 许可证

MIT License © 2026 [peking-lixd](https://github.com/peking-lixd)

---

<div align="center">

### ⭐ 如果这个项目对你有帮助，请给个 Star！

[📬 问题反馈](https://github.com/peking-lixd/awesome-llm-resources/issues) · 
[🔄 提交 PR](https://github.com/peking-lixd/awesome-llm-resources/pulls) · 
[📧 联系作者](mailto:lixd@pku.edu.cn)

**🌟 Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=peking-lixd/awesome-llm-resources&type=Date)](https://star-history.com/#peking-lixd/awesome-llm-resources&Date)

</div>

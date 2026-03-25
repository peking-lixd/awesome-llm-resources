# 📖 LLM 学习路线

> 从入门到精通的系统学习路径 · 预计 8-12 周

**最后更新**: 2026-03-25 | **难度**: 初级 → 高级

---

## 🗺️ 学习地图

```
┌─────────────────────────────────────────────────────────────────┐
│                      LLM 学习路线 (8-12 周)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  阶段 1: 基础入门 (2 周)                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ Transformer │ →│ 预训练模型  │ →│  动手实践   │              │
│  │   基础      │  │   理解      │  │  HuggingFace│              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                 │
│  阶段 2: 进阶提升 (3 周)                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   大模型    │ →│  高效微调   │ →│  对齐技术   │              │
│  │   原理      │  │  LoRA/QLoRA │  │  RLHF/DPO   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                 │
│  阶段 3: 专业深入 (3 周)                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  推理优化   │ →│  Agent 系统  │ →│  实战项目   │              │
│  │  架构优化   │  │  工具使用   │  │  完整应用   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                 │
│  阶段 4: 前沿探索 (2-4 周)                                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  最新论文   │ →│  开源贡献   │ →│  个人项目   │              │
│  │  跟踪学习   │  │  社区参与   │  │  创新实践   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 阶段 1: 基础入门 (2 周)

### Week 1: Transformer 基础

**学习目标**: 理解 Transformer 架构核心原理

#### 📖 必读论文
- [ ] **Attention Is All You Need** (2017) - [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
  - 重点：Self-Attention 机制、Positional Encoding
  - 时间：2-3 小时精读

#### 🎥 视频课程
- [ ] [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) - 图文讲解
- [ ] [Stanford CS224N](https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ) - Lecture 5-7

#### 💻 实践任务
- [ ] 用 PyTorch 实现 Self-Attention
- [ ] 用 PyTorch 实现完整 Transformer
- [ ] 在小型数据集上训练

#### 📝 代码资源
```python
# 推荐实现顺序
1. Multi-Head Attention
2. Positional Encoding
3. Encoder Layer
4. Decoder Layer
5. Complete Transformer
```

**参考实现**:
- [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)
- [HuggingFace Course](https://huggingface.co/course)

---

### Week 2: 预训练语言模型

**学习目标**: 理解 BERT、GPT 等预训练模型

#### 📖 必读论文
- [ ] **BERT** (2018) - [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)
  - 重点：Masked LM、Next Sentence Prediction
- [ ] **GPT-3** (2020) - [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
  - 重点：Decoder-only 架构、Few-shot Learning

#### 🎥 视频课程
- [ ] [HuggingFace NLP Course](https://huggingface.co/learn/nlp-course)
- [ ] [Jay Alammar - BERT](http://jalammar.github.io/illustrated-bert/)

#### 💻 实践任务
- [ ] 使用 HuggingFace Transformers 加载 BERT
- [ ] 使用 BERT 进行文本分类
- [ ] 使用 GPT-2 进行文本生成
- [ ] 理解 Tokenizer 工作原理

#### 🛠️ 工具掌握
```bash
# 必须掌握的库
- transformers (HuggingFace)
- datasets (HuggingFace)
- tokenizers
- accelerate
```

---

## 🚀 阶段 2: 进阶提升 (3 周)

### Week 3: 大模型原理

**学习目标**: 理解大模型的核心特性

#### 📖 必读论文
- [ ] **Scaling Laws** (2020) - [arXiv:2001.08361](https://arxiv.org/abs/2001.08361)
- [ ] **Emergent Abilities** (2022) - [arXiv:2206.07682](https://arxiv.org/abs/2206.07682)
- [ ] **LLaMA** (2023) - [arXiv:2302.13971](https://arxiv.org/abs/2302.13971)

#### 📚 核心概念
- [ ] 涌现能力 (Emergent Abilities)
- [ ] 缩放定律 (Scaling Laws)
- [ ] In-Context Learning
- [ ] Zero-shot / Few-shot Learning

#### 💻 实践任务
- [ ] 本地运行 LLaMA 模型 (使用 Ollama)
- [ ] 测试不同 size 模型的能力差异
- [ ] 实验不同的 Prompt 策略

---

### Week 4: 高效微调

**学习目标**: 掌握 LoRA、QLoRA 等微调技术

#### 📖 必读论文
- [ ] **LoRA** (2021) - [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
- [ ] **QLoRA** (2023) - [arXiv:2305.14314](https://arxiv.org/abs/2305.14314)
- [ ] **Prefix Tuning** (2021) - [arXiv:2101.00190](https://arxiv.org/abs/2101.00190)

#### 🛠️ 工具掌握
- [ ] **PEFT** - HuggingFace 参数高效微调库
- [ ] **LLaMA-Factory** - 一站式微调平台
- [ ] **Unsloth** - 加速微调

#### 💻 实践任务
- [ ] 使用 LoRA 微调 LLaMA
- [ ] 使用 QLoRA 在单卡上微调 7B 模型
- [ ] 对比全量微调 vs LoRA 的效果

#### 📝 实践指南
```bash
# 使用 LLaMA-Factory 微调
git clone https://github.com/hiyouga/LLaMA-Factory
cd LLaMA-Factory
# 修改配置文件，启动训练
```

---

### Week 5: 对齐技术

**学习目标**: 理解 RLHF、DPO 等对齐方法

#### 📖 必读论文
- [ ] **InstructGPT** (2022) - [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)
- [ ] **DPO** (2023) - [arXiv:2305.18290](https://arxiv.org/abs/2305.18290)
- [ ] **Constitutional AI** (2022) - [arXiv:2212.08073](https://arxiv.org/abs/2212.08073)

#### 📚 核心概念
- [ ] RLHF (Reinforcement Learning from Human Feedback)
- [ ] PPO (Proximal Policy Optimization)
- [ ] DPO (Direct Preference Optimization)
- [ ] Safety Alignment

#### 💻 实践任务
- [ ] 使用 TRL 库进行 RLHF 实验
- [ ] 使用 DPO 进行偏好优化
- [ ] 构建简单的偏好数据集

---

## 🎯 阶段 3: 专业深入 (3 周)

### Week 6: 推理优化

**学习目标**: 掌握模型推理加速技术

#### 📖 必读论文
- [ ] **FlashAttention** (2022) - [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)
- [ ] **vLLM** (2023) - [arXiv:2309.06180](https://arxiv.org/abs/2309.06180)
- [ ] **RoPE** (2021) - [arXiv:2104.09864](https://arxiv.org/abs/2104.09864)

#### 🛠️ 工具掌握
- [ ] **vLLM** - 高吞吐推理引擎
- [ ] **TensorRT-LLM** - NVIDIA 加速
- [ ] **llama.cpp** - CPU 推理

#### 💻 实践任务
- [ ] 使用 vLLM 部署模型
- [ ] 对比不同推理引擎的性能
- [ ] 实验量化 (INT8/INT4)

---

### Week 7: Agent 系统

**学习目标**: 构建自主智能体

#### 📖 必读论文
- [ ] **Chain-of-Thought** (2022) - [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- [ ] **ReAct** (2022) - [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- [ ] **Toolformer** (2023) - [arXiv:2302.04761](https://arxiv.org/abs/2302.04761)

#### 🛠️ 工具掌握
- [ ] **LangChain** - 应用开发框架
- [ ] **AutoGen** - 多 Agent 框架
- [ ] **CrewAI** - Agent 协作

#### 💻 实践任务
- [ ] 构建一个简单的 Agent
- [ ] 实现工具调用功能
- [ ] 创建多 Agent 协作系统

---

### Week 8: 实战项目

**学习目标**: 完成一个完整的 LLM 应用

#### 🎯 项目选题 (选一个)
- [ ] **RAG 问答系统** - 基于文档的智能问答
- [ ] **代码助手** - 代码生成与解释
- [ ] **数据分析 Agent** - 自动数据分析
- [ ] **客服机器人** - 多轮对话系统

#### 📋 项目要求
- [ ] 完整的需求分析
- [ ] 技术选型与架构设计
- [ ] 实现与测试
- [ ] 性能优化
- [ ] 文档编写

#### 📝 项目模板
```
project/
├── README.md          # 项目说明
├── requirements.txt   # 依赖
├── src/              # 源代码
├── tests/            # 测试
├── data/             # 数据
└── docs/             # 文档
```

---

## 🔬 阶段 4: 前沿探索 (2-4 周)

### Week 9-10: 论文跟踪

**学习目标**: 跟踪最新研究进展

#### 📚 每日习惯
- [ ] 浏览 [arXiv CS.CL](https://arxiv.org/list/cs.CL/recent)
- [ ] 关注 [HuggingFace Daily Papers](https://huggingface.co/papers)
- [ ] 阅读 [Papers With Code](https://paperswithcode.com)

#### 📝 论文笔记模板
```markdown
## 论文标题
- 链接：arXiv:xxxx.xxxxx
- 机构：xxx
- 日期：2026-xx-xx

### 核心贡献
1. ...
2. ...

### 关键方法
- ...

### 实验结果
- ...

### 我的思考
- 创新点：...
- 局限性：...
- 可借鉴：...
```

---

### Week 11-12: 开源贡献

**学习目标**: 参与开源社区

#### 🎯 贡献方式
- [ ] 修复 Bug
- [ ] 添加功能
- [ ] 改进文档
- [ ] 翻译本地化

#### 📝 推荐项目
- **LangChain** - 文档完善、Issue 友好
- **LLaMA-Factory** - 中文社区活跃
- **HuggingFace** - 生态系统完善

#### 💡 贡献流程
```
1. Fork 项目
2. 创建分支
3. 修改代码
4. 提交 PR
5. 参与 Review
```

---

## 📚 学习资源汇总

### 🎥 视频课程
| 课程 | 平台 | 难度 | 链接 |
|------|------|------|------|
| CS224N | Stanford | 中级 | [YouTube](https://youtube.com) |
| CS324 | Stanford | 高级 | [官网](https://stanford-cs324.github.io) |
| HuggingFace | HF | 初级 | [课程](https://huggingface.co/learn) |
| LLM University | Cohere | 中级 | [课程](https://llm.university) |

### 📖 书籍推荐
- 《Transformers for NLP》- 入门经典
- 《Deep Learning》- 基础理论
- 《Speech and Language Processing》- 全面教材

### 🌐 社区资源
- [HuggingFace Discord](https://discord.gg/huggingface)
- [LangChain Discord](https://discord.gg/langchain)
- [Reddit r/MachineLearning](https://reddit.com/r/MachineLearning)
- [Twitter AI Community](https://twitter.com)

---

## ✅ 学习检查清单

### 阶段 1 检查点
- [ ] 能解释 Self-Attention 原理
- [ ] 能实现 Transformer
- [ ] 能使用 HuggingFace Transformers

### 阶段 2 检查点
- [ ] 理解 Scaling Laws
- [ ] 能用 LoRA 微调模型
- [ ] 理解 RLHF/DPO 原理

### 阶段 3 检查点
- [ ] 能部署推理服务
- [ ] 能构建 Agent 系统
- [ ] 完成一个完整项目

### 阶段 4 检查点
- [ ] 能独立阅读论文
- [ ] 参与开源贡献
- [ ] 有个人代表作

---

<div align="center">

**💡 提示**: 学习进度因人而异，建议按需调整

[← 返回主页](../README.md)

</div>

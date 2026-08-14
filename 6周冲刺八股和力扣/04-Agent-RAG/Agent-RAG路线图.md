---
title: Agent-RAG路线图
status: active
---

# Agent / RAG 路线图

## RAG 主线

1. [LLM 基础](LLM基础.md)：Token、上下文、生成和限制。
2. [RAG](RAG.md)：采集、切分、索引、检索、生成与引用。
3. 检索增强：Metadata、Query Rewrite、Dense + BM25、RRF、Reranker。
4. [评估与可观测性](评估与可观测性.md)：评测集、Recall@K、生成忠实度、延迟和成本。

## Agent 主线

1. [Agent 与 Tool Calling](Agent与Tool-Calling.md)：结构化输出、工具定义、状态、路由和重试。
2. 工作流：Checkpoint、人工审批、失败恢复和幂等。
3. [MCP](MCP.md)：Client、Server、Tools、Resources 和安全边界。
4. 生产能力：权限、审计、Prompt Injection 防护、降级和监控。

## 完成标准

- 能画图并解释数据和请求如何流动。
- 能说明为什么采用该方案，以及不用它会怎样。
- 每个指标说明数据、基线、参数和失败样例。
- 能区分已经验证的事实与未来计划。

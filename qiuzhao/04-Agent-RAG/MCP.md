---
title: MCP
status: planned
---

# MCP

## 学习问题

- MCP Client、Server 和 Host 分别承担什么职责？
- Tools、Resources、Prompts 的语义有什么区别？
- 本地 STDIO 与网络传输的信任边界有何不同？
- 如何做工具发现、参数校验、认证、授权和审计？
- 为什么“接入 MCP”不自动意味着系统安全或可靠？

## 项目验收

- [ ] 独立实现一个只读 MCP Server。
- [ ] 至少暴露一个 Tool 和一个 Resource。
- [ ] 对输入做结构化校验。
- [ ] 为错误、超时和权限拒绝保留可追踪日志。
- [ ] 明确禁止模型直接触发的高风险操作。

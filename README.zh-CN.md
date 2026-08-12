# qiuzhao-skills

面向中文校招与实习申请的开源 Skills 集合：从招聘官网发现岗位，基于简历证据判断匹配度，定制简历，辅助填写网申，并准备面试。

## Skills

| Skill | 用途 | 关键输出 |
|---|---|---|
| `job-fit-ranker` | 分析招聘官网或 JD，筛选并排序岗位 | 硬条件、匹配分、证据、缺口、官方链接 |
| `jd-resume-tailor` | 针对单个 JD 优化现有简历 | 改写内容、关键词覆盖、事实核验清单 |
| `application-form-helper` | 将简历映射到中文网申表单 | 字段计划、缺失冲突、提交前检查 |
| `interview-prep` | 根据 JD 和简历准备面试 | 技术深挖、STAR 提纲、追问、补齐计划 |

## 安装

安装全部 Skills：

```bash
npx skills add luosir1123-ai/qiuzhao-skills -g
```

只安装一个 Skill：

```bash
npx skills add luosir1123-ai/qiuzhao-skills --skill job-fit-ranker -g
```

也可以克隆仓库后从本地路径安装：

```bash
git clone https://github.com/luosir1123-ai/qiuzhao-skills.git
npx skills add ./qiuzhao-skills -g
```

## 推荐流程

1. 用 `$job-fit-ranker` 输入招聘官网和简历，得到岗位排名。
2. 用 `$jd-resume-tailor` 针对首选岗位生成事实可核验的定制版本。
3. 用 `$application-form-helper` 映射并填写网申字段，在最终提交前人工检查。
4. 用 `$interview-prep` 生成岗位相关的技术深挖和回答提纲。

示例提示词：

```text
使用 $job-fit-ranker 分析这个招聘官网，完整阅读候选岗位 JD，结合我的简历给出 Top 5，并标出学历、届别、专业等硬条件。
```

## 设计原则

- 证据优先：匹配结论必须对应简历事实。
- 硬条件优先：学历、届别、专业、语言等不被综合分掩盖。
- 分类准确：实习、工作、项目、科研经历不相互冒充。
- 隐私本地化：仓库不需要上传简历，也不提供托管后端。
- 人工最终确认：不绕过验证码、身份校验、声明或最终投递按钮。

## 局限

招聘网站结构和岗位状态随时可能变化；登录、反自动化机制或不可见分页会限制覆盖范围。Skill 应报告实际检查范围，不承诺抓取完整性，也不保证录用结果。

## 开发与贡献

```bash
python3 -m unittest discover -v
python3 scripts/validate.py
python3 scripts/check_private_data.py .
```

提交示例必须使用虚构身份和 `example.com` 邮箱。详见 [AGENTS.md](AGENTS.md)。

## License

[MIT](LICENSE)

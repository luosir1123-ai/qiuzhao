---
title: Python基础速查
status: active
---

# Python 基础速查

> [!tip] 使用方式
> 先完成练习，再回来查语法。读懂代码不算会，关闭笔记后能写出来才算。

## Day 1 最小语法

```python
name = input("name: ")
age = int(input("age: "))

if age >= 18:
    message = f"{name} is an adult"
else:
    message = f"{name} is a minor"

print(message)
```

## 循环与容器

```python
scores = [80, 95, 67]
total = 0

for score in scores:
    total += score

average = total / len(scores)
passed = {score for score in scores if score >= 60}
by_name = {"Alice": 80, "Bob": 95}
```

- `list` 有序、可重复、可修改。
- `tuple` 有序、可重复、不可修改。
- `dict` 保存键值映射，键必须可哈希。
- `set` 保存不重复元素，适合判重和集合运算。

## 函数

```python
def count_words(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

## 闭卷练习

- [ ] 输入两个整数，输出较大的数；相等时输出 `equal`。
- [ ] 输入若干空格分隔整数，输出最大值、最小值和平均值。
- [ ] 统计一句话中每个单词出现的次数。
- [ ] 写函数去除列表中的重复元素并保持原顺序。

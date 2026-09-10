# Text Stats

这是一个使用 Python 标准库实现的简单英文词频统计程序。程序从 UTF-8 文本文件中提取英文单词，忽略大小写，并按出现次数从高到低输出；出现次数相同时，按单词字母顺序输出。

## 运行方法

在项目根目录执行：

```text
python code/text_stats.py <文本文件路径>
```

例如：

```text
python code/text_stats.py sample.txt
```

示例输出：

```text
hello: 2
is: 2
python: 2
world: 2
and: 1
simple: 1
the: 1
wide: 1
```

程序使用正则表达式 `[A-Za-z]+` 提取英文单词。文件不存在、无法读取或不是有效的 UTF-8 文件时，会输出错误提示并以非零状态码退出。

Web edit for Git pull practice

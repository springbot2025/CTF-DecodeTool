# 简单的CTF工具练习

## 当前结构

```text
.
├── main.py              # 程序入口
├── decoder.py           # 兼容旧导入路径
└── ctf_tool/
    ├── cli.py           # 命令行交互
    ├── constants.py     # 菜单和文案常量
    └── decoder.py       # 核心解码与 flag 提取逻辑
```

## 1.0版本

- 支持base64,hex,binary等简单编码转换
- 支持flag自动搜索
- 一些简单的错误处理，如错误的base64编码形式处理（补全padding），flag头输入自动去掉"{"等等

## 1.01版本

- 一些简单更新
- 利用base64库增加了其他base族解码方式
- 修复了一些已知问题
- README.md中增加了todo list

## 2.0版本

- 模块化管理，文件大改，逻辑在ctf_tool中并封装
- 各方面format格式化

### 提示

- 正在制作中，会第一时间推送成果
- 建议：下载后运行main.py
- 可执行文件在exe文件夹里，更新不及时见谅
- 代码中会有很多bug，欢迎测试并提出qwq

## todolist

- GUI界面
- 增加更多编码/加密方式
- 为嵌套解码设计链式调用
- _find_flag方法的拓展：尝试发现flag头的基础编码（ZmxhZw等），这可能需要在重构方法之后实现

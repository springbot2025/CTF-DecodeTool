"""
一些常量的定义。
统一大写
"""

APP_TITLE = "欢迎使用 Spring 的 CTF 工具！"
DIVIDER = "=" * 30

MAIN_MENU = {
    "1": "解码工具",
    "2": "长文本寻找 flag",
    "3": "暴力破解 flag（todo）",
}

DECODE_METHODS = {
    "1": ("base64", "base64"),
    "2": ("base32", "base32"),
    "3": ("base16", "base16"),
    "4": ("base85", "base85"),
    "5": ("hex", "hex"),
    "6": ("binary", "binary"),
}

DECRYPT_METHODS = {
    "1": ("xor", "xor"),
}

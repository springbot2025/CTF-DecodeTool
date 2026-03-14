"""命令行交互入口。"""

from __future__ import annotations

import time

from .constants import APP_TITLE, DECODE_METHODS, DECRYPT_METHODS, DIVIDER, MAIN_MENU
from .decoder import Decode


def run() -> None:
    print(DIVIDER)
    print(APP_TITLE)

    while True:
        _print_main_menu()
        choice = input("请输入编号：").strip()

        if choice == "1":
            _handle_decode_tool()
        elif choice == "2":
            _handle_find_flag()
        elif choice == "3":
            print("暴力破解功能还在开发中。")
        else:
            print("请输入正确的编号！")

        if _exit():
            print("感谢使用，再见！")
            time.sleep(2)
            break


def _print_main_menu() -> None:
    print("请选择你需要的功能：")
    for key, label in MAIN_MENU.items():
        print(f"{key}. {label}")


def _handle_decode_tool() -> None:
    cypher = input("请输入密文：")
    flag_header = _read_flag_header()
    key = _read_optional_key()
    decoder = Decode(cypher, key=key, flag_header=flag_header)

    if key:
        method = _choose_method("请选择解密方式：", DECRYPT_METHODS)
    else:
        method = _choose_method("请选择解码方式：", DECODE_METHODS)

    if method is None:
        print("请输入正确的编号！")
        return

    result = decoder.decode_with(method)
    if result is not None:
        decoder.print_ans(result)


def _handle_find_flag() -> None:
    text = input("请输入文本：\n")
    decoder = Decode("", flag_header=_read_flag_header())
    flag = decoder.find_flag(text)
    if flag:
        print(f"找到flag：\"{flag}\"")
        return
    print("未找到符合格式的flag。")


def _read_flag_header() -> str:
    flag_header = input("请输入flag头（回车则默认为flag）：").strip()
    return flag_header or "flag"


def _read_optional_key() -> str | None:
    key = input("请输入密钥（无密钥则直接回车）：").strip()
    return key or None


def _choose_method(prompt: str, options: dict[str, tuple[str, str]]) -> str | None:
    labels = [f"{key}. {value[1]}" for key, value in options.items()]
    choice = input(f"{prompt}{' '.join(labels)}\n").strip()
    method = options.get(choice)
    if method:
        return method[0]
    return None


def _exit() -> bool:
    choice = input("输入quit退出，输入回车继续：").strip().lower()
    return choice == "quit"

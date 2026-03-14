"""核心解码逻辑。"""

from __future__ import annotations

import base64 as b64
import re
from string import hexdigits
from typing import Callable


class Decode:
    """封装常见 CTF 解码能力和 flag 提取逻辑。"""

    def __init__(
        self,
        cypher: str,
        key: str | None = None,
        flag_header: str = "flag",
        if_clean: bool = False,
    ) -> None:
        self.c = cypher
        self.k = key
        self.fh = self._normalize_flag_header(flag_header)
        self.if_clean = if_clean

    @staticmethod
    def _normalize_flag_header(flag_header: str) -> str:
        header = (flag_header or "flag").strip()
        header = header.split("{")[0]
        return header or "flag"

    def clean(self, value: str | None = None) -> str:
        raw = self.c if value is None else value
        return "".join(raw.split()).replace(",", "")

    def decode_with(self, method: str) -> str | None:
        handler = getattr(self, method, None)
        if handler is None or not callable(handler):
            raise ValueError(f"不支持的方法: {method}")
        return handler()

    def _decode_bytes(
        self,
        method_name: str,
        decoder: Callable[[str], bytes],
        value: str,
    ) -> str | None:
        try:
            decoded = decoder(value).decode("utf-8", errors="ignore")
        except Exception as exc:
            print(f"{method_name}解码失败，原因: {exc}")
            return None
        return decoded

    def base64(self) -> str | None:
        value = self.clean()
        padding = len(value) % 4
        if padding:
            value += "=" * (4 - padding)
        return self._decode_bytes("base64", b64.b64decode, value)

    def base32(self) -> str | None:
        value = self.clean()
        return self._decode_bytes("base32", b64.b32decode, value)

    def base16(self) -> str | None:
        value = self.clean().upper()
        return self._decode_bytes("base16", b64.b16decode, value)

    def base85(self) -> str | None:
        value = self.clean()
        return self._decode_bytes("base85", b64.b85decode, value)

    def hex(self) -> str | None:
        value = self.clean().lower().replace("0x", "")
        try:
            decoded = bytes.fromhex(value).decode("utf-8", errors="ignore")
        except Exception as exc:
            print(f"hex解码失败，原因: {exc}")
            return None
        return decoded

    def binary(self) -> str | None:
        value = self.clean().replace("0b", "")
        try:
            number = int(value, 2)
            size = max(1, (number.bit_length() + 7) // 8)
            decoded = number.to_bytes(size, "big").decode("utf-8", errors="ignore")
        except Exception as exc:
            print(f"binary解码失败，原因: {exc}")
            return None
        return decoded

    def xor(self) -> str | None:
        if not self.k:
            print("xor解码失败，原因: 缺少密钥")
            return None

        cipher_text = self.clean()
        key_bytes = self.k.encode("utf-8")

        try:
            cipher_bytes = self._to_bytes(cipher_text)
            decoded = bytes(
                value ^ key_bytes[index % len(key_bytes)]
                for index, value in enumerate(cipher_bytes)
            )
        except Exception as exc:
            print(f"xor解码失败，原因: {exc}")
            return None

        return decoded.decode("utf-8", errors="ignore")

    def reverse(self) -> str:
        return self.clean()[::-1]

    def _to_bytes(self, value: str) -> bytes:
        normalized = value.lower().replace("0x", "")
        if normalized and len(normalized) % 2 == 0 and all(char in hexdigits for char in normalized):
            return bytes.fromhex(normalized)
        return value.encode("utf-8")

    def find_flag(self, text: str) -> str | None:
        pattern = rf"{re.escape(self.fh)}\{{[^{{}}]+\}}"
        match = re.search(pattern, text)
        if match:
            return match.group(0)
        return None

    def print_ans(self, ans: str) -> None:
        print(f"原始解码结果为：\"{ans}\"")
        print("正在寻找flag...")
        flag = self.find_flag(ans)
        if flag:
            print(f"找到flag：\"{flag}\"")
            return
        print("尝试后未找到flag，可能需要多次嵌套解码。")

    def _find_flag(self, text: str) -> str | None:
        return self.find_flag(text)

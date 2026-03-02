class Decode:
    def __init__(self, cypher, key = None, flag_header = "flag"):
        self.c = cypher
        self.k = key
        self.fh = flag_header.split("{")[0]
    
    def clean(self):
        self.c = "".join(self.c.split()).replace(",","")
    
    def base64(self):
        self.clean()
        import base64
        padding = len(self.c) % 4
        if padding:
            self.c += "=" * (4 - padding)
        try:
            m = base64.b64decode(self.c).decode('utf-8', errors = 'ignore')
        except Exception as e:
            print(f"base64解码失败，原因: {e}")
            return
        print(f"原始解码结果为\"{m}\"")
        self._find_flag(m)
    
    def hex(self):
        self.clean()
        self.c = self.c.lower()
        self.c = self.c.replace("0x", "")
        try:
            m = bytes.fromhex(self.c).decode('utf-8', errors = 'ignore')
        except Exception as e:
            print(f"hex解码失败，原因: {e}")
            return
        print(f"原始解码结果为\"{m}\"")
        self._find_flag(m)
    
    def binary(self):
        self.clean()
        self.c = self.c.replace("0b", "")
        try:
            n = int(self.c, 2)
            m = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', errors = 'ignore')
        except Exception as e:
            print(f"binary解码失败，原因: {e}")
            return
        print(f"原始解码结果为\"{m}\"")
        self._find_flag(m)
    
    def xor(self):
        self.clean()
        
        
    def _find_flag(self, m):
        if self.fh in m and "}" in m and "{" in m:
                    print("找到flag:")
                    flag = self.fh + "{" + m.split("{")[1].split("}")[0] + "}"
                    print(f"{flag}")
        else:
            print("尝试后未找到flag, 可能需要多次嵌套解码")
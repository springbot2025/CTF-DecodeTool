'''
CTF一把梭神秘小工具
'''
from decoder import Decode
import time

def main():
    while True:
        print("请选择你需要的功能：")
        print("1. 解码工具（自动寻找flag）")
        print("2. 长文本寻找flag")

        choice = input("请输入编号：")
        if choice == "1":
            c = input("请输入密文:\n")

            flag_header = input("请输入flag的前缀（输入回车则默认为flag）：")
            if flag_header.strip() == "":
                flag_header = "flag"
            
            key = input("请输入密钥：（无密码则输入回车）\n")
            if key.strip() == "":
                key = None
            
            decoder = Decode(c, key, flag_header)

            if not key:
                choice2 = input("请选择解码方式：1. base64 2. hex 3. binary\n")
                if choice2 == "1":
                    decoder.base64()
                elif choice2 == "2":
                    decoder.hex()
                elif choice2 == "3":
                    decoder.binary()
            else:
                choice2 = input("请选择解密方式：1. xor\n")
                if choice2 == "1":
                    decoder.xor()

        if choice == "2":
            text = input("请输入文本:\n")

            flag_header = input("请输入flag的前缀（输入回车则默认为flag）：")
            if flag_header.strip() == "":
                flag_header = "flag"
            
            decoder = Decode("", flag_header = flag_header)
            decoder._find_flag(text)
        else:
            print("请输入正确的编号！")
        i = input("输入quit退出，输入回车继续：")
        if i == "quit":
            print("感谢使用，再见！")
            time.sleep(2)
            break

if __name__ == '__main__':
    print("=" * 30)
    print("欢迎使用Spring的CTF工具！")
    main()
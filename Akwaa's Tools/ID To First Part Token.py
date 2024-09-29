import os
import base64
def main():
    os.system("cls")
    userid = input("id : ")
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print()
    print("premiere partie du token", encodedStr)
main()
class InputError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


def get_input():
    name = input("请输入你的姓名：")
    if name == "":
        raise InputError("未输入内容")


try:
    get_input()
except InputError as e:
    print(e)

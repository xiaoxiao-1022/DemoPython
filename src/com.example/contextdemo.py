import contextlib


@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print("open file:", file_name, "in __enter__")
    file_handler = open(file_name, "r")

    # 【重点】：yield
    yield file_handler

    # __exit__方法
    print("close file:", file_name, "in __exit__")
    file_handler.close()
    return


with open_func("/Users/MING/mytest.txt") as file_in:
    for line in file_in:
        print(line)

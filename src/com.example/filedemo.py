file = open("iterabledemo.py")
print(file.readline())
file.close()


with open("iterabledemo.py") as file:
    print(file.readline())

    class Resource:
        def __enter__(self):
            print("===connect to resource===")
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print("===close resource connection===")

        def operate(self):
            print("===in operation===")

    with Resource() as res:
        res.operate()

astr = "abc"
alist = [1, 2, 3]
adict = {"name": "wangbm", "age": 18}
agen = (i for i in range(4, 8))


def gen(*args, **kw):
    for item in args:
        yield from item


new_list = gen(astr, alist, adict, agen)
print(list(new_list))

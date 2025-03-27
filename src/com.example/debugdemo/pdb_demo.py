import utils


def myfunc(mylist):
    import pdb

    pdb.set_trace()
    result = utils.sum(mylist)
    print(result)


if __name__ == "__main__":
    print("----start----")
    myfunc([1, 2, 3, 4])
    print("----end-----")

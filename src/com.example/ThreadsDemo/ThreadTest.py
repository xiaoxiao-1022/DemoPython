# CPU计算密集型
import time

import requests


def count(x=1, y=1):
    # 使程序完成150万计算
    c = 0
    while c < 50000:
        c += 1
        x += x
        y += y


# 磁盘读写IO密集型
def io_disk():
    with open("hosts.txt", "w") as f:
        for x in range(500000):
            f.write("python-learning\n")


# 网络IO密集型
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
url = "https://www.tieba.com/"


def io_request():
    try:
        webPage = requests.get(url, headers=header)
        html = webPage.text
        return
    except Exception as e:
        return {"error": e}


# 【模拟】IO密集型
def io_simulation():
    time.sleep(2)

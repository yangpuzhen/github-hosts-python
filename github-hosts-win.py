import requests
import win32con
from bs4 import BeautifulSoup
from time import sleep
import win32api

# 本代码由codegeex生成
url1 = 'https://gitlab.com/ineo6/hosts/-/raw/master/next-hosts'
url2 = 'https://gitee.com/frankwuzp/github-host/raw/main/hosts'

choice = input("请选择能访问的数据源，输入1数据源为gitlab,输入2数据源为gitee：")

if choice == '1':
    url = url1
elif choice == '2':
    url = url2
else:
    win32api.MessageBox(0, "输入信息非法，请重新输入", "hosts", win32con.MB_OK)
    exit()

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()

with open("C:\Windows\System32\drivers\etc\hosts", 'w', encoding='utf-8') as f:
    f.write(text)
    sleep(3);
if f.closed:
    win32api.MessageBox(0, "写入host信息成功。", "hosts", win32con.MB_OK)
    with open("C:\Windows\System32\drivers\etc\hosts", 'r', encoding='utf-8') as f:
        print(f.read())
else:
    win32api.MessageBox(0, "写入host信息失败。", "hosts", win32con.MB_OK)
    with open("C:\Windows\System32\drivers\etc\hosts", 'r', encoding='utf-8') as f:
        print(f.read())

# -*-coding:  utf-8 -*-
"""
# File Name    : test.py
# Create Time  : 2023/10/30 0030
# Author       : QinZhou
# Email        : 1185917912@qq.com
# Described    : 
"""
import sys
import urllib.request


def main1():
    urlresult = urllib.request.urlopen("http://www.baidu.com").read()
    print(urlresult)


if __name__ == "__main__":
    main1()
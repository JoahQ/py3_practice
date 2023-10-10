# -*-coding: utf-8 -*-
"""
# File Name    : pizza.py.py
# Create Time  : 2023/8/8 0008
# Author       : QinZhou
# Email        : 1185917912@qq.com
# Described    : 
"""


def make_pizza(size, *toppings):
    """

    :param size:
    :param toppings:
    :return:
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
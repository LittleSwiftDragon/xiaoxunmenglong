#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Frankiln Zheng'

def check_account(name):
    print(f"""
---------------查询余额-----------------
{name}，你好，您的余额剩余：{database[name]}元
        """)
    cmd = input('请输入任意键返回主菜单')
    if not cmd:
        main_menu(name)


def deposit(name):
    print(f"""
------------------存款--------------------
{name}，你好，您的余额剩余：{database[name]}元
    """)
    num = int(input('请输入您的存款金额：'))
    database[name] += num
    print(f"""
{name}，你好，您存款{num}元成功
{name}，你好，您的余额剩余：{database[name]}元
        """)
    cmd = input('请输入任意键返回主菜单')
    if not cmd:
        main_menu(name)


def drawback(name):
    print(f"""
------------------取款--------------------
{name}，你好，您的余额剩余：{database[name]}元
    """)
    num = int(input('请输入您的取款金额：'))
    database[name] -= num
    print(f"""
{name}，你好，您取款{num}元成功
{name}，你好，您的余额剩余：{database[name]}元
            """)
    cmd = input('请输入任意键返回主菜单')
    if not cmd:
        main_menu(name)


def exit_menu():
    print('感谢您的使用，下次再见')


def main_menu(name):
    print(f"""
-----------------主菜单-----------------
{name}，你好，欢迎来到天地银行ATM，请选择操作：
查询余额\t[输入1]
存款\t\t[输入2]
取款\t\t[输入3]
退出\t\t[输入4]
    """)
    choice = int(input('请输入您的选择：'))  # 以下部分将导致函数嵌套使用，可能效率不高，最好弄出主脚本循环调用,
    # 以上的余额可以采用调用查询即可，通过判断实现表头去除
    if choice == 1:
        check_account(name)
    elif choice == 2:
        deposit(name)
    elif choice == 3:
        drawback(name)
    elif choice == 4:
        exit_menu()
    else:
        print('输入有误，请重新输入')
        main_menu(name)


database = {'Mike': 5000000}
name = input('请输入您的姓名：')
main_menu(name)

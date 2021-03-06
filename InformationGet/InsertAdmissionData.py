#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : InsertAdmissionData.py
@Author: SangYu
@Date  : 2018/12/25 14:03
@Desc  : 此程序用于将招生数据插入数据库
'''
from InformationGet import MysqlOperation
import os


# 读取文件目录下所有文件（不包含文件夹）
def read_all_file_list(dir_path):
    file_list = []
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            file_list.append(file_path)
    return file_list


# 读取文档内容
def read_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


# 获取MySQL表构造表项列表
def get_insert_mysql_table_tuple(file_path, school):
    file_content = read_file_content(file_path)
    file_name = file_list[0].split("\\")[-1]
    year = file_name.split(" ")[0]
    district = file_name.split(" ")[1]
    # print("年份：", year, "地区：", district)
    table_content = []
    for i in range(len(file_content)):
        file_content[i] = file_content[i].strip()
        temp = file_content[i].split("\t")
        table_content.append(temp)
    table_head = table_content[0]
    # print("表头：", table_head)
    table_content = table_content[1:]
    mysql_content = []
    for item in table_content:
        major = item[0]
        classy = item[1]
        numbers = item[2]
        temp = (school, district, major, year, classy, numbers)
        mysql_content.append(temp)
    # for item in mysql_content:
    #     print(item)
    return mysql_content


if __name__ == "__main__":
    # print(read_all_file_list("Information/九校联盟/哈尔滨工业大学/招生计划"))
    dir_path = "Information/九校联盟/哈尔滨工业大学/招生计划"
    school = "哈尔滨工业大学"
    file_list = read_all_file_list(dir_path)
    mysql_content = get_insert_mysql_table_tuple(file_list[0], school)
    for item in mysql_content:
        print(item)

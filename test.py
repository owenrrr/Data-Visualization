#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import csv
import json

# file:json to csv
def transcsv(jsonpath, csvpath):
    json_file = open(jsonpath, 'r', encoding='utf8')
    csv_file = open(csvpath, 'w', newline='')
    # 读文件
    ls = json.load(json_file)  # 将json格式的字符串转换成python的数据类型，解码过程


    # data = [list(ls[0].keys())]  # 获取列名,即key
    # for item in ls:
    #     data.append(list(item.values()))  # 获取每一行的值value
    # 写入文件
    for line in ls:
        csv_file.write(str(line[0]) + "," + str(line[1]) + "\n")  # 以逗号分隔一行的每个元素，最后换行 fw.close() #关闭csv文件
    # 关闭文件
    json_file.close()
    csv_file.close()


# file:csv to json
def transjson(jsonpath, csvpath):
    fw = open(jsonpath, 'w', encoding='utf8')  # 打开csv文件


    fo = open(csvpath, 'r', newline='')  # 打开csv文件

    ls = []
    for line in fo:
        line = line.replace("\n", "")  # 将换行换成空
        ls.append(line.split(","))  # 以，为分隔符
    # print(ls)
    # 写入
    for i in range(1, len(ls)):  # 遍历文件的每一行内容，除了列名
        ls[i] = dict(zip(ls[0], ls[i]))  # ls[0]为列名，所以为key,ls[i]为value,
        # zip()是一个内置函数，将两个长度相同的列表组合成一个关系对

    json.dump(ls[1:], fw, sort_keys=True, indent=4)
    # 将Python数据类型转换成json格式，编码过程
    # 默认是顺序存放，sort_keys是对字典元素按照key进行排序
    # indet参数用语增加数据缩进，使文件更具有可读性

    # 关闭文件
    fo.close()
    fw.close()

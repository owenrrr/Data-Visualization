#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import csv
import time
import os
from test import transcsv

header = ('name', 'type', 'value', 'date')

def start():
    # 最终的csvFile
    csvfinalFile = open('./fixed/players.csv', 'w', newline='',encoding='utf8')
    final = csv.writer(csvfinalFile)
    final.writerow(header)

    # 全部json文件名
    filenameList = os.listdir('./json')
    timeList = []
    numberList = []
    finalList = []

    for i in filenameList:
        # 创建新的csv文件
        jsonpath = './json/' + i
        csvpath = './csv/' + i[:-4] + 'csv'
        transcsv(jsonpath, csvpath)

        # 打开需要修改的.csv文件
        csvFile = open(csvpath, 'r',encoding='utf8')
        f = csv.reader(csvFile)
        for ind in f:
            numberList.append(ind[1])
            j = time.localtime(int(ind[0]) / 1000)
            k = time.strftime('%Y-%m-%d', j)
            timeList.append(k)

        for index in range(len(numberList)):
            final.writerow((i[:-4], 'Games', numberList[index], timeList[index]))

        timeList = []
        numberList = []
        csvFile.close()
    csvfinalFile.close()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import readJSON

data = readJSON.读JSON文件("data.json")
沙雕简介 = data["沙雕简介"]
第一章 = data["第一章"]
第二章 = data["第二章"]
第三章 = data["第三章"]
第四章 = data["第四章"]
第五章 = data["第五章"]
a="沙雕小说\n第一章:二狗的回忆"
b="\n第二章:王八之气"
c="\n第三章:合格的沙雕"
d="\n第四章:凑不够字数"
e="\n第五章:卖火柴的小红帽"
if __name__ == "__main__":
    print(a+b+c+d+e)
    sb = input("请选择章节或章节名称:")
    if(sb=="第一章" or sb=="二狗的回忆"):
        print(str(沙雕简介))
        print(str(第一章))
    elif(sb=="第二章" or sb=="王八之气"):
        print(str(第二章))
    elif(sb=="第三章" or sb=="合格的沙雕"):
        print(str(第三章))
    elif (sb == "第四章" or sb == "凑不够字数"):
        print(str(第四章))
    elif (sb == "第五章" or sb == "卖火柴的小红帽"):
        print(str(第五章))
    else:
        print("暂无此章节，方向盘给你你开！")
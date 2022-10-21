#-*-coding:utf-8-*-

import os
import io

# 统计gspan.data文件中图的个数
n = []     #存储多个文件的图的个数
path1 = "gspan_data"  #数据未处理的文件夹
files= os.listdir(path1)   #得到文件夹下的所有文件名称
for file in files:
    i = 0
    file_read = io.open(path1+"/"+file,'r',encoding='utf-8')
    try:
        lines = file_read.readlines()
        for line in lines:
            if "t " in line:
                i+=1
        i-=1
        n.append(i)
    finally:
        file_read.close()

#存储输出多个文件的文件名
files2 = []
for i in range(1,len(n)+1):
    if i <= 9:
        files2.append("gspan_output"+"0"+str(i)+".data")
    else:
        files2.append("gspan_output" +str(i) + ".data")

#将运行命令写入test.bat
file_write = open("test.bat",'w')
paths_1 = []
paths_2 = []
path2 = "gspan_preoutput"
for file in files:
    paths_1.append(" ./" + path1 + "/" + file)
for file in files2:
    paths_2.append(" ./" + path2 + "/" + file)
try:
    for j in range(len(n)):
        file_write.write("python -m gspan_mining -s "+str(n[j])+paths_1[j]+" >"+paths_2[j]+"\n")
finally:
    file_write.close()
#在windows终端执行test.bat文件的命令
os.system("test.bat")

#将输出结果保留成“t # 0 v 0 4 v 1 5 e 0 1 4”这种格式
# path2 = "gspan_preoutput" #数据未处理的文件夹
path3 = "gspan_output"    #数据处理之后的文件夹
files3= os.listdir(path2) #得到文件夹下的所有文件名称
s = []
for file in files3:
    file_read = io.open(path2+"/"+file,'r',encoding='utf-8')
    with io.open(path3+"/"+file,'w',encoding='utf-8') as file_write:
        try:
             lines = file_read.readlines()
             for line in lines:
                 if ("t " in line) | ("v " in line) |("e " in line):
                     file_write.write(line)
        finally:
            file_read.close()
            file_write.close()
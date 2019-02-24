import pandas as pd
def dataToCsv(file, data, columns, target):
    """
    数据转化为CSV文件
    :param file:文件对象
    :param data:数据集的数据部分
    :param columns:数据集的特征名称
    :param target:数据集的结果
    :return:CSV文件
    """
    data = list(data)
    columns = list(columns)
    file_data = pd.DataFrame(data, index=range(len(data)), columns=columns)
    file_target = pd.DataFrame(target, index=range(len(data)), columns=['target'])
    file_all = file_data.join(file_target, how='outer')
    file_all.to_csv(file)

def text_save(filename, data):
    """
    Python 将列表数据写入文件（txt）
    :param filename:filename为写入CSV文件的路径
    :param data: data为要写入数据列表
    :return:
    """
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

import csv
import codecs
def data_write_csv(file_name, datas):
    """
    Python 将列表数据写入文件（csv）
    :param file_name: file_name为写入CSV文件的路径
    :param datas:datas为要写入数据列表
    :return:csv文件
    """
    file_csv = codecs.open(file_name,'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(data)
    print("保存文件成功，处理结束")

import xlwt
def data_write(file_path, datas):
    """
    Python 将列表数据写入文件（excel）
    :param file_path:要保存的路径
    :param datas:要保存的数据
    :return:
    """
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i, j, data[j])
        i = i + 1
        f.save(file_path)  # 保存文件
import numpy as np

def main():
    with open('node_position_mode1.txt', 'r') as f1:
        list1_node_position = f1.read()#字符串格式 导入node position数据
    new_list1=list1_node_position.replace('[', '').replace(']', '')  # 去除[]

    f = open("node_position_mode1_number.txt", 'w')# 去除[]后重新导出 只剩数字的str
    for ip in new_list1:
        f.write(str(ip))
    f.close()

    with open('node_position_mode1_number.txt', 'r') as f1:#导入只含数字的str
        list1_node_position = f1.read()
    b=list1_node_position.split('\n')#根据换行拆分
    d=[]#化字符串为ndarray
    for i in range(50):
        a=b[i].split()
        c = []
        for each in a:
            c.append(float(each))
        d.append(c)
    #建立程序可用ndarray
    list2=[]
    count=0
    data_count=0
    while count<10:
        list3=np.zeros((5,3))
        for i in range(5):
            for j in range(3):
                list3[i][j]=d[data_count+i][j]
        list2.append(list3)
        data_count=data_count+5
        count+=1
    print(list2)



if __name__ == '__main__':
    main()

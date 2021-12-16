import pymysql
import csv
import math
import os

wind_corr = {'south': '南风', 'southeast': '东南风', 'southwest': '西南风', 'west': '西风', 'northwest': '西北风', 'north': '北风', 'northeast': '东北风', 'east': '东风'}

cities = ['西安', '宝鸡', '咸阳', '渭南', '铜川', '汉中', '商洛', '榆林', '安康', '延安']
nums = [43, 13, 6, 7, 2, 13, 4, 8, 15, 9]
binocular = [16, 12, 8, 8, 7, 12, 7, 9, 14, 9]
conn = pymysql.connect(host='10.249.44.81', user='root', password='Talented10', charset='utf8mb4')
cursor = conn.cursor()
'''
sql_create = "create database if not exists hetero"
cursor.execute(sql_create)
'''
'''
sql_use = "use hetero;"
cursor.execute(sql_use)
'''
#sql_create_table = ''' create table wind_images (`id` int not null auto_increment, `city` char(5) not null, `path` char(60) not null, wind_direction char(5), wind_power char(5), primary key (`id`)) default charset=utf8;'''
#cursor.execute(sql_create_table)
'''
f = open('wind.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(f)
sql_insert = "insert into wind_images(city, path, wind_direction, wind_power) values(%s, %s, %s, %s);"
csv_res = []
ind = 0
for line in csv_reader:
    csv_res.append(line)
for ind_bino, bino in enumerate(binocular):
    for i in range(bino):
        full_name = 'wind_shift/' + csv_res[ind + i][0] + '.jpg'
        tmp = csv_res[ind + i][2] + '级'
        #print(full_name)
        try:
            cursor.execute(sql_insert, (cities[ind_bino], full_name, wind_corr[csv_res[ind + i][1]], tmp))
            conn.commit()
        except:
            print('nok')
            conn.rollback()
    ind += bino
'''
'''
sql_insert = "insert into float_images(city, path) values(%s, %s);"
img_name = os.listdir('static/visual_epoch_24')
ind = 0
for ind_bino, bino in enumerate(binocular):
    for i in range(bino):
        full_name = 'visual_epoch_24/' + img_name[ind + i]
        #print(full_name)
        try:
            cursor.execute(sql_insert, (cities[ind_bino], full_name))
            conn.commit()
        except:
            print('nok')
            conn.rollback()
    ind += bino
'''
#conn.close()
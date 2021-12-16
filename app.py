from flask import Flask, redirect, url_for, render_template, make_response
from flask.helpers import flash
from flask_cors import CORS
import pymysql

app = Flask(__name__, static_url_path='')
cors = CORS(app, resources=r'/*')

result = []
conn = pymysql.connect(host='localhost', user='root', password='Talented10', charset='utf8mb4')
cursor = conn.cursor()
sql_db = "use hetero;"
cursor.execute(sql_db)

sql_disaster = "select * from disaster;"
cursor.execute(sql_disaster)
disaster_result = cursor.fetchall()
result.append(disaster_result)

sql_play = "select * from play;"
cursor.execute(sql_play)
play_result = cursor.fetchall()
result.append(play_result)

sql_float = "select * from float_detection;"
cursor.execute(sql_float)
float_result = cursor.fetchall()
result.append(float_result)

sql_float_img = "select * from float_images;"
cursor.execute(sql_float_img)
ft_images = cursor.fetchall()
ft_dict = {}
for im in ft_images:
    if im[1] not in ft_dict:
        ft_dict[im[1]] = [im[2]]
    else:
        ft_dict[im[1]].append(im[2])
result.append(ft_dict)

sql_wind_img = "select * from wind_images;"
cursor.execute(sql_wind_img)
wd_images = cursor.fetchall()
wd_dict = {}
for im in wd_images:
    if im[1] not in wd_dict:
        wd_dict[im[1]] = [[im[2], im[3], im[4]]]
    else:
        wd_dict[im[1]].append([im[2], im[3], im[4]])
result.append(wd_dict)
print(result[4])

@app.route('/')
def index():
    resp = make_response(render_template('xxx.html', tag=result))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    #return render_template('xxx.html', tag=result)

if __name__ == '__main__':
    app.run()

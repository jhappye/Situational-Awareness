# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from admin import user


# 建立flask对象
app = Flask(__name__)
# 载入配置文件
app.config.from_pyfile('config.py')
# 创建数据库对象
db = SQLAlchemy(app)

#面板首页
@app.route('/',methods=['GET','POST'])
def index():
    return 'Hello World!'


#登录面板
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username= request.form['username']
        password= request.form['password']
        info=user.check(str(username),str(password))
        return info
    else:
        return render_template('login.html')

@app.route('/ip',methods=['GET','POST'])
def localbyip():
    if request.method=='POST':
        ip= request.form['ip']

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

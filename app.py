# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:16:02 2022

@author: syubi
"""

from flask import Flask,render_template, redirect,request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

import jinja2
import psycopg2
from sqlalchemy import create_engine  #匯入庫 建立搜尋引擎

from config import Config	
app = Flask(__name__)

SQLALCHEMY_TRACK_MODIFICATIONS = True


# 查詢時會顯示原始SQL語句

app.config['SQLALCHEMY_ECHO'] = True

 
# 禁止自動提交資料處理

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@127.0.0.1:5432/%s' % (Config.user,Config.password,Config.database)

# 設定sqlalchemy自動更跟蹤資料庫



 

# 讀取配置

app.config.from_object(Config)



# 建立資料庫sqlalchemy工具物件

db = SQLAlchemy(app)



@app.route('/',methods=['POST','GET'])
def hello():
    return render_template("index.html")




@app.route("/submit")
def submit():

    order1 = Order1()
    order1.custmer_id=request.args.get('custmer_id')
    order1.order_id=request.args.get('order_id')
    order1.customer_name=request.args.get('customer_name')
    order1.puechase_time=request.args.get('puechase_time')
    db.session.add(order1)
    db.session.commit()
    return"success"
    
@app.route("/submit1")
def submit1():

    
    order1 = Order1()
    # 


    order1 = Order1.query.filter(Order1.custmer_id==request.args.get('oldcustmer_id') or Order1.order_id==request.args.get('oldorder_id') or Order1.customer_name==request.args.get('oldcustomer_name') or Order1.puechase_time==request.args.get('oldpuechase_time')).first()


    order1.customer_name=request.args.get('newcustmer_id')
    order1.custmer_id=request.args.get('neworder_id')
    order1.order_id=request.args.get('newcustomer_name')
    order1.puechase_time=request.args.get('newpuechase_time')
       
    db.session.add(order1)
    db.session.commit()

    # # 已存在判斷 擋下
    # return "oldcustmer_id= "+aa1+"  newcustmer_id="+aa2
    
    return"success"
    

@app.route('/order/add')
def add1():
   
    return render_template("add.html")

@app.route('/order/modify')
def modify1(): 
    
    return render_template("modify.html")

class Order1(db.Model):

    # 定義表名

    __tablename__ = 'order'

    # 定義欄位

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)

    custmer_id = db.Column(db.String(64), unique=True)

    order_id = db.Column(db.String(64), unique=True) 
    
    customer_name = db.Column(db.String(64), unique=True)
    
    puechase_time = db.Column(db.String(64), unique=True)
    # def __init__(self):
    #     self.custmer_id="custmer_id"
    #     self.order_id="order_id"
    #     self.customer_name="customer_name"
    #     self.puechase_time="puechase_time"
    # def __init__(self, custmer_id,order_id,customer_name,puechase_time):
    #     self.custmer_id=custmer_id
    #     self.order_id=order_id
    #     self.customer_name=customer_name
    #     self.puechase_time=puechase_time
       
    
class Order_Item(db.Model):

    # 定義表名

    __tablename__ = 'order_item'

    # 定義欄位

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)

    order_id = db.Column(db.String(64), unique=True) 

    product_name = db.Column(db.String(64), unique=True) 

    amount=db.Column(db.String(64), unique=True) 
    
    product_id=db.Column(db.String(64), unique=True) 
    
    price=db.Column(db.String(64), unique=True) 
    


if __name__ == '__main__':
    app.run(port=8088,debug=True)

 
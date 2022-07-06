from flask import Flask
# class Config():
app = Flask(__name__)
class Config():
    """配置引數"""
    user = 'postgres'
    # database="table1", user="postgres", password="00000000", host="127.0.0.1", port="5432")

    password = '00000000'

    database = 'table1'
    # 設定連線資料庫的URL
    def __init__(self):
        
    
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@127.0.0.1:5432/%s' % (self.user,self.password,self.database)
    
     
    
        # 設定sqlalchemy自動更跟蹤資料庫
    
        # SQLALCHEMY_TRACK_MODIFICATIONS = True
    
     
    
        # # 查詢時會顯示原始SQL語句
    
        # app.config['SQLALCHEMY_ECHO'] = True
    
     
    
        # # 禁止自動提交資料處理
    
        # app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
        # # def __init__(self):
        #    # self.app=app
        # app.config.from_object(Config)
    
    
# app1=Config.setconfig(Config,Config.app)
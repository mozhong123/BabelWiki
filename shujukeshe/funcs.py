import pymysql
import datetime
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import json
import time
import requests
import os.path

def create_s_user():
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table s_user (id int (4)not null auto_increment PRIMARY KEY ,name  varchar(64)  not  null  unique ,password varchar(128) not null ,email varchar(64) not null unique not null,sex char(4) not null,c_time datetime not null,has_confirmed bool not null,code varchar(128) unique not null);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def create_s_confirm_user():
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table s_confirm_user (user_id int (4)not null unique PRIMARY KEY ,name varchar(" \
              "64) not null unique, birthday date not null,age int(4) not null,vip bool not null,FOREIGN KEY(name) REFERENCES s_user(name)on delete cascade on update cascade);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def send_email(email, code):  # 发送验证邮件
    subject = '来自www.zhaoyiqidashuaibi.com的注册确认邮件'
    text_content = '''感谢注册www.zhaoyiqidashuaibi.com\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
    html_content = '''
    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.zhaoyiqidashuaibi.com</a>，\
    这里是二次元的聚集地，专注于方舟内容的分享！</p>
    <p>请点击站点链接完成注册确认！</p>
    <p>此链接有效期为{}天！</p>
    '''.format('120.27.15.104:8000', code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def find_user_name(name):  # 根据名字查找
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from s_user where name = \'{name_value}\'limit 1;".format(name_value=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_user_email(email):  # 根据邮箱查找
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from s_user where email = \'{email_value}\'limit 1;".format(email_value=email)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_user_code(code):  # 根据确认码查找
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from s_user where code = \'{code_value}\'limit 1;".format(code_value=code)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_confirms_user_name(name):  # 根据用户名查找
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from s_confirm_user where name = \'{name_value}\'limit 1;".format(name_value=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def add_user(name, password, email, sex):  # 向s_user表中插入未注册的用户数据
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')

        cursor = db.cursor()
        #  进行插入
        sql = "insert into s_user(name, password, email, sex ,c_time , has_confirmed ,code) value"  "( \'{name}\', " \
              "\'{password}\', \'{email}\', \'{sex}\' ,\'{c_time}\',\'{has_confirmed}\',\'{code}\');".format(name=name,
                                                                                                             password=password,
                                                                                                             email=email,
                                                                                                             sex=sex,
                                                                                                             c_time=datetime.datetime.now(),
                                                                                                             has_confirmed=0,
                                                                                                             code=1)

        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_confirms_user(user_id, name):  # 向s_confirm_user表中插入已注册的用户数据
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')

        cursor = db.cursor()
        #  进行插入
        sql = "insert into s_confirm_user(user_id,name,birthday,age,vip) value"  "( \'{user_id}\',\'{name}\',\'{birthday}\',\'{age}\',\'{vip}\');".format(
            user_id=user_id, name=name, birthday="2003-01-01", age=20, vip=0)

        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def delete_user(name):  # 在s_user中删除该用户
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from s_user where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def delete_confirm_user(name):  # 在s_confirm_user中删除该用户
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from s_confirm_user where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_user_has_confirmed(name, has_confirmed):  # 更新用户注册信息
    try:
        if has_confirmed == 0:  # 若为注销用户
            delete_user(name)
            delete_confirm_user(name)
        else:  # 若为更新信息
            db = pymysql.connect(host='127.0.0.1', user='root',
                                 password='13278403012zhao', port=3306, db='sjk')
            cursor = db.cursor()
            sql = "update s_user set has_confirmed=\'{has_confirmed}\'   where name = \'{name}\';".format(
                has_confirmed=has_confirmed, name=name)
            cursor.execute(sql)
            db.commit()
            return True
    except Exception as e:
        return False


def update_user(id1, name, sex):  # 更改s_user的用户名与性别
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update s_user set name=\'{name}\', sex=\'{sex}\'  where id = \'{id1}\';".format(
            name=name, sex=sex, id1=id1)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_user_password(name, newpassword):  # 更改用户密码
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update s_user set password=\'{newpassword}\' where name = \'{name}\';".format(newpassword=newpassword,
                                                                                             name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_user_code(name, code):  # 更改s_user的code
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update s_user set  code=\'{code}\'  where name = \'{curname}\';".format(code=code, curname=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False

def update_user_operator_name(name, newname):
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "ALTER TABLE " + name + " rename " + newname + ";"
        cursor.execute(sql)  # 处理sql语句
        db.commit()
        return True
    except Exception as e:
        return None




def update_user_birthday(user_id, newbirthday):  # 更改用户生日
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update s_confirm_user set birthday=\'{newbirthday}\', age=\'{age}\' where user_id = \'{user_id}\';".format(
            newbirthday=newbirthday, age=int(datetime.date.today().__sub__(newbirthday).days) / 365, user_id=user_id)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_confirm_user_vip(name, vip):  # 更改用户生日
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update s_confirm_user set vip=\'{vip}\' where name = \'{name}\';".format(
            vip = vip, name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_token(name, token):  # 更改token
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update s_confirm_user set token=\'{token}\' where name = \'{name}\';".format(
            token=token, name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def saveJson(newDict, filename):
    saveList = []
    for ts, chars in newDict.items():
        saveList.append({'ts': ts, 'chars': chars})
    # 可选参数: indent = 4 (自动换行并设置缩进值为4)
    json.dump(saveList, open(filename, mode='w', encoding='utf-8'), ensure_ascii=False)


def card_record(token):
    page = 1
    newDict = {}
    while True:
        url = "https://ak.hypergryph.com/user/api/inquiry/gacha?page=" + str(page) + "&token=" + token
        res = requests.get(url)
        info = json.loads(res.text)['data']['list']
        if info:
            page += 1
            for ts_chars in info:
                ts = ts_chars['ts']
                chars = ts_chars['chars']
                newDict[ts] = chars
        else:
            break

    queryTs = time.time()
    newEnd = max(newDict.keys())
    newStart = min(newDict.keys())
    newLog = [{'queryTs': queryTs, 'Start_End': [newStart, newEnd], 'total': len(newDict)}]

    filename = 'Arknights.json'
    if os.path.isfile(filename):
        loadDict = {}
        with open(filename, 'r', encoding='utf-8') as loadFile:
            loadJson = json.load(loadFile)
        for ts_chars in loadJson:
            ts = ts_chars['ts']
            chars = ts_chars['chars']
            loadDict[ts] = chars

        loadEnd = max(loadDict.keys())
        loadStart = min(loadDict.keys())
        if (newEnd, newStart) == (loadEnd, loadStart):
            print("抽卡记录无更新信息")
        else:
            newDict.update(loadDict)
            saveJson(newDict, filename)
            with open('ArknightsQueryLog.json', 'r', encoding='utf-8') as loadFile:
                loadLogJson = json.load(loadFile)
            newLog.append(loadLogJson)
            json.dump(newLog, open('ArknightsQueryLog.json', mode='w', encoding='utf-8'), ensure_ascii=False)
    else:
        saveJson(newDict, filename)
        json.dump(newLog, open('ArknightsQueryLog.json', mode='w', encoding='utf-8'), ensure_ascii=False)

    infoList = []
    for ts, chars in newDict.items():
        ymdTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
        for char in chars:
            char_name = char['name']
            char_star = int(char['rarity']) + 1
            char_isNew = char['isNew']
            infoList.append(tuple([ts, ymdTime, char_name, char_star, char_isNew]))

    result = tuple(infoList)
    return result


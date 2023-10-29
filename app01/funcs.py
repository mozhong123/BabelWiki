import pymysql
import datetime
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def create_work_record():
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table work_record (id int (4)not null auto_increment PRIMARY KEY ,staff_id varchar(100) not null, staff_work varchar(50) not null, staff_optio varchar(10) not null, staff_name varchar(100) not null,staff_state varchar(100) not null,staff_time date not null,staff_introduction varchar(600) not null);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass

def create_work_manage():
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table work_manage (work_idx int (4)not null auto_increment PRIMARY KEY ,work_manage varchar(100) not null, work_type varchar(50) not null, work_conten varchar(100) not null, work_num int(4) not null);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def find_all_work_record():
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from work_record where staff_state = '成功提交申请' order by staff_time desc;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


def find_work_manage():
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from work_manage;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


def find_work_type(name):
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select distinct work_type from work_manage where work_manage = \'{work_manager}\';".format(
            work_manager=name)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


def find_name(idx):
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select work_manage from work_manage where work_idx = \'{work_idx}\';".format(
            work_idx=idx)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None


def find_work_record(staff_optio):
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select staff_id, staff_work, staff_optio, staff_name,staff_state,staff_introduction,id from work_record where staff_optio in ({}) and staff_state = '正在提交申请';".format(
            ','.join(["'%s'" % item for item in staff_optio]))
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None


def find_email_code(name):  # 查找管理员的email与code
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select email, code from s_user where name =  \'{name}\';".format(name=name)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None


def find_work_team(name):  # 查找该成员的work_team
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select work_team from s_confirm_user where name =  \'{name}\';".format(name=name)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None


def add_work_record(staff_id, staff_work, staff_optio, staff_name, staff_introduction):  # 向work_record表中插入提交的信息
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        #  进行插入
        sql = "insert into work_record(staff_id, staff_work, staff_optio, staff_name, staff_state, staff_time, staff_introduction) value"  "( \'{staff_id}\',\'{staff_work}\',\'{staff_optio}\',\'{staff_name}\',\'{staff_state}\',\'{staff_time}\',\'{staff_introduction}\');".format(
            staff_id=staff_id, staff_work=staff_work, staff_optio=staff_optio, staff_name=staff_name,
            staff_state='正在提交申请', staff_time=datetime.date.today(), staff_introduction=staff_introduction)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def send_email(email, name, code, idx):  # 发送验证邮件
    subject = '来自www.zhaoyiqidashuaibi.com的请求确认邮件'
    text_content = '''有一名小伙伴想加入到您的队伍中！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
    html_content = '''
    <p>有一名叫{}的小伙伴想要加入您的团队!</p>
    <p><a href="http://{}/apply_confirm/?code={}/?name={}/?idx={}" target=blank>www.zhaoyiqidashuaibi.com</a>，\
    若您同意请点击该链接批准！</p>
    <p><a href="http://{}/apply_confirm/?code={}/?name={}/?idx={}" target=blank>www.zhaoyiqidashuaibi.com</a>，\
    若您不同意请点击该链接拒绝！</p>
    
    '''.format(name, '120.27.15.104:8000', code, name, idx, '118.190.207.178:8000', 1, name, idx)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_apply_email(email, str1):  # 发送请求结果
    subject = '来自www.zhaoyiqidashuaibi.com的申请结果通知邮件'
    text_content = '''申请结果\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
    html_content = '''
    <p>{}</p>
    '''.format(str1)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_information_email(email, str1, str2):  # 发送提交结果
    subject = '来自www.zhaoyiqidashuaibi.com的提交结果通知邮件'
    text_content = '''提交结果\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''
    html_content = '''
    <p>{}</p>
    <p>{}</p>
    '''.format(str1, str2)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def update_user_work_team(name, team):  # 更改s_confirm_user的work_team
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update s_confirm_user set work_team=\'{team}\' where name = \'{name}\';".format(
            team=team, name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_work_num(idx):  # 更改work_manage的work_num
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update work_manage set work_num = work_num + 1 where work_idx = \'{idx}\';".format(
            idx=idx)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_work_num_decline(idx):  # 更改work_manage的work_num
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update work_manage set work_num = work_num - 1 where work_idx = \'{idx}\';".format(
            idx=idx)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_work_record(idx, str1):  # 更改work_record
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update work_record set staff_state = \'{str1}\' where id = \'{idx}\';".format(
            str1=str1, idx=idx)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False

def update_work_record_name(oldname, newname):  # 更改work_record的提交人名字
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update work_record set staff_id = \'{staff_id}\' where staff_id = \'{idx}\';".format(
            staff_id=newname, idx=oldname)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False

def update_work_manage_name(oldname, newname):  # 更改work_manage的提交人名字
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update work_manage set work_manage = \'{staff_id}\' where work_manage = \'{idx}\';".format(
            staff_id=newname, idx=oldname)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False
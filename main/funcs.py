import pymysql
import datetime
from django.conf import settings
import os
import random


def find_operator_clicks(name):  # 查找点击次数
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select clicks from operator where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回所有元组
    except Exception as e:
        return None


def find_max_operator_clicks():  # 查找最多点击次数
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name,clicks from operator order by clicks desc limit 1;"  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回所有元组
    except Exception as e:
        return None


def find_max_contributer():  # 查找最多贡献者
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "SELECT staff_id, count(1) FROM work_record where staff_state = \'{staff_state}\' group by staff_id order by count(1) desc limit 1;".format(
            staff_state='成功提交申请')
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_last_contributer():  # 查找昨日贡献者
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select staff_id, staff_work, staff_optio, staff_name from work_record where staff_state = \'{staff_state}\' and  DATEDIFF(staff_time,curdate())=-1 ;".format(
            staff_state='成功提交申请')  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取一个元组
        return result  # 返回所有元组
    except Exception as e:
        return None


def update_operator_clicks(name, clicks):  # 更新干员的点击次数
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update operator set  clicks=\'{clicks}\'  where name = \'{name}\';".format(clicks=clicks, name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def create_card_pool():  # 创建卡池表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table card_pool (id int (4)not null auto_increment PRIMARY KEY , name varchar(64) not null unique, avatar varchar(64)not null, begin datetime not null, end datetime not null, operator_name varchar(64)not null);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def create_enemy():  # 创建敌人表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table enemy (id int (4)not null auto_increment PRIMARY KEY , avatar varchar(64) not null, name varchar(" \
              "64) not null unique, position char(10) not  null , species char(10) not null, ability char(100), ATK varchar(8)not null, HP varchar(8)not null, DEF varchar(8)not null, SR varchar(8)not null, first_appear varchar(64)not null, index(first_appear));"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def find_all_enemy():  # 查找所有敌人
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select avatar, name, position, species,  ability , ATK , HP , DEF , SR, first_appear from enemy ;"  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回所有元组
    except Exception as e:
        return None


def create_Operator():  # 创建干员信息表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table operator (id int (4)not null auto_increment PRIMARY KEY , avatar varchar(64) not null, name varchar(" \
              "64) not null unique, career char(6) not  null , rarity char(6) not null, position char(10) not null, sex char(4)not null, retime varchar(8)not null, refair int(4)not null, block int(4)not null,   material varchar(100), quantity varchar(64), ATI varchar(8)not null, clicks int not null, index(career), index(sex), index(rarity));"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def create_talent():  # 创建干员天赋表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table talent (name varchar(64) PRIMARY KEY , talent_name1 varchar(48)not null, describe1 varchar(128)not null, talent_name2 varchar(48), describe2 varchar(128), FOREIGN KEY(name) REFERENCES operator(name) on delete cascade  on update cascade);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def create_potential():  # 创建干员潜能表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table potential (name varchar(64) PRIMARY KEY , potential2 varchar(64)not null, potential3 varchar(64)not null, potential4 varchar(64)not null, potential5 varchar(64)not null, potential6 varchar(64)not null,  FOREIGN KEY(name) REFERENCES operator(name) on delete cascade  on update cascade);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def create_skill():  # 创建干员技能表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table skill (name varchar(64) PRIMARY KEY , skill_name1 varchar(64)not null, skill_describe1 varchar(128)not null, initial1 int(4)not null, deplete1 int(4)not null, continued1 int(4)not null, skill_name2 varchar(64), skill_describe2 varchar(128), initial2 int(4), deplete2 int(4), continued2 int(4),  skill_name3 varchar(64), skill_describe3 varchar(128), initial3 int(4), deplete3 int(4), continued3 int(4),FOREIGN KEY(name) REFERENCES operator(name) on delete cascade  on update cascade);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def create_attribute():  # 创建干员属性表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table attribute (name varchar(64) PRIMARY KEY , HP1 int(4) not null, ATK1 int(4)not null, DEF1 int(4)not null, SR1 int(4)not null, HP2 int(4), ATK2 int(4), DEF2 int(4), SR2 int(4), HP3 int(4), ATK3 int(4), DEF3 int(4), SR3 int(4), HP4 int(4), ATK4 int(4), DEF4 int(4), SR4 int(4), FOREIGN KEY(name) REFERENCES operator(name) on delete cascade  on update cascade);"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def create_material():  # 创建材料表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table material (id int (4)not null auto_increment PRIMARY KEY , name varchar(64)not null unique, avatar varchar(64)not null, rarity varchar(10)not null, operator_used varchar(400)not null,  index(rarity));"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def create_level():  # 创建关卡表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table level (name varchar(64) PRIMARY KEY , type varchar(20) not null, combat_consumption int(4) not null, exercise_consumption int(4) not null, deploy_max int(4)not null, cost int(4) not null, cost_max int(4) not null, home_HP int(4) not null, enemy_amounts int(4) not null, first_drop varchar(20) not null, common_drop varchar(64) );"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def find_level_material():  # 查找关卡掉落的材料
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from level;"  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_material_information(name):  # 查找材料的名称与头像
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name,avatar from material where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_career(name):  # 查找干员的职业
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select career from operator where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator(list1, list2, list3):  # 查找干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        if len(list1) != 0 and len(list2) != 0 and len(list3) != 0:
            sql = "SELECT id,avatar,name, career, rarity, position, sex, retime, refair, block, ATI FROM operator WHERE career in ({}) and sex in ({}) and rarity in ({})".format(
                ','.join(["'%s'" % item for item in list1]), ','.join(["'%s'" % item for item in list2]),
                ','.join(["'%s'" % item for item in list3]))
            cursor.execute(sql)  # 处理sql语句

        elif len(list1) != 0 and len(list2) != 0 and len(list3) == 0:
            sql = "SELECT id,avatar,name, career, rarity, position, sex, retime, refair, block, ATI FROM operator WHERE career in ({}) and sex in ({})".format(
                ','.join(["'%s'" % item for item in list1]), ','.join(["'%s'" % item for item in list2]))
            cursor.execute(sql)  # 处理sql语句

        elif len(list1) != 0 and len(list2) == 0 and len(list3) == 0:
            sql = "SELECT id,avatar,name, career, rarity, position, sex, retime, refair, block, ATI FROM operator WHERE career in ({}) ".format(
                ','.join(["'%s'" % item for item in list1]))
            cursor.execute(sql)  # 处理sql语句

        elif len(list1) != 0 and len(list2) == 0 and len(list3) != 0:
            sql = "SELECT id,avatar,name, career, rarity, position, sex, retime, refair, block, ATI FROM operator WHERE career in ({}) and rarity  in ({})".format(
                ','.join(["'%s'" % item for item in list1]), ','.join(["'%s'" % item for item in list3]))
            cursor.execute(sql)  # 处理sql语句

        elif len(list1) == 0 and len(list2) != 0 and len(list3) != 0:
            sql = "SELECT id,avatar,name, career, rarity, position, sex, retime, refair, block, ATI FROM operator WHERE  sex in ({}) and rarity in ({})".format(
                ','.join(["'%s'" % item for item in list2]), ','.join(["'%s'" % item for item in list3]))
            cursor.execute(sql)  # 处理sql语句

        elif len(list1) == 0 and len(list2) != 0 and len(list3) == 0:
            sql = "SELECT id,avatar,name, career, rarity, position, sex, retime, refair, block, ATI FROM operator WHERE  sex in ({}) ".format(
                ','.join(["'%s'" % item for item in list2]))
            cursor.execute(sql)  # 处理sql语句

        elif len(list1) == 0 and len(list2) == 0 and len(list3) != 0:
            sql = "SELECT id,avatar,name, career, rarity, position, sex, retime, refair, block, ATI FROM operator WHERE  rarity in ({}) ".format(
                ','.join(["'%s'" % item for item in list3]))
            cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_operator_s(name):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select avatar,name,career,rarity,position,sex,retime,refair from operator where name = \'{name}\'limit 1;".format(
            name=name)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None


def create_gacha(name):  # 给每个用户创建抽卡表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = """CREATE TABLE  `%s`(
                         id INT NOT NULL AUTO_INCREMENT,
                         operator_name  varchar(30),
                         operator_rarity char(6),
                         time datetime,
                         PRIMARY KEY(id),
                         index(operator_name),
                         index(operator_rarity))
                         """ % name
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        pass


def find_operator_four():  # 查找四星干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "SELECT name FROM operator WHERE rarity = \'{rarity}\';".format(rarity='四星')
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_user_operator(name, rarity):  # 在用户表中查找各星干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "SELECT operator_name FROM  `%s` " % name + " WHERE operator_rarity = \'{rarity}\';".format(rarity=rarity)
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_operator_five():  # 查找五星干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "SELECT name FROM operator WHERE rarity = \'{rarity}\';".format(rarity='五星')
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_operator_six():  # 查找六星干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "SELECT name FROM operator WHERE rarity = \'{rarity}\';".format(rarity='六星')
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_gacha_operator_amounts(name, rarity):  # 查询抽到的干员数量
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "SELECT count(id) FROM `%s` " % name + "WHERE operator_rarity = '%s' " % rarity
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_gacha_operator_most(name):  # 查询出现次数最多的干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "SELECT operator_name, count(1) FROM `%s` group by operator_name order by count(1) desc limit 1;" % name
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_all_gacha_operator(name):  # 查询抽到的干员数量
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "SELECT operator_name,operator_rarity,time FROM `%s` " % name
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回元组
    except Exception as e:
        return None


def find_all_operator():  # 查找所有干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select id,avatar,name, career, rarity, position, sex, retime, refair, block, ATI from operator ;"  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回所有元组
    except Exception as e:
        return None


def find_material_avatar(name):  # 查找干员的升级材料的头像
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select avatar from material where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_exist_operator(name):  # 查找干员是否存在
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name from operator where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_exist_material(name):  # 查找材料是否存在
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name from material where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_exist_level(name):  # 查找关卡是否存在
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name from level where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_exist_card_pool(name):  # 查找卡池是否存在
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name from card_pool where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_exist_enemy(name):  # 查找敌人是否存在
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name from enemy where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_material(name):  # 查找干员所需材料及数量
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select material, quantity from operator where name = \'{name}\' limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def add_level(name, type1, combat_consumption, exercise_consumption, deploy_max, cost, cost_max, home_HP, enemy_amounts,
              common_drop):  # 添加关卡
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into level(name, type, combat_consumption, exercise_consumption, deploy_max, cost, cost_max, home_HP, enemy_amounts, first_drop, common_drop) value"  "( \'{name}\', " \
              "\'{type1}\',\'{combat_consumption}\', \'{exercise_consumption}\', \'{deploy_max}\', \'{cost}\', \'{cost_max}\', \'{home_HP}\', \'{enemy_amounts}\', \'{first_drop}\', \'{common_drop}\');".format(
            name=name,
            type1=type1,
            combat_consumption=combat_consumption,
            exercise_consumption=exercise_consumption,
            deploy_max=deploy_max,
            cost=cost,
            cost_max=cost_max,
            home_HP=home_HP,
            enemy_amounts=enemy_amounts,
            first_drop='stone',
            common_drop=common_drop
        )
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_material(name, avatar, rarity, operator_used):  # 添加材料
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into material(name, avatar, rarity, operator_used) value"  "( \'{name}\', " \
              "\'{avatar}\', \'{rarity}\', \'{operator_used}\');".format(
            name=name,
            avatar=avatar,
            rarity=rarity,
            operator_used=operator_used)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_card_pool(name, avatar, begin, end, operator_name):  # 添加卡池
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into card_pool(name, avatar, begin, end, operator_name) value"  "( \'{name}\', " \
              "\'{avatar}\', \'{begin}\',\'{end}\', \'{operator_name}\');".format(
            name=name,
            avatar=avatar,
            begin=begin,
            end=end,
            operator_name=operator_name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_enemy(avatar, name, position, species, ability, ATK, HP, DEF, SR, first_appear):  # 添加敌人
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into enemy(avatar, name, position, species, ability, ATK, HP, DEF, SR, first_appear) value"  "( \'{avatar}\', " \
              "\'{name}\', \'{position}\',\'{species}\', \'{ability}\', \'{ATK}\', \'{HP}\', \'{DEF}\', \'{SR}\', \'{first_appear}\');".format(
            avatar=avatar,
            name=name,
            position=position,
            species=species,
            ability=ability,
            ATK=ATK,
            HP=HP,
            DEF=DEF,
            SR=SR,
            first_appear=first_appear)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def delete_material(name):  # 删除材料
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from material where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True

    except Exception as e:
        return False


def delete_level(name):  # 删除关卡
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from level where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def delete_enemy(name):  # 删除敌人
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from enemy where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def delete_card_pool(name):  # 删除卡池
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from card_pool where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def find_operator_later_information(name):  # 查找干员retime等信息
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select retime,refair,block,ATI from operator where name = \'{name}\' limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_attribute_former(name):  # 查找干员HP等信息
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select HP1,ATK1,DEF1,SR1 from attribute where name = \'{name}\' limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_material_rarity(rarity):  # 根据稀有度查找材料
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name,avatar from material where rarity in ({});".format(
            ','.join(["'%s'" % item for item in rarity]))  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回全部元组
    except Exception as e:
        return None


def find_material_all():  # 根据稀有度查找材料
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name,avatar from material;"  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回全部元组
    except Exception as e:
        return None


def find_material_operator_used(name):  # 查找需要该材料的干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select operator_used from material where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_name_avatar(name):  # 查找干员姓名及头像
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name,avatar from operator where name = \'{name}\' limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_attribute_all_former():  # 查找干员HP等信息
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select HP1,ATK1,DEF1,SR1 from attribute ;"  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        raise e
        return None


def find_operator_attribute(name):  # 查找干员属性
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from attribute where name = \'{name}\' limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_later_information(name):  # 查找干员retime等信息
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select retime,refair,block,ATI from operator where name = \'{name}\' limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 取一个元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_talent(name):  # 查找干员的天赋
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from talent where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_potential(name):  # 查找干员的潜能
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from potential where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_skill(name):  # 查找干员的技能
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select * from skill where name = \'{name}\'limit 1;".format(name=name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchone()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_card_pool_information():  # 查找卡池的基本信息
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select name, avatar, begin, end, operator_name from card_pool;"  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部
        return result  # 返回全部元组
    except Exception as e:
        return None


def add_operator(name, avatar, career, rarity, position, sex, retime, refair, block, material, quantity, ATI):  # 添加干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into operator(name, avatar, career, rarity, position, sex , retime, refair, block, material, quantity," \
              "ATI, clicks) value"  "( \'{name}\', " \
              "\'{avatar}\', \'{career}\', \'{rarity}\', \'{position}\' ,\'{sex}\'," \
              "\'{retime}\',\'{refair}\',\'{block}\',\'{material}\',\'{quantity}\',\'{ATI}\',\'{clicks}\');".format(
            name=name,
            avatar=avatar,
            career=career,
            rarity=rarity,
            position=position,
            sex=sex,
            retime=retime,
            refair=refair,
            block=block,
            material=material,
            quantity=quantity,
            ATI=ATI,
            clicks=0)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_attribute(name, HP1, ATK1, DEF1, SR1, HP2, ATK2, DEF2, SR2, HP3, ATK3, DEF3, SR3, HP4, ATK4, DEF4,
                  SR4):  # 添加干员的属性
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into attribute(name, HP1, ATK1, DEF1, SR1, HP2, ATK2, DEF2, SR2, HP3, ATK3, DEF3, SR3, HP4, ATK4, DEF4, SR4) value"  "( \'{name}\', " \
              "\'{HP1}\', \'{ATK1}\', \'{DEF1}\', \'{SR1}\' ,\'{HP2}\', \'{ATK2}\', \'{DEF2}\', \'{SR2}\',\'{HP3}\', \'{ATK3}\', \'{DEF3}\', \'{SR3}\',\'{HP4}\', \'{ATK4}\', \'{DEF4}\', \'{SR4}\');".format(
            name=name,
            HP1=HP1,
            ATK1=ATK1,
            DEF1=DEF1,
            SR1=SR1,
            HP2=HP2,
            ATK2=ATK2,
            DEF2=DEF2,
            SR2=SR2,
            HP3=HP3,
            ATK3=ATK3,
            DEF3=DEF3,
            SR3=SR3,
            HP4=HP4,
            ATK4=ATK4,
            DEF4=DEF4,
            SR4=SR4)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_skill(name, skill_name1, skill_describe1, initial1, deplete1, continued1, skill_name2, skill_describe2,
              initial2, deplete2, continued2, skill_name3, skill_describe3, initial3, deplete3, continued3):  # 添加干员的技能
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into skill(name, skill_name1, skill_describe1, initial1, deplete1, continued1, skill_name2, skill_describe2, initial2, deplete2, continued2,skill_name3, skill_describe3, initial3, deplete3, continued3) value"  "( \'{name}\', " \
              "\'{skill_name1}\', \'{skill_describe1}\', \'{initial1}\', \'{deplete1}\' ,\'{continued1}\',\'{skill_name2}\', \'{skill_describe2}\', \'{initial2}\', \'{deplete2}\' ,\'{continued2}\',\'{skill_name3}\', \'{skill_describe3}\', \'{initial3}\', \'{deplete3}\' ,\'{continued3}\');".format(
            name=name,
            skill_name1=skill_name1,
            skill_describe1=skill_describe1,
            initial1=initial1,
            deplete1=deplete1,
            continued1=continued1,
            skill_name2=skill_name2,
            skill_describe2=skill_describe2,
            initial2=initial2,
            deplete2=deplete2,
            continued2=continued2,
            skill_name3=skill_name3,
            skill_describe3=skill_describe3,
            initial3=initial3,
            deplete3=deplete3,
            continued3=continued3)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_talent(name, talent_name1, describe1, talent_name2, describe2):  # 添加干员的天赋
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into talent(name, talent_name1, describe1, talent_name2, describe2) value"  "( \'{name}\', " \
              "\'{talent_name1}\', \'{describe1}\', \'{talent_name2}\', \'{describe2}\');".format(
            name=name,
            talent_name1=talent_name1,
            describe1=describe1,
            talent_name2=talent_name2,
            describe2=describe2)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_potential(name, potential2, potential3, potential4, potential5, potential6):  # 添加干员的潜能
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into potential(name, potential2, potential3, potential4, potential5, potential6) value"  "( \'{name}\', " \
              "\'{potential2}\', \'{potential3}\', \'{potential4}\', \'{potential5}\', \'{potential6}\');".format(
            name=name,
            potential2=potential2,
            potential3=potential3,
            potential4=potential4,
            potential5=potential5,
            potential6=potential6)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def update_operator(id1, name, career, rarity, position, sex, retime, refair, block, ATI):  # 更改干员信息
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update operator set name = \'{name}\', career=\'{career}\', rarity=\'{rarity}\', position=\'{position}\', sex=\'{sex}\' , " \
              "retime=\'{retime}\', refair=\'{refair}\', " \
              "block=\'{block}\',ATI=\'{ATI}\' where id=\'{id1}\';".format(
            name=name,
            career=career,
            rarity=rarity,
            position=position,
            sex=sex,
            retime=retime,
            refair=refair,
            block=block,
            ATI=ATI,
            id1=id1)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def delete_operator(name):  # 删除干员
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from operator where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True

    except Exception as e:
        return False


def delete_attribute(name):  # 删除干员的属性
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from attribute where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True

    except Exception as e:
        return False


def delete_talent(name):  # 删除干员的天赋
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from talent where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True

    except Exception as e:
        return False


def delete_skill(name):  # 删除干员的技能
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from skill where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True

    except Exception as e:
        return False


def delete_potential(name):  # 删除干员的潜能
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "delete from potential where name = \'{name}\';".format(name=name)
        cursor.execute(sql)
        db.commit()
        return True

    except Exception as e:
        return False


def handle_uploaded_file_operator(f, name, rare):  # 读取上传文件
    now_path = os.path.dirname(__file__)
    s_path = 'static/main/image/' + rare + '/' + name + '.png'
    with open(os.path.join(now_path, s_path), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_file_material(f, name, rare):  # 读取上传文件
    now_path = os.path.dirname(__file__)
    s_path = 'static/main/image/material/' + rare + '/' + name + '.png'
    with open(os.path.join(now_path, s_path), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_file_enemy(f, name):  # 读取上传文件
    now_path = os.path.dirname(__file__)
    s_path = 'static/main/image/enemy/' + name + '.png'
    with open(os.path.join(now_path, s_path), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_file_pool(f, name):  # 读取上传文件
    now_path = os.path.dirname(__file__)
    s_path = 'static/main/image/pool/' + name + '.jpg'
    with open(os.path.join(now_path, s_path), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def handle_uploaded_file_others(f, name):  # 读取上传文件
    now_path = os.path.dirname(__file__)
    s_path = 'static/main/image/others/' + name + '.jpg'
    with open(os.path.join(now_path, s_path), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def create_comment():  # 创建讨论区表
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "create table comment (id int (4)not null auto_increment PRIMARY KEY , user_name varchar(64) not null, operator_name varchar(64) not null, comment  varchar(600) not null, comment_time datetime not null , pre_comment_id int(4), index(user_name), index(operator_name), index(pre_comment_id ));"  # sql语句
        cursor.execute(sql)  # 处理sql语句
    except Exception as e:
        pass


def find_operator_comment(operator_name):  # 查找干员对应的评论
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select  user_name, comment, comment_time, pre_comment_id from comment where operator_name = \'{name}\';".format(
            name=operator_name)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 单个取元组
        return result  # 返回一个元组
    except Exception as e:
        return None


def find_operator_pre_comment(id1):  # 查找干员对应的评论的回复评论
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "select  user_name, comment from comment where id = \'{id1}\';".format(id1=id1)  # sql语句
        cursor.execute(sql)  # 处理sql语句
        result = cursor.fetchall()  # 取全部元组
        return result  # 返回全部元组
    except Exception as e:
        return None


def update_comment(id1):  # 更新用户评论
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "update comment set comment=\'{comment}\'   where id = \'{id1}\';".format(
            comment='评论已删除', id1=id1)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_comment(user_name, operator_name, comment, comment_time, pre_comment_id):  # 添加评论
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        sql = "insert into comment(user_name, operator_name, comment, comment_time, pre_comment_id) value"  "( \'{user_name}\', " \
              "\'{operator_name}\', \'{comment}\', \'{comment_time}\', \'{pre_comment_id}\');".format(
            user_name=user_name,
            operator_name=operator_name,
            comment=comment,
            comment_time=comment_time,
            pre_comment_id=pre_comment_id)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False

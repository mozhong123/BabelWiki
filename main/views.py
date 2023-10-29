import numpy as np
from django.shortcuts import render
from django.shortcuts import redirect
from . import funcs
import json
import datetime
import pymysql
import random

four = list(funcs.find_operator_four())
five = list(funcs.find_operator_five())
six = list(funcs.find_operator_six())


# Create your views here.
def operator(request):
    funcs.create_Operator()
    if not request.session.get('is_login', None):
        return redirect('/login/')
    list1 = []
    list2 = []
    list3 = []
    job_pioneer = request.GET.get('jobs_pioneer', '')
    job_guards = request.GET.get('jobs_guards', '')
    job_sniper = request.GET.get('jobs_sniper', '')
    job_armor = request.GET.get('jobs_armor', '')
    job_doctor = request.GET.get('jobs_doctor', '')
    job_support = request.GET.get('jobs_support', '')
    job_warlock = request.GET.get('jobs_warlock', '')
    job_special = request.GET.get('jobs_special', '')
    sex_male = request.GET.get('sex_male', '')
    sex_female = request.GET.get('sex_female', '')
    rare_six = request.GET.get('rare_six', '')
    rare_five = request.GET.get('rare_five', '')
    rare_four = request.GET.get('rare_four', '')
    jobs_pioneer = job_pioneer
    jobs_guards = job_guards
    jobs_sniper = job_sniper
    jobs_armor = job_armor
    jobs_doctor = job_doctor
    jobs_support = job_support
    jobs_warlock = job_warlock
    jobs_special = job_special
    sex_male_ = sex_male
    sex_female_ = sex_female
    rare_five_ = rare_five
    rare_six_ = rare_six
    rare_four_ = rare_four
    if job_pioneer == '' and job_sniper == '' and job_armor == '' and job_sniper == '' and job_doctor == '' and job_guards == '' and job_special == '' and job_support == '' and job_warlock == '' and sex_female == '' and sex_male == '' and rare_five == '' and rare_four == '' and rare_six == '':
        result = funcs.find_all_operator()
        result = list(result)
        rows = len(result)
        result1 = funcs.find_operator_attribute_all_former()
        result1 = list(result1)
        for i in range(rows):
            result[i] = list(result[i])
            for j in range(4):
                if i<len(result1) and  j<len(result1[i]):
                    result[i].insert(7 + j, result1[i][j])
        result = tuple(result)

    else:
        if job_pioneer != '':
            job_pioneer = '先锋'
            jobs_pioneer = '先锋'
            job_pioneer = (job_pioneer + '1').split('1')
            list1 = list1 + job_pioneer
            del list1[-1]

        if job_guards != '':
            job_guards = '近卫'
            jobs_guards = '近卫'
            job_guards = (job_guards + '1').split('1')
            list1 = list1 + job_guards
            del list1[-1]

        if job_sniper != '':
            job_sniper = '狙击'
            jobs_sniper = '狙击'
            job_sniper = (job_sniper + '1').split('1')
            list1 = list1 + job_sniper
            del list1[-1]

        if job_armor != '':
            job_armor = '重装'
            jobs_armor = '重装'
            job_armor = (job_armor + '1').split('1')
            list1 = list1 + job_armor
            del list1[-1]

        if job_doctor != '':
            job_doctor = '医疗'
            jobs_doctor = '医疗'
            job_doctor = (job_doctor + '1').split('1')
            list1 = list1 + job_doctor
            del list1[-1]

        if job_support != '':
            job_support = '辅助'
            jobs_support = '辅助'
            job_support = (job_support + '1').split('1')
            list1 = list1 + job_support
            del list1[-1]

        if job_warlock != '':
            job_warlock = '术士'
            jobs_warlock = '术士'
            job_warlock = (job_warlock + '1').split('1')
            list1 = list1 + job_warlock
            del list1[-1]

        if job_special != '':
            job_special = '特种'
            jobs_special = '特种'
            job_special = (job_special + '1').split('1')
            list1 = list1 + job_special
            del list1[-1]

        if sex_male != '':
            sex_male = '男'
            sex_male_ = '男'
            sex_male = (sex_male + '1').split('1')
            list2 = list2 + sex_male
            del list2[-1]

        if sex_female != '':
            sex_female = '女'
            sex_female_ = '女'
            sex_female = (sex_female + '1').split('1')
            list2 = list2 + sex_female
            del list2[-1]

        if rare_six != '':
            rare_six = '六星'
            rare_six_ = '六星'
            rare_six = (rare_six + '1').split('1')
            list3 = list3 + rare_six
            del list3[-1]

        if rare_five != '':
            rare_five = '五星'
            rare_five_ = '五星'
            rare_five = (rare_five + '1').split('1')
            list3 = list3 + rare_five
            del list3[-1]

        if rare_four != '':
            rare_four = '四星'
            rare_four_ = '四星'
            rare_four = (rare_four + '1').split('1')
            list3 = list3 + rare_four
            del list3[-1]
        if list1 == '' and list2 == '' and list3 == '':
            pass
        else:
            result = funcs.find_operator(list1, list2, list3)
            result = list(result)
            rows = len(result)
            for i in range(rows):
                result1 = funcs.find_operator_attribute_former(result[i][2])
                result1 = list(result1)
                result[i] = list(result[i])
                for j in range(4):
                    result[i].insert(7 + j, result1[j])
            result = tuple(result)

    return render(request, 'main/operator.html',
                  {'result': json.dumps(result), 'job_pioneer': jobs_pioneer, 'job_guards': jobs_guards,
                   'job_sniper': jobs_sniper, 'job_armor': jobs_armor, 'job_doctor': jobs_doctor,
                   'job_support': jobs_support, 'job_warlock': jobs_warlock, 'job_special': jobs_special,
                   'sex_male': sex_male_, 'sex_female': sex_female_, 'rare_six': rare_six_, 'rare_five': rare_five_,
                   'rare_four': rare_four_})


def gacha(request):  # 抽卡主界面
    if not request.session.get('is_login', None):
        return redirect('/login/')
    name = request.session['user_name']
    funcs.create_gacha(name)
    return render(request, 'main/pool_draw.html')


def gacha_choice(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'main/pool_choice.html')


def gacha_add_one(request):  # 抽卡一次
    if not request.session.get('is_login', None):
        return redirect('/login/')
    name = request.session['user_name']
    np.random.seed(0)
    p = np.array([0.64, 0.26, 0.10])
    index = np.random.choice([4, 5, 6], p=p.ravel())
    try:
        db = pymysql.connect(host='127.0.0.1', user='root',
                             password='13278403012zhao', port=3306, db='sjk')
        cursor = db.cursor()
        if index == 4:
            result = list(random.choice(four))
            sql = 'insert into %s(operator_name,operator_rarity,time)' % name + ' value (%s,%s,%s)'
            cursor.execute(sql, [result, '四星', datetime.datetime.now()])
        elif index == 5:
            result = list(random.choice(five))
            sql = 'insert into %s(operator_name,operator_rarity,time)' % name + ' value (%s,%s,%s)'
            cursor.execute(sql, [result, '五星', datetime.datetime.now()])
        elif index == 6:
            result = list(random.choice(six))
            sql = 'insert into %s(operator_name,operator_rarity,time)' % name + ' value (%s,%s,%s)'
            cursor.execute(sql, [result, '六星', datetime.datetime.now()])
        db.commit()
    except Exception as e:
        pass
    result_pool = funcs.find_operator_s(result[0])
    manages = []
    data = {
        'avatar': result_pool[0],
        'name': result_pool[1],
        'career': result_pool[2],
        'rarity': result_pool[3],
        'position': result_pool[4],
        'sex': result_pool[5],
        'retime': result_pool[6],
        'refair': result_pool[7],
    }
    manages.append(data)
    return render(request, 'main/draw_one.html', {'manages': manages})


def gacha_add_ten(request):  # 抽卡十次
    if not request.session.get('is_login', None):
        return redirect('/login/')
    name = request.session['user_name']
    np.random.seed(0)
    p = np.array([0.64, 0.26, 0.10])
    ans = []
    for i in range(10):
        index = np.random.choice([4, 5, 6], p=p.ravel())
        try:
            db = pymysql.connect(host='127.0.0.1', user='root',
                                 password='13278403012zhao', port=3306, db='sjk')
            cursor = db.cursor()
            if index == 4:
                result = list(random.choice(four))
                ans = ans + result
                sql = 'insert into %s(operator_name,operator_rarity,time)' % name + ' value (%s,%s,%s)'
                cursor.execute(sql, [result, '四星', datetime.datetime.now()])
            elif index == 5:
                result = list(random.choice(five))
                ans = ans + result
                sql = 'insert into %s(operator_name,operator_rarity,time)' % name + ' value (%s,%s,%s)'
                cursor.execute(sql, [result, '五星', datetime.datetime.now()])
            elif index == 6:
                result = list(random.choice(six))
                ans = ans + result
                sql = 'insert into %s(operator_name,operator_rarity,time)' % name + ' value (%s,%s,%s)'
                cursor.execute(sql, [result, '六星', datetime.datetime.now()])
            db.commit()
        except Exception as e:
            pass
    manages = []
    for i in range(10):
        result_pool = funcs.find_operator_s(ans[i])
        data = {
            'avatar': result_pool[0],
            'name': result_pool[1],
            'career': result_pool[2],
            'rarity': result_pool[3],
            'position': result_pool[4],
            'sex': result_pool[5],
            'retime': result_pool[6],
            'refair': result_pool[7],
        }
        manages.append(data)
    return render(request, 'main/draw_ten.html', {'manages': manages})


def gacha_analyse(request):  # 抽卡分析
    if not request.session.get('is_login', None):
        return redirect('/login/')
    name = request.session['user_name']

    four = list(funcs.find_gacha_operator_amounts(name, '四星'))  # 四星数量
    five = list(funcs.find_gacha_operator_amounts(name, '五星'))  # 五星数量
    six = list(funcs.find_gacha_operator_amounts(name, '六星'))  # 六星数量

    four[0] = list(four[0])
    five[0] = list(five[0])
    six[0] = list(six[0])
    sum = four[0][0] + five[0][0] + six[0][0]
    four_percent = round(four[0][0] / sum, 4)
    five_percent = round(five[0][0] / sum, 4)
    six_percent = round(six[0][0] / sum, 4)

    ans = list(funcs.find_gacha_operator_most(name))
    operator_name = list(ans[0])

    amounts = funcs.find_gacha_operator_most(name)[1]
    percent = round(amounts / sum, 4)

    result = []
    result.append(four[0][0])
    result.append(four_percent * 100)
    result.append(five[0][0])
    result.append(five_percent * 100)
    result.append(six[0][0])
    result.append(six_percent * 100)
    result = result + operator_name
    result.append(percent * 100)
    return render(request, 'main/analysis_star.html', {'result': result})


def gacha_analyse_operator(request):  # 抽卡分析
    if not request.session.get('is_login', None):
        return redirect('/login/')
    name = request.session['user_name']
    result = []
    four1 = list(funcs.find_user_operator(name, '四星'))
    five1 = list(funcs.find_user_operator(name, '五星'))
    six1 = list(funcs.find_user_operator(name, '六星'))
    four_xianfeng = 0
    four_jinwei = 0
    four_juji = 0
    four_zhongzhuang = 0
    four_yiliao = 0
    four_fuzhu = 0
    four_shushi = 0
    five_xianfeng = 0
    five_jinwei = 0
    five_juji = 0
    five_zhongzhuang = 0
    five_yiliao = 0
    five_fuzhu = 0
    five_shushi = 0
    six_xianfeng = 0
    six_jinwei = 0
    six_juji = 0
    six_zhongzhuang = 0
    six_yiliao = 0
    six_fuzhu = 0
    six_shushi = 0
    for i in range(len(four1)):
        t = funcs.find_operator_career(four1[i][0])
        if t[0] == '先锋':
            four_xianfeng = four_xianfeng + 1
        elif t[0] == '近卫':
            four_jinwei = four_jinwei + 1
        elif t[0] == '狙击':
            four_juji = four_juji + 1
        elif t[0] == '重装':
            four_zhongzhuang = four_zhongzhuang + 1
        elif t[0] == '医疗':
            four_yiliao = four_yiliao + 1
        elif t[0] == '辅助':
            four_fuzhu = four_fuzhu + 1
        elif t[0] == '术士':
            four_shushi = four_shushi + 1
    for i in range(len(five1)):
        t = funcs.find_operator_career(five1[i][0])
        if t[0] == '先锋':
            five_xianfeng = five_xianfeng + 1
        elif t[0] == '近卫':
            five_jinwei = five_jinwei + 1
        elif t[0] == '狙击':
            five_juji = five_juji + 1
        elif t[0] == '重装':
            five_zhongzhuang = five_zhongzhuang + 1
        elif t[0] == '医疗':
            five_yiliao = five_yiliao + 1
        elif t[0] == '辅助':
            five_fuzhu = five_fuzhu + 1
        elif t[0] == '术士':
            five_shushi = five_shushi + 1
    for i in range(len(six1)):
        t = funcs.find_operator_career(six1[i][0])
        if t[0] == '先锋':
            six_xianfeng = six_xianfeng + 1
        elif t[0] == '近卫':
            six_jinwei = six_jinwei + 1
        elif t[0] == '狙击':
            six_juji = six_juji + 1
        elif t[0] == '重装':
            six_zhongzhuang = six_zhongzhuang + 1
        elif t[0] == '医疗':
            six_yiliao = six_yiliao + 1
        elif t[0] == '辅助':
            six_fuzhu = six_fuzhu + 1
        elif t[0] == '术士':
            six_shushi = six_shushi + 1

    result.append(four_xianfeng)
    result.append(four_jinwei)
    result.append(four_juji)
    result.append(four_zhongzhuang)
    result.append(four_yiliao)
    result.append(four_fuzhu)
    result.append(four_shushi)
    result.append(five_xianfeng)
    result.append(five_jinwei)
    result.append(five_juji)
    result.append(five_zhongzhuang)
    result.append(five_yiliao)
    result.append(five_fuzhu)
    result.append(five_shushi)
    result.append(six_xianfeng)
    result.append(six_jinwei)
    result.append(six_juji)
    result.append(six_zhongzhuang)
    result.append(six_yiliao)
    result.append(six_fuzhu)
    result.append(six_shushi)

    return render(request, 'main/analysis_operater.html', {'result': result,'name': name})


def gacha_record(request):  # 抽卡记录
    if not request.session.get('is_login', None):
        return redirect('/login/')
    name = request.session['user_name']
    result = funcs.find_all_gacha_operator(name)
    manages = []
    for i in range(len(result)):
        result_pool = funcs.find_operator_s(result[i][0])
        data = {
            'avatar': result_pool[0],
            'name': result_pool[1],
            'career': result_pool[2],
            'rarity': result_pool[3],
            'position': result_pool[4],
            'sex': result_pool[5],
            'retime': result_pool[6],
            'refair': result_pool[7],
        }
        manages.append(data)
    return render(request, 'main/draw_record.html', {'manages': manages, 'result': result})


def enemy(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    result = funcs.find_all_enemy()
    return render(request, 'main/enemy.html', {'result': json.dumps(result)})


def operator_W(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    clicks = list(funcs.find_operator_clicks('W'))
    clicks = clicks[0] + 1
    funcs.update_operator_clicks('W', clicks)
    result = funcs.find_operator_material('W')
    name = result[0].split(',')  # 将材料名分隔开
    nums = result[1].split(',')  # 将材料数量分隔开
    rows = len(name)
    result = [[0] * 3 for i in range(rows)]
    for i in range(rows):
        avatar = funcs.find_material_avatar(name[i])
        avatar = list(avatar)
        res = name[i] + ',' + str(nums[i])
        res = res.split(',')
        res = avatar + res
        result[i] = res
    result_material = tuple(result)
    result_attribute_grow = funcs.find_operator_attribute('W')
    result_attribute_fixed = funcs.find_operator_later_information('W')
    result_talent = funcs.find_operator_talent('W')
    result_potencial = funcs.find_operator_potential('W')
    result_skill = funcs.find_operator_skill('W')
    comments = list(funcs.find_operator_comment('W'))
    rows = len(comments)
    for i in range(rows):
        comments[i] = list(comments[i])
        comments[i][2] = str(comments[i][2])
        if (comments[i][3] != ''):
            pre_comment1 = list(funcs.find_operator_pre_comment(int(comments[i][3])))
            del comments[i][-1]
            rows1 = len(pre_comment1)
            for j in range(rows1):
                pre_comment1[j] = list(pre_comment1[j])
                comments[i] = comments[i] + pre_comment1[j]
        else:
            del comments[i][-1]
            comments[i] = comments[i] + [''] + ['']
    comments = tuple(comments)
    print(comments)
    if request.method == 'POST':
        first_comment = request.POST.get('first_comment', '')
        pre_comment = request.POST.get('reply_comment', '')
        if first_comment != '':
            user_name = request.session['user_name']
            operator_name = 'W'
            comment = first_comment
            comment_time = datetime.datetime.now()
            pre_comment_id = ''
            funcs.add_comment(user_name, operator_name, comment, comment_time, pre_comment_id)
            return redirect('/operator/W/')
        else:
            user_name = request.session['user_name']
            operator_name = 'W'
            comment = pre_comment
            comment_time = datetime.datetime.now()
            pre_comment_id = int(request.POST.get('id', ''))
            funcs.add_comment(user_name, operator_name, comment, comment_time, pre_comment_id)
            return redirect('/operator/W/')

    if request.method == 'GET':
        delete_id = request.GET.get('delete_id', '')
        if delete_id != '':
            funcs.update_comment(int(delete_id))
            return redirect('/operator/W/')
    return render(request, 'main/operator/W.html',
                  {'result_1': json.dumps(result_attribute_grow), 'result_2': json.dumps(result_attribute_fixed),
                   'result_3': json.dumps(result_material), 'result_4': json.dumps(result_talent),
                   'result_5': json.dumps(result_potencial), 'result_6': json.dumps(result_skill),
                   'comments': json.dumps(comments)})


def material(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    rare_four = request.GET.get('rare_four', '')
    rare_three = request.GET.get('rare_three', '')
    rare_four_ = rare_four
    rare_three_ = rare_three
    if rare_four == '' and rare_three == '':
        result = funcs.find_material_all()
    else:
        result = []
        if rare_three != '':
            rare_three = '三星'
            rare_three_ = '三星'
            rare_three = (rare_three + '1').split('1')
            result = result + rare_three
            del result[-1]

        if rare_four != '':
            rare_four = '四星'
            rare_four_ = '四星'
            rare_four = (rare_four + '1').split('1')
            result = result + rare_four
            del result[-1]
        result = funcs.find_material_rarity(result)
        result = tuple(result)
    return render(request, 'main/material.html',
                  {'result': json.dumps(result), 'rare_four': rare_four_, 'rare_three': rare_three_})


def material_shuangjinamipian(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    result = funcs.find_material_operator_used('双极纳米片')
    result = result[0].split(',')
    rows = len(result)
    ans = [[0] * 2 for i in range(rows)]
    for i in range(rows):
        res = funcs.find_operator_name_avatar(result[i])
        ans[i] = res
    ans = tuple(ans)
    return render(request, 'main/material/双极纳米片.html', {'result': json.dumps(ans)})


def material_tongzhenlie(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    result = funcs.find_material_operator_used('酮阵列')
    result = result[0].split(',')
    rows = len(result)
    ans = [[0] * 2 for i in range(rows)]
    for i in range(rows):
        res = funcs.find_operator_name_avatar(result[i])
        ans[i] = res
    ans = tuple(ans)
    return render(request, 'main/material/酮阵列.html', {'result': json.dumps(ans)})


def material_D32gang(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    result = funcs.find_material_operator_used('D32钢')
    result = result[0].split(',')
    rows = len(result)
    ans = [[0] * 2 for i in range(rows)]
    for i in range(rows):
        res = funcs.find_operator_name_avatar(result[i])
        ans[i] = res
    ans = tuple(ans)
    return render(request, 'main/material/D32钢.html', {'result': json.dumps(ans)})


def level(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    result = list(funcs.find_level_material())
    rows = len(result)
    for i in range(rows):
        result[i] = list(result[i])
        common_drop = list(funcs.find_material_information(result[i][10]))
        del result[i][-1]
        del result[i][-1]
        result[i] = result[i] + common_drop
    result = tuple(result)
    return render(request, 'main/level.html', {'result': json.dumps(result)})


def pool(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    result = list(funcs.find_card_pool_information())
    rows = len(result)
    for i in range(rows):
        result[i] = list(result[i])
        operator = str(result[i][4]).split(',')
        rows1 = len(operator)
        del result[i][-1]
        for j in range(rows1):
            information = list(funcs.find_operator_name_avatar(operator[j]))
            result[i] = result[i] + information
        result[i][2] = str(result[i][2])
        result[i][3] = str(result[i][3])
    result = tuple(result)
    print(result)
    return render(request, 'main/pool.html', {'result': json.dumps(result)})

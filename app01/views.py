import datetime
import pandas as pd
from django.conf import settings
from django.shortcuts import render, redirect
from . import funcs
from main import funcs as funcs_main
from django.contrib import messages


# Create your views here.
def record(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    funcs.create_work_record()
    result = funcs.find_all_work_record()
    workers, idx = [], 1
    for i in result:
        i = list(i)
        if i[2] == '创建表单':
            i[2] = '创建'
        elif i[2] == '修改表单':
            i[2] = '修改'
        data = {'idx': idx,
                'staff_work_type': i[2],
                'staff_option': i[3],
                'staff_state': i[5],
                'staff_time': i[6],
                'staff_id': i[1],
                'staff_name': i[4]
                }
        workers.append(data)
        idx += 1
    result = funcs_main.find_max_operator_clicks()
    data1 = {
        'name': result[0],
        'amounts': result[1]
    }
    result1 = funcs_main.find_max_contributer()
    data2 = {
        'name': result1[0],
        'amounts': result1[1],
    }
    result2 = list(funcs_main.find_last_contributer())
    last_contributer = []
    for i in range(len(result2)):
        result2[i] = list(result2[i])
        if result2[i][1] == '创建表单':
            result2[i][1] = '创建'
        elif result2[i][1] == '修改表单':
            result2[i][1] = '修改'
        data3 = {
            'staff_id': result2[i][0],
            'staff_work': result2[i][1],
            'staff_optio': result2[i][2],
            'staff_name': result2[i][3]
        }
        last_contributer.append(data3)
    return render(request, 'record.html',
                  {'workers': workers, 'operator': data1, 'contributer': data2, 'last_contributer': last_contributer})


def manage1(request, nid):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 2 and request.session.get('user_vip') != 1:
        return redirect('/index/')
    request.session['manage1'] = nid
    return redirect('/manage')


def manage(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 2 and request.session.get('user_vip') != 1:
        return redirect('/index/')

    result = funcs.find_work_manage()
    manages, idx = [], 1
    for i in result:
        data = {'idx': idx,
                'work_number': i[0],
                'work_manager': i[1],
                'work_type': i[2],
                'work_content': i[3],
                'work_num': i[4]
                }
        manages.append(data)
        idx += 1
    nid = request.session['manage1']
    if nid != 0:
        name = list(funcs.find_name(nid))
        result = funcs.find_email_code(name[0])
        apply_name = request.session['user_name']
        funcs.send_email(result[0], apply_name, result[1], nid)
        request.session['manage1'] = 0
    name = request.session['user_name']
    ans = funcs.find_work_team(name)
    vip = request.session['user_vip']
    return render(request, 'manage.html', {'manages': manages, 'ans': ans[0], 'vip': vip})


def process1(request, nid):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 2:
        return redirect('/index/')
    request.session['process1'] = nid
    return redirect('/process')


def process2(request, nid):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 2:
        return redirect('/index/')
    if nid == 0:
        nid = -500
    else:
        nid = -nid
    request.session['process2'] = nid
    return redirect('/process')


def process(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 2:
        return redirect('/index/')
    name = request.session['user_name']
    type1 = list(funcs.find_work_type(name))
    list1 = []
    for i in range(len(type1)):
        list1 = list1 + list(type1[i])
    result = funcs.find_work_record(list1)
    manages, idx = [], 0
    ans = []
    list1 = []
    for i in result:
        data = {'idx': idx,
                'name': i[0],
                'content': i[1],
                'type': i[2],
                'dir': i[3],
                'state': i[4]
                }
        manages.append(data)
        list1.append(idx)
        idx += 1
    for i in range(len(result)):
        introduction = str(i) + ',' + result[i][5]
        introduction = introduction.split(',')
        introduction[0] = int(introduction[0])
        ans.append(introduction)

    nid1 = request.session['process1']
    nid2 = request.session['process2']
    if nid1 != 999:
        i = nid1
    elif nid2 != 999:
        i = nid2
    else:
        i = 999
    if i >= 0 and i != 999:
        email = funcs.find_email_code(result[i][0])
        if result[i][1] == '创建表单':
            if result[i][2] == '干员':
                funcs_main.add_operator(ans[i][1], ans[i][2], ans[i][3], ans[i][4], ans[i][5], ans[i][6], ans[i][7],
                                        int(ans[i][8]), int(ans[i][9]), ans[i][10],
                                        ans[i][11], int(ans[i][12]))
                funcs_main.add_attribute(ans[i][1], int(ans[i][13]), int(ans[i][14]), int(ans[i][15]), int(ans[i][16]),
                                         int(ans[i][17]), int(ans[i][18]), int(ans[i][19]), int(ans[i][20]),
                                         int(ans[i][21]), int(ans[i][22]), int(ans[i][23]), int(ans[i][24]),
                                         int(ans[i][25]), int(ans[i][26]),
                                         int(ans[i][27]),
                                         int(ans[i][28]))
                funcs_main.add_talent(ans[i][1], ans[i][29], ans[i][30], ans[i][31], ans[i][32])
                funcs_main.add_potential(ans[i][1], ans[i][33], ans[i][34], ans[i][35], ans[i][36], ans[i][37])
                funcs_main.add_skill(ans[i][1], ans[i][38], ans[i][39], int(ans[i][40]), int(ans[i][41]),
                                     int(ans[i][42]), ans[i][43],
                                     ans[i][44], int(ans[i][45]), int(ans[i][46]), int(ans[i][47]), ans[i][48],
                                     ans[i][49],
                                     int(ans[i][50]),
                                     int(ans[i][51]), int(ans[i][52]))
            elif result[i][2] == '材料':
                funcs_main.add_material(ans[i][1], ans[i][2], ans[i][3], ans[i][4])
            elif result[i][2] == '卡池':
                funcs_main.add_card_pool(ans[i][1], ans[i][2], pd.to_datetime(ans[i][3]), pd.to_datetime(ans[i][4]),
                                         ans[i][5])
            elif result[i][2] == '敌人':
                funcs_main.add_enemy(ans[i][2], ans[i][1], ans[i][3], ans[i][4], ans[i][5], int(ans[i][6]),
                                     int(ans[i][7]), int(ans[i][8]), int(ans[i][9]), ans[i][10])
            elif result[i][2] == '关卡':
                funcs_main.add_level(ans[i][1], ans[i][2], int(ans[i][3]), int(ans[i][4]), int(ans[i][5]),
                                     int(ans[i][6]), int(ans[i][7]),
                                     int(ans[i][8]), int(ans[i][9]), ans[i][10])

        elif result[i][1] == '修改表单':
            if result[i][2] == '干员':
                funcs_main.delete_attribute(ans[i][1])
                funcs_main.delete_talent(ans[i][1])
                funcs_main.delete_potential(ans[i][1])
                funcs_main.delete_skill(ans[i][1])
                funcs_main.delete_operator(ans[i][1])
            elif result[i][2] == '材料':
                funcs_main.delete_material(ans[i][1])
            elif result[i][2] == '卡池':
                funcs_main.delete_card_pool(ans[i][1])
            elif result[i][2] == '敌人':
                funcs_main.delete_enemy(ans[i][1])
            elif result[i][2] == '关卡':
                funcs_main.delete_level(ans[i][1])
        str1 = '成功提交申请'
        funcs.update_work_record(result[i][6], str1)
        str1 = '恭喜您，提交的内容已通过！'
        str2 = '感谢您的贡献！'
        funcs.send_information_email(email[0], str1, str2)
        request.session['process1'] = 999
        request.session['process2'] = 999
    elif i < 0:
        if i == -500:
            i = 0
        else:
            i = - i
        email = funcs.find_email_code(result[i][0])
        str1 = '申请打回'
        funcs.update_work_record(result[i][6], str1)
        str1 = '对不起，您提交的内容有误或不合规！'
        str2 = '请修改后再提交！'
        funcs.send_information_email(email[0], str1, str2)
        request.session['process1'] = 999
        request.session['process2'] = 999
    return render(request, 'process.html', {'manages': manages, 'ans': ans})


def user_apply_confirm(request):  # 用户确认
    result = request.GET.get('code', None)
    t = result.split('/?')
    code = t[0]
    name = t[1][5:]
    idx = t[2][4:]
    result = funcs.find_email_code(name)
    if code == '1':
        message = '您已拒绝该请求'
        str1 = '对不起，很遗憾的通知您：您未被录取！'
        funcs.send_apply_email(result[0], str1)
        return render(request, 'confirm.html', locals())
    else:
        message = '您已同意该请求'
        str1 = '恭喜您，已成功加入该小组！'
        funcs.send_apply_email(result[0], str1)
        team = funcs.find_work_team(name)
        if team[0] != '0':
            funcs.update_work_num_decline(team[0])
        funcs.update_user_work_team(name, idx)
        funcs.update_work_num(idx)
        return render(request, 'confirm.html', locals())

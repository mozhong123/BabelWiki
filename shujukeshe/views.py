from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from . import forms
from . import funcs
import hashlib
import datetime
import json
from main import funcs as funcs_main
from app01 import funcs as funcs_app

# Create your views here.


def hash_code(s, salt='dazuoye'):  # 对密码与确认码进行加密
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def make_confirm_string(name):  # 创建确认码对象
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(name, now)
    return code


def index(request):  # 主界面
    funcs.create_s_user()  # 建s_user表
    funcs_main.create_Operator()
    funcs_main.create_talent()
    funcs_main.create_potential()
    funcs_main.create_attribute()
    funcs_main.create_skill()
    funcs_main.create_material()
    funcs_main.create_level()
    funcs_main.create_card_pool()
    funcs_main.create_enemy()
    funcs_main.create_comment()
    if not request.session.get('is_login', None):
        return render(request, 'shujukeshe/index_unlogin.html', locals())
    request.session['manage1'] = 0
    request.session['process1'] = 999
    request.session['process2'] = 999
    return render(request, 'shujukeshe/index_login.html', locals())


def to_index(request):
    return redirect('/index/')


def login(request):  # 登录
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = funcs.find_user_name(username)  # 调用查找用户名的函数
            user_confirm = funcs.find_confirms_user_name(username)  # 调用查找用户名的函数
            if not user:
                message = '用户不存在！'
                return render(request, 'shujukeshe/login.html', locals())

            if not user[6]:  # 判断是否邮件确认过
                message = '该用户还未经过邮件确认！'
                return render(request, 'shujukeshe/login.html', locals())

            if user[2] == hash_code(password):  # 判断密码是否相同
                request.session['is_login'] = True
                request.session['user_id'] = user[0]  # id
                request.session['user_name'] = user[1]  # name
                request.session['user_password'] = password  # password
                request.session['user_email'] = user[3]  # email
                request.session['user_sex'] = user[4]  # sex
                request.session['user_birthday'] = user_confirm[2].strftime('%Y-%m-%d')  # birthday
                request.session['user_age'] = user_confirm[3]  # age
                request.session['user_vip'] = user_confirm[4]
                request.session['user_token'] = user_confirm[6]
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'shujukeshe/login.html', locals())
        else:
            return render(request, 'shujukeshe/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'shujukeshe/login.html', locals())


def register(request):  # 注册

    if request.session.get('is_login', None):  # 已经登录了
        return redirect('/index/')
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            if sex == 'male':
                sex = '男'
            elif sex == 'female':
                sex = '女'

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'shujukeshe/register.html', locals())
            else:
                same_name_user = funcs.find_user_name(username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'shujukeshe/register.html', locals())
                same_email_user = funcs.find_user_email(email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'shujukeshe/register.html', locals())
                funcs.add_user(username, hash_code(password1), email, sex)
                code = make_confirm_string(username)
                funcs.update_user_code(username, code)
                funcs.send_email(email, code)
                message = '请前往邮箱进行确认！'
                return render(request, 'shujukeshe/confirm.html', locals())
        else:
            return render(request, 'shujukeshe/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'shujukeshe/register.html', locals())


def logout(request):  # 登出
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()
    # del request.session['is_login']
    return redirect("/index/")


def user_confirm(request):  # 用户确认
    code = request.GET.get('code', None)
    message = ''
    try:
        user = funcs.find_user_code(code)
    except:
        message = '无效的确认请求！'
        return render(request, 'shujukeshe/confirm.html', locals())
    c_time = user[5]
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        funcs.delete_user(user[1])  # 从s_user中删除该用户
        message = '您的邮件已经过期！请重新注册！'
        return render(request, 'shujukeshe/confirm.html', locals())
    else:
        funcs.create_s_confirm_user()  # 建s_confirm_user表
        funcs.add_confirms_user(user[0], user[1])
        funcs.update_user_has_confirmed(user[1], 1)  # 更新注册状态
        message = '感谢确认，请使用账户登录！'
        return render(request, 'shujukeshe/confirm.html', locals())


def user_homepage(request):  # 个人主页
    if not request.session.get('is_login', None):
        return redirect('/index/')
    return render(request, 'shujukeshe/myaccount.html', locals())


def modify(request):  # 修改个人信息
    if not request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        modify_form = forms.Modify_User_Form(request.POST)
        message = "请检查填写的内容！"
        if modify_form.is_valid():
            username = modify_form.cleaned_data.get('username')
            birthday = modify_form.cleaned_data.get('birthday')
            sex = modify_form.cleaned_data.get('sex')
            if sex == 'male':
                sex = '男'
            elif sex == 'female':
                sex = '女'
            same_name_user = funcs.find_user_name(username)
            if same_name_user:
                message = '用户名已经存在!'
                return render(request, 'shujukeshe/modify.html', locals())
            user_id = request.session['user_id']
            funcs.update_user(user_id, username, sex)
            funcs.update_user_birthday(user_id, birthday)
            oldname = request.session['user_name']
            funcs_app.update_work_record_name(oldname, username)
            funcs_app.update_work_manage_name(oldname, username)
            funcs.update_user_operator_name(oldname, username)
            request.session['user_name'] = username
            request.session['user_sex'] = sex
            request.session['user_birthday'] = birthday.strftime('%Y-%m-%d')
            request.session['user_age'] = int((datetime.date.today().__sub__(birthday).days) / 365) + 1


            message = '修改成功！'
            modify_form = forms.Modify_User_Form()
            return render(request, 'shujukeshe/modify.html', locals())
        else:
            return render(request, 'shujukeshe/modify.html', locals())
    else:
        modify_form = forms.Modify_User_Form()
        return render(request, 'shujukeshe/modify.html', locals())


def repassword(request):  # 修改密码
    if not request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        repassword_form = forms.repassword_Form(request.POST)
        message = "请检查填写的内容！"
        if repassword_form.is_valid():
            password1 = repassword_form.cleaned_data.get('password1')
            password2 = repassword_form.cleaned_data.get('password2')
            password3 = repassword_form.cleaned_data.get('password3')
            old_password = request.session['user_password']
            if password1 != old_password:
                message = '密码错误！'
                return render(request, 'shujukeshe/repassword.html', locals())
            if password1 == password2:
                message = '新设置密码与原密码相同！'
                return render(request, 'shujukeshe/repassword.html', locals())
            if password2 != password3:
                message = '两次输入的新密码不一致！'
                return render(request, 'shujukeshe/repassword.html', locals())
            username = request.session['user_name']
            funcs.update_user_password(username, hash_code(password2))
            message = '修改成功，请重新登录！'
            request.session.flush()
            # del request.session['is_login']
            return render(request, 'shujukeshe/p_confirm.html', locals())
        else:
            return render(request, 'shujukeshe/modify.html', locals())
    repassword_form = forms.repassword_Form()
    return render(request, 'shujukeshe/repassword.html', locals())


def contact_us(request):
    return render(request, 'shujukeshe/contact_us.html', locals())


def vip_access(request):
    if request.session.get('user_vip') == 1 or request.session.get('user_vip') == 2:
        return redirect('/user_homepage/')
    q1 = request.GET.get('q1', '1cn@H131')
    q2 = request.GET.get('q2', '1cn@H131')
    q3 = request.GET.get('q3', '1cn@H131')
    if q1 == '1cn@H131' and q2 == '1cn@H131' and q3 == '1cn@H131':
        pass
    elif q1 != '' and q2 != '' and q3 != '':
        if q1 == '驴' and q2 == '蓝毒' and q3 == '冰淇淋':
            name = request.session['user_name']
            funcs.update_confirm_user_vip(name, 1)
            request.session.flush()
            return render(request, 'shujukeshe/v_confirm.html', locals())
        else:
            message = '回答错误！'
    else:
        message = '请填写完整！'
    return render(request, 'shujukeshe/vip_access.html', locals())


def add_operator(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    if request.method == 'GET':
        add_Operator_form = forms.add_Operator(request.GET)
        message = '请检查填写的内容！'
        if add_Operator_form.is_valid():
            user_name = request.session['user_name']
            vip = request.session['user_vip']
            name = add_Operator_form.cleaned_data.get('name', '')
            career = add_Operator_form.cleaned_data.get('career', '')
            rarity = add_Operator_form.cleaned_data.get('rarity', '')
            position = add_Operator_form.cleaned_data.get('position', '')
            sex = add_Operator_form.cleaned_data.get('sex', '')
            retime = add_Operator_form.cleaned_data.get('retime', '')
            refair = add_Operator_form.cleaned_data.get('refair', '')
            block = add_Operator_form.cleaned_data.get('block', '')
            ATI = add_Operator_form.cleaned_data.get('ATI', '')
            material = add_Operator_form.cleaned_data.get('material', '')
            quantity = add_Operator_form.cleaned_data.get('quantity', '')
            HP1 = add_Operator_form.cleaned_data.get('HP1', '')
            ATK1 = add_Operator_form.cleaned_data.get('ATK1', '')
            DEF1 = add_Operator_form.cleaned_data.get('DEF1', '')
            SR1 = add_Operator_form.cleaned_data.get('SR1', '')
            HP2 = add_Operator_form.cleaned_data.get('HP2', '')
            ATK2 = add_Operator_form.cleaned_data.get('ATK2', '')
            DEF2 = add_Operator_form.cleaned_data.get('DEF2', '')
            SR2 = add_Operator_form.cleaned_data.get('SR2', '')
            HP3 = add_Operator_form.cleaned_data.get('HP3', '')
            ATK3 = add_Operator_form.cleaned_data.get('ATK3', '')
            DEF3 = add_Operator_form.cleaned_data.get('DEF3', '')
            SR3 = add_Operator_form.cleaned_data.get('SR3', '')
            HP4 = add_Operator_form.cleaned_data.get('HP4', '')
            ATK4 = add_Operator_form.cleaned_data.get('ATK4', '')
            DEF4 = add_Operator_form.cleaned_data.get('DEF4', '')
            SR4 = add_Operator_form.cleaned_data.get('SR4', '')
            talent_name1 = add_Operator_form.cleaned_data.get('talent_name1', '')
            describe1 = add_Operator_form.cleaned_data.get('describe1', '')
            talent_name2 = add_Operator_form.cleaned_data.get('talent_name2', '')
            describe2 = add_Operator_form.cleaned_data.get('describe2', '')
            potential2 = add_Operator_form.cleaned_data.get('potential2', '')
            potential3 = add_Operator_form.cleaned_data.get('potential3', '')
            potential4 = add_Operator_form.cleaned_data.get('potential4', '')
            potential5 = add_Operator_form.cleaned_data.get('potential5', '')
            potential6 = add_Operator_form.cleaned_data.get('potential6', '')
            skill_name1 = add_Operator_form.cleaned_data.get('skill_name1', '')
            skill_describe1 = add_Operator_form.cleaned_data.get('skill_describe1', '')
            initial1 = add_Operator_form.cleaned_data.get('initial1', '')
            deplete1 = add_Operator_form.cleaned_data.get('deplete1', '')
            continued1 = add_Operator_form.cleaned_data.get('continued1', '')
            skill_name2 = add_Operator_form.cleaned_data.get('skill_name2', '')
            skill_describe2 = add_Operator_form.cleaned_data.get('skill_describe2', '')
            initial2 = add_Operator_form.cleaned_data.get('initial2', '')
            deplete2 = add_Operator_form.cleaned_data.get('deplete2', '')
            continued2 = add_Operator_form.cleaned_data.get('continued2', '')
            skill_name3 = add_Operator_form.cleaned_data.get('skill_name3', '')
            skill_describe3 = add_Operator_form.cleaned_data.get('skill_describe3', '')
            initial3 = add_Operator_form.cleaned_data.get('initial3', '')
            deplete3 = add_Operator_form.cleaned_data.get('deplete3', '')
            continued3 = add_Operator_form.cleaned_data.get('continued3', '')
            if sex == 'male':
                sex = '男'
            elif sex == 'female':
                sex = '女'
            if rarity == '4':
                rarity = '四星'
                avatar1 = '/static/main/image/four/'
                avatar2 = name + '.png'
                avatar = avatar1 + avatar2
            elif rarity == '5':
                rarity = '五星'
                avatar1 = '/static/main/image/five/'
                avatar2 = name + '.png'
                avatar = avatar1 + avatar2
            elif rarity == '6':
                rarity = '六星'
                avatar1 = '/static/main/image/six/'
                avatar2 = name + '.png'
                avatar = avatar1 + avatar2
            if vip == 2:
                funcs_main.add_operator(name, avatar, career, rarity, position, sex, retime, refair, block, material,
                quantity, ATI)
                funcs_main.add_attribute(name, HP1, ATK1, DEF1, SR1, HP2, ATK2, DEF2, SR2, HP3, ATK3, DEF3, SR3, HP4, ATK4,
                  DEF4,
                  SR4)
                funcs_main.add_talent(name, talent_name1, describe1, talent_name2, describe2)
                funcs_main.add_potential(name, potential2, potential3, potential4, potential5, potential6)
                funcs_main.add_skill(name, skill_name1, skill_describe1, initial1, deplete1, continued1, skill_name2,
                skill_describe2, initial2, deplete2, continued2, skill_name3, skill_describe3,
                initial3,
                deplete3, continued3)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = name+','+avatar+','+career+','+rarity+','+position+','+sex+','+retime+','+str(refair)+','+str(block)+','+material+','+quantity+','+str(ATI)+','+str(HP1)+','+str(ATK1)+','+str(DEF1)+','+str(SR1)+','+str(HP2)+','+str(ATK2)+','+str(DEF2)+','+str(SR2)+','+str(HP3)+','+str(ATK3)+','+str(DEF3)+','+str(SR3)+','+str(HP4)+','+str(ATK4)+','+str(DEF4)+','+str(SR4)+','+talent_name1+','+describe1+','+talent_name2+','+describe2+','+potential2+','+potential3+','+potential4+','+potential5+','+potential6+','+skill_name1+','+skill_describe1+','+str(initial1)+','+str(deplete1)+','+str(continued1)+','+skill_name2+','+skill_describe2+','+str(initial2)+','+str(deplete2)+','+str(continued2)+','+skill_name3+','+skill_describe3+','+str(initial3)+','+str(deplete3)+','+str(continued3)
            funcs_app.add_work_record(user_name, '创建表单', '干员', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())
    add_Operator_form = forms.add_Operator()
    return render(request, 'shujukeshe/add_operator.html', locals())


def delete_operator(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    name = request.GET.get('operator', 'hgadshg')
    user_name = request.session['user_name']
    vip = request.session['user_vip']
    if name == '':
        message = '请填写要删除的干员代号！'
    elif name == 'hgadshg':
        pass
    else:
        result = funcs_main.find_exist_operator(name)
        if result == None:
            message = '查无此人！'
        else:
            if vip == 2:
                funcs_main.delete_attribute(name)
                funcs_main.delete_talent(name)
                funcs_main.delete_potential(name)
                funcs_main.delete_skill(name)
                funcs_main.delete_operator(name)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = name
            funcs_app.add_work_record(user_name, '修改表单', '干员', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())
    return render(request, 'shujukeshe/delete_operator.html', locals())


def add_material(request):  # 添加材料
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    if request.method == 'GET':
        add_material_form = forms.add_material(request.GET)
        message = '请检查填写的内容！'
        if add_material_form.is_valid():
            user_name = request.session['user_name']
            vip = request.session['user_vip']
            name = add_material_form.cleaned_data.get('name', '')
            rarity = add_material_form.cleaned_data.get('rarity', '')
            operator_used = add_material_form.cleaned_data.get('operator_used', '')
            if rarity == '4':
                rarity = '四星'
                avatar1 = '/static/main/image/four/'
                avatar2 = name + '.png'
                avatar = avatar1 + avatar2
            elif rarity == '3':
                rarity = '三星'
                avatar1 = '/static/main/image/three/'
                avatar2 = name + '.png'
                avatar = avatar1 + avatar2
            if vip == 2:
                funcs_main.add_material(name, avatar, rarity, operator_used)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = ''
            str1 = name+','+avatar+','+rarity+','+operator_used
            funcs_app.add_work_record(user_name, '创建表单', '材料', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())
    add_Operator_form = forms.add_Operator()
    return render(request, 'shujukeshe/add_material.html', locals())


def delete_material(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    name = request.GET.get('material', 'hgadshg')
    user_name = request.session['user_name']
    vip = request.session['user_vip']
    if name == '':
        message = '请填写要删除的材料名！'
    elif name == 'hgadshg':
        pass
    else:
        result = funcs_main.find_exist_material(name)
        if result == None:
            message = '没有该材料！'
        else:
            if vip == 2:
                funcs_main.delete_material(name)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = name
            funcs_app.add_work_record(user_name, '修改表单', '材料', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())
    return render(request, 'shujukeshe/delete_material.html', locals())


def add_pool(request):  # 添加卡池
    if not request.session.get('is_login'):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    if request.method == 'GET':
        add_pool_form = forms.add_pool(request.GET)
        message = '请检查填写的内容！'
        if add_pool_form.is_valid():
            user_name = request.session['user_name']
            vip = request.session['user_vip']
            name = add_pool_form.cleaned_data.get('name', '')
            begin = add_pool_form.cleaned_data.get('begin', '')
            end = add_pool_form.cleaned_data.get('end', '')
            operator_name = add_pool_form.cleaned_data.get('operator_name', '')
            avatar1 = '/static/main/image/pool/'
            avatar2 = name + '.png'
            avatar = avatar1 + avatar2
            if vip == 2:
                funcs_main.add_card_pool(name, avatar, begin, end, operator_name)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = ''
            str1 = name + ',' + avatar + ',' + str(begin) + ',' + str(end) + ',' + operator_name
            funcs_app.add_work_record(user_name, '创建表单', '卡池', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())
    add_pool_form = forms.add_pool()
    return render(request, 'shujukeshe/add_pool.html', locals())


def delete_pool(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    name = request.GET.get('pool', 'hgadshg')
    user_name = request.session['user_name']
    vip = request.session['user_vip']
    if name == '':
        message = '请填写要删除的卡池名！'
    elif name == 'hgadshg':
        pass
    else:
        result = funcs_main.find_exist_card_pool(name)
        if result == None:
            message = '没有该卡池！'
        else:
            if vip == 2:
                funcs_main.delete_card_pool(name)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = ''
            str1 = name
            funcs_app.add_work_record(user_name, '修改表单', '卡池', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())

    return render(request, 'shujukeshe/delete_pool.html', locals())


def add_enemy(request):  # 添加敌人
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    if request.method == 'GET':
        add_enemy_form = forms.add_enemy(request.GET)
        message = '请检查填写的内容！'
        if add_enemy_form.is_valid():
            user_name = request.session['user_name']
            vip = request.session['user_vip']
            name = add_enemy_form.cleaned_data.get('name', '')
            position = add_enemy_form.cleaned_data.get('position', '')
            species = add_enemy_form.cleaned_data.get('species', '')
            ability = add_enemy_form.cleaned_data.get('ability', '')
            ATK = add_enemy_form.cleaned_data.get('ATK', '')
            HP = add_enemy_form.cleaned_data.get('HP', '')
            DEF = add_enemy_form.cleaned_data.get('DEF', '')
            SR = add_enemy_form.cleaned_data.get('SR', '')
            first_appear = add_enemy_form.cleaned_data.get('first_appear', '')
            avatar1 = '/static/main/image/enemy/'
            avatar2 = name + '.png'
            avatar = avatar1 + avatar2
            if vip == 2:
                funcs_main.add_enemy(avatar, name, position, species, ability, ATK, HP, DEF, SR, first_appear)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = ''
            str1 = name + ',' + avatar + ',' + position + ',' + species + ',' + ability + ',' + str(ATK) + ',' + str(HP) + ',' + str(DEF) + ',' + str(SR) + ',' + first_appear
            funcs_app.add_work_record(user_name, '创建表单', '敌人', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())
    add_enemy_form = forms.add_enemy()
    return render(request, 'shujukeshe/add_enemy.html', locals())


def delete_enemy(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    name = request.GET.get('enemy', 'hgadshg')
    user_name = request.session['user_name']
    vip = request.session['user_vip']
    if name == '':
        message = '请填写要删除的敌人名！'
    elif name == 'hgadshg':
        pass
    else:
        result = funcs_main.find_exist_enemy(name)
        if result == None:
            message = '没有该敌人！'
        else:
            if vip == 2:
                funcs_main.delete_enemy(name)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = ''
            str1 = name
            funcs_app.add_work_record(user_name, '修改表单', '敌人', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())
    return render(request, 'shujukeshe/delete_enemy.html', locals())


def add_level(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    if request.method == 'GET':
        add_level_form = forms.add_level(request.GET)
        message = '请检查填写的内容！'
        if add_level_form.is_valid():
            user_name = request.session['user_name']
            vip = request.session['user_vip']
            name = add_level_form.cleaned_data.get('name', '')
            type1 = add_level_form.cleaned_data.get('type1', '')
            combat_consumption = add_level_form.cleaned_data.get('combat_consumption', '')
            exercise_consumption = add_level_form.cleaned_data.get('exercise_consumption', '')
            deploy_max = add_level_form.cleaned_data.get('deploy_max', '')
            cost = add_level_form.cleaned_data.get('cost', '')
            cost_max = add_level_form.cleaned_data.get('cost_max', '')
            home_HP = add_level_form.cleaned_data.get('home_HP', '')
            enemy_amounts = add_level_form.cleaned_data.get('enemy_amounts', '')
            common_drop = add_level_form.cleaned_data.get('common_drop', '')
            if vip == 2:
                funcs_main.add_level(name, type1, combat_consumption, exercise_consumption, deploy_max, cost, cost_max,
                                     home_HP, enemy_amounts, common_drop)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = ''
            str1 = name + ',' + type1 + ',' + str(combat_consumption) + ',' + str(exercise_consumption) + ',' + str(deploy_max) + ',' + str(cost) + ',' + str(cost_max) + ',' + str(home_HP) + ',' + str(enemy_amounts) + ',' + common_drop
            funcs_app.add_work_record(user_name, '创建表单', '关卡', name, str1)

            return render(request, 'shujukeshe/a_confirm.html', locals())
    add_level_form = forms.add_level()
    return render(request, 'shujukeshe/add_level.html', locals())


def delete_level(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 1 and request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    name = request.GET.get('level', 'hgadshg')
    user_name = request.session['user_name']
    vip = request.session['user_vip']
    if name == '':
        message = '请填写要删除的关卡名！'
    elif name == 'hgadshg':
        pass
    else:
        result = funcs_main.find_exist_level(name)
        if result == None:
            message = '没有该关卡！'
        else:
            if vip == 2:
                funcs_main.delete_level(name)
                return render(request, 'shujukeshe/c_confirm.html', locals())
            str1 = ''
            str1 = name
            funcs_app.add_work_record(user_name, '修改表单', '关卡', name, str1)
            return render(request, 'shujukeshe/a_confirm.html', locals())

    return render(request, 'shujukeshe/delete_level.html', locals())


def upload(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    if request.session.get('user_vip') != 2:
        return redirect('/user_homepage/')
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('title', '')
            belong = form.cleaned_data.get('belong', '')
            rare = form.cleaned_data.get('rare', '')
            if belong == "operator":
                funcs_main.handle_uploaded_file_operator(request.FILES['file'], name, rare)
            elif belong == "material":
                funcs_main.handle_uploaded_file_material(request.FILES['file'], name, rare)
            elif belong == "enemy":
                funcs_main.handle_uploaded_file_enemy(request.FILES['file'], name)
            elif belong == "pool":
                funcs_main.handle_uploaded_file_pool(request.FILES['file'], name)
            elif belong == "others":
                funcs_main.handle_uploaded_file_others(request.FILES['file'], name)
            return render(request, 'shujukeshe/f_confirm.html')
    else:
        form = forms.UploadFileForm()
    return render(request, 'shujukeshe/upload.html', locals())


def get_token(request):
    if request.method == 'POST':
        token=request.POST.get('q1','')
        if token=='':
            message='请输入Token！'
            return render(request, 'shujukeshe/get_token.html',locals())
        name=request.session.get('user_name')
        funcs.update_token(name,token)
        message='成功！'
        request.session['user_token']=token
    return render(request, 'shujukeshe/get_token.html',locals())


def card_record(request):
    token=request.session.get('user_token')
    print(token)
    result=funcs.card_record(token)
    return render(request, 'shujukeshe/card_record.html',{'result':json.dumps(result)})
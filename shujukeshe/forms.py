from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))


class RegisterForm(forms.Form):
    gender = (("male", "男"), ("female", "女"))
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)


class Modify_User_Form(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="新用户名", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label="出生日期",initial='2003-01-01',widget=forms.DateInput(attrs={'type': 'date'}))
    sex = forms.ChoiceField(label='性别', choices=gender)


class repassword_Form(forms.Form):
    password1 = forms.CharField(label="原密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="新密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password3 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class add_Operator(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    rarity_species = (
        ('4', "四星"),
        ('5', "五星"),
        ('6', "六星"),
    )
    name = forms.CharField(label="代号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    career = forms.CharField(label="职业", max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rarity = forms.ChoiceField(label='稀有度', choices=rarity_species)
    position = forms.CharField(label="位置", max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    retime = forms.CharField(label="初始再部署时间", max_length=6,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    refair = forms.IntegerField(label="初始部署费用",
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    block = forms.IntegerField(label="初始阻挡数",
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    material = forms.CharField(label="升级材料", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.CharField(label="数量", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    ATI = forms.CharField(label="初始攻击间隔", max_length=6,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    HP1 = forms.IntegerField(label="初始生命1",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ATK1 = forms.IntegerField(label="初始攻击1",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    DEF1 = forms.IntegerField(label="初始防御1",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    SR1 = forms.IntegerField(label="初始法术抗性1",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    HP2 = forms.IntegerField(label="初始生命2",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ATK2 = forms.IntegerField(label="初始攻击2",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    DEF2 = forms.IntegerField(label="初始防御2",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    SR2 = forms.IntegerField(label="初始法术抗性2",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    HP3 = forms.IntegerField(label="初始生命3",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ATK3 = forms.IntegerField(label="初始攻击3",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    DEF3 = forms.IntegerField(label="初始防御3",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    SR3 = forms.IntegerField(label="初始法术抗性3",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    HP4 = forms.IntegerField(label="初始生命4",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ATK4 = forms.IntegerField(label="初始攻击4",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    DEF4 = forms.IntegerField(label="初始防御4",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    SR4 = forms.IntegerField(label="初始法术抗性4",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    talent_name1 = forms.CharField(label="第一天赋", max_length=10,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    describe1 = forms.CharField(label="描述一", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    talent_name2 = forms.CharField(label="第二天赋", max_length=10,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    describe2 = forms.CharField(label="描述二", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential2 = forms.CharField(label="潜能二", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential3 = forms.CharField(label="潜能三", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential4 = forms.CharField(label="潜能四", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential5 = forms.CharField(label="潜能五", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential6 = forms.CharField(label="潜能六", max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_name1 = forms.CharField(label="技能一名称", max_length=20,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_describe1 = forms.CharField(label="技能一描述", max_length=100,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    initial1 = forms.IntegerField(label="初始1",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    deplete1 = forms.IntegerField(label="消耗1",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    continued1 = forms.IntegerField(label="持续1",
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    skill_name2 = forms.CharField(label="技能二名称", max_length=20,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_describe2 = forms.CharField(label="技能二描述", max_length=100,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    initial2 = forms.IntegerField(label="初始2",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    deplete2 = forms.IntegerField(label="消耗2",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    continued2 = forms.IntegerField(label="持续2",
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    skill_name3 = forms.CharField(label="技能三名称", max_length=20,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_describe3 = forms.CharField(label="技能三描述", max_length=100,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    initial3 = forms.IntegerField(label="初始3",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    deplete3 = forms.IntegerField(label="消耗3",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    continued3 = forms.IntegerField(label="持续3",
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    
class add_material(forms.Form):
    rarity_species = (
        ('4', "四星"),
        ('3', "三星"),
    )
    name = forms.CharField(label="材料名", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rarity = forms.ChoiceField(label='稀有度', choices=rarity_species)
    operator_used = forms.CharField(label="需要的干员", max_length=100,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
class add_level(forms.Form):
    name = forms.CharField(label="代号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type1 = forms.CharField(label="类型", max_length=30,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    combat_consumption = forms.IntegerField(label="作战消耗",
                                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exercise_consumption = forms.IntegerField(label="演习消耗",
                                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    deploy_max = forms.IntegerField(label="部署上限",
                                    widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cost = forms.IntegerField(label="初始cost",
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cost_max = forms.IntegerField(label="cost上限",
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    home_HP = forms.IntegerField(label="目标点耐久",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    enemy_amounts = forms.IntegerField(label="待处理目标数量",
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}))
    common_drop = forms.CharField(label="常规掉落", max_length=40,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
class add_enemy(forms.Form):
    name = forms.CharField(label="敌人名称", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(label="地位级别", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    species = forms.CharField(label="种类", max_length=40,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    ability = forms.CharField(label="能力", max_length=40,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    ATK = forms.IntegerField(label="攻击力",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    HP = forms.IntegerField(label="耐久",
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    DEF = forms.IntegerField(label="防御力",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    SR = forms.IntegerField(label="法术抗性",
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    first_appear = forms.CharField(label="首次出现的关卡", max_length=40,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    
class add_pool(forms.Form):
    name = forms.CharField(label="卡池名称", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    begin = forms.DateTimeField(label="开始时间",input_formats=['%I:%M %p %d-%b-%Y'], widget=forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))
    end = forms.DateTimeField(label="结束时间",input_formats=['%I:%M %p %d-%b-%Y'], widget=forms.DateTimeInput(
                 attrs={'type': 'datetime-local'},
                 format='%I:%M %p %d-%b-%Y'))
    operator_name = forms.CharField(label="可抽取的干员", max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))        



class UploadFileForm(forms.Form):
    belong = (
        ('operator', "干员头像"),
        ('material', "材料图片"),
        ('enemy', "敌人头像"),
        ('pool', "卡池详情"),
        ('others', "其他文件"),
    )
    title = forms.CharField(max_length=50,label="名称", widget=forms.TextInput(attrs={'class': 'form-control form-control-title'}))
    belong = forms.ChoiceField(label='文件类型', choices=belong)
    rare = forms.CharField(label="*稀有度",max_length=50, widget=forms.TextInput(attrs={'class': 'form-control form-control-rare','placeholder':"使用英文填写, 如'five', 若没有该属性则填写'0'"}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control form-control-lg"}))
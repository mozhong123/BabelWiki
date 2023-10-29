from django import forms
from captcha.fields import CaptchaField


class OperatorForm(forms.Form):
    name = forms.CharField(label="代号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    career = forms.CharField(label="职业", max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rarity = forms.IntegerField(label="稀有度",
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    position = forms.CharField(label="位置", max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.CharField(label="性别", max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    HP = forms.IntegerField(label="初始生命",
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ATK = forms.IntegerField(label="初始攻击",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    DEF = forms.IntegerField(label="初始防御",
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    SR = forms.IntegerField(label="初始法术抗性",
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    retime = forms.CharField(label="初始再部署时间", max_length=6,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    refair = forms.IntegerField(label="初始部署费用",
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    block = forms.IntegerField(label="初始阻挡数",
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ATI = forms.CharField(label="初始攻击间隔", max_length=6,
                          widget=forms.TextInput(attrs={'class': 'form-control'}))


class Operator_talent(forms.Form):
    name = forms.CharField(label="代号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    talent_name1 = forms.CharField(label="第一天赋", max_length=10,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    describe1 = forms.CharField(label="描述一", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    talent_name2 = forms.CharField(label="第二天赋", max_length=10,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    describe2 = forms.CharField(label="描述二", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))


class Operator_potential(forms.Form):
    name = forms.CharField(label="代号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential2 = forms.CharField(label="潜能二", max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential3 = forms.CharField(label="潜能三", max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential4 = forms.CharField(label="潜能四", max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential5 = forms.CharField(label="潜能五", max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    potential6 = forms.CharField(label="潜能六", max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))


class Operator_skill(forms.Form):
    name = forms.CharField(label="代号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
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


class Operator_skill2(forms.Form):
    name = forms.CharField(label="代号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_name = forms.CharField(label="技能二名称", max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_describe = forms.CharField(label="技能二描述", max_length=100,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    initial = forms.IntegerField(label="初始",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    deplete = forms.IntegerField(label="消耗",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    continued = forms.IntegerField(label="持续",
                                   widget=forms.NumberInput(attrs={'class': 'form-control'}))


class Operator_skill3(forms.Form):
    name = forms.CharField(label="代号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_name = forms.CharField(label="技能三名称", max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill_describe = forms.CharField(label="技能三描述", max_length=100,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    initial = forms.IntegerField(label="初始",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    deplete = forms.IntegerField(label="消耗",
                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    continued = forms.IntegerField(label="持续",
                                   widget=forms.NumberInput(attrs={'class': 'form-control'}))

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from utils.tencent.sms import send_sms_single


# Create your views here.
def send_sms(request):
    tpl = request.GET.get('tpl')
    mobile = request.GET.get('mobile')
    print(tpl, mobile)
    res = send_sms_single(tpl, mobile)

    # res = HttpResponse('hello word')

    # return JsonResponse(res)
    return HttpResponse(res)


from django import forms
from user.models import UserInfo
# 自定义表单的正则匹配
from django.core.validators import RegexValidator


class RegisterForm(forms.ModelForm):
    # 自定义表单的正则匹配
    mobile_phpne = forms.CharField(label="手机", validators=[RegexValidator(r'^1[3|4|5|6|7|8|9]\d[9]', '手机格式错误'),])
    # 自定义输入框的格式
    password = forms.CharField(label="密码", widget=forms.PasswordInput())

    password1 = forms.CharField(label="再次输入密码", widget=forms.PasswordInput())
    code = forms.CharField(label="验证码")

    class Meta:
        model = UserInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """重写给每个字段动态添加属性"""
        super().__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
            filed.widget.attrs['placeholder'] = '请输入{}'.format(filed.label)




def register(request):
    eh = request.POST.get('hh')
    print(eh, 'sss')
    form = RegisterForm()
    return render(request, 'index.html', {'form':form})


def login(request):
    return send_sms(request)
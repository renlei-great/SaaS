
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from saas_29.settings import SMS_APPID, SMS_APPKEY, SMS_TEMPLATE
from django.http import HttpResponse
import random, string

def send_sms_single(tpl, mobile_phone):
    """使用腾讯云发送短信
    tpl: 使用模板类型
    mobile_phone : 电话号
    """
    try:
        # 短信应用ｉｄ
        appid = SMS_APPID
        # 短信应用 SDK AppKey
        appkey = SMS_APPKEY
        # 需要发送短信的手机号码
        mobile_phone = mobile_phone
        # 签名
        sms_sign = "SaaSRenLei"
        # 模板参数
        if tpl == 'login':
            params = ["".join(random.sample(string.digits, 4))]
        else:
            params = ["".join(random.sample(string.digits, 4)), 5]
        # 短信模板ID，需要在短信控制台中申请
        template_id = SMS_TEMPLATE[tpl]
    except KeyError:
        return HttpResponse("请求方式有误")
    else:
        ssender = SmsSingleSender(appid, appkey)
        res = ssender.send_with_param(
            86,
            mobile_phone,
            template_id,
            params,
            sign=sms_sign
        )
        if res == 0:
            return HttpResponse(res)
        else:
            return HttpResponse(res['errmsg'])


if __name__ == "__main__":
    send_sms_single('register',15561245051)

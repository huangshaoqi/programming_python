# coding:utf-8
import urllib2
import urllib

# 用户名 查看用户名请登录用户中心->验证码、通知短信->帐户及签名设置->APIID
account = "C05613468"
# 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "7b13a658154de39a9c6b7452fa639223"
mobile = "18632229371"
text = "您的验证码是：123456。请不要把验证码泄露给其他人。"
data = {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'}
req = urllib2.urlopen(
    url='http://106.ihuyi.com/webservice/sms.php?method=Submit',
    data=urllib.urlencode(data)
)
content = req.read()
print(content)

# �ӿ����ͣ��������ߴ������Žӿڣ�֧�ַ�����֤����š�����֪ͨ���ŵȡ�
# �˻�ע�᣺��ͨ���õ�ַ��ͨ�˻�http://sms.ihuyi.com/register.html
# ע�����
# ��1�������ڼ䣬����Ĭ�ϵ�ģ����в��ԣ�Ĭ��ģ������ӿ��ĵ���
# ��2����ʹ��APIID���鿴APIID���¼�û�����->��֤�����->��Ʒ����->APIID���� APIkey�����ýӿڣ�
# ��3���ô���������뻥�����߶��Žӿڲο�ʹ�ã��ͻ��ɸ���ʵ����Ҫ���б�д��

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import httplib
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# �û����ǵ�¼�û�����->��֤�����->��Ʒ����->APIID
account = "�û���"
# ���� �鿴�������¼�û�����->��֤�����->��Ʒ����->APIKEY
password = "����"


def send_sms(text, mobile):
    params = urllib.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = "138xxxxxxxx"
    text = "������֤���ǣ�121254���벻Ҫ����֤��й¶�������ˡ�"

    print(send_sms(text, mobile))

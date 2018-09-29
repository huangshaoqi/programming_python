# �ӿ����ͣ��������ߴ������Žӿڣ�֧�ַ�����֤����š�����֪ͨ���ŵȡ�
# �˻�ע�᣺��ͨ���õ�ַ��ͨ�˻�http://user.ihuyi.com/register.html
# ע�����
# ��1�������ڼ䣬����Ĭ�ϵ�ģ����в��ԣ�Ĭ��ģ������ӿ��ĵ���
# ��2����ʹ�� �û��� �� APIkey�����ýӿڣ�APIkey�ڻ�Ա���Ŀ��Ի�ȡ��
# ��3���ô���������뻥�����߶��Žӿڲο�ʹ�ã��ͻ��ɸ���ʵ����Ҫ���б�д��

# !/usr/local/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib

# �û��� �鿴�û������¼�û�����->��֤�롢֪ͨ����->�ʻ���ǩ������->APIID
account = "�û���"
# ���� �鿴�������¼�û�����->��֤�롢֪ͨ����->�ʻ���ǩ������->APIKEY
password = "����"
mobile = "138xxxxxxxx"
text = "������֤���ǣ�121254���벻Ҫ����֤��й¶�������ˡ�"
data = {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'}
req = urllib2.urlopen(
    url='http://106.ihuyi.com/webservice/sms.php?method=Submit',
    data=urllib.urlencode(data)
)
content = req.read()
print(content)

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email import utils
import smtplib

mail_host = ""
mail_user = ""
mail_pass = ""

username = "测试使用"


def send_mail(to_list, sub, content):
    try:
        server = smtplib.SMTP()
        server.connect(mail_host, 25)
        server.login(mail_user, mail_pass)

        # 构建文本内容
        main_msg = MIMEMultipart('related')
        text_msg = MIMEText(content, _subtype='html', _charset='utf-8')
        main_msg.attach(text_msg)

        me = username + "<" + mail_user + ">"
        main_msg['Subject'] = Header(sub, 'utf-8')
        main_msg['From'] = me
        main_msg['To'] = to_list
        main_msg['Date'] = utils.formatdate()

        server.sendmail(me, to_list, main_msg.as_string())
        server.close()
        return True
    except Exception as e:
        return False


if send_mail("290678391@qq.com", "测试邮件", "This is test email."):
    print("发送成功！")
else:
    print("发送失败！")

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '1243998690@qq.com'  # 发件人邮箱账号
my_pass = 'wqwhkdmfxsaagcgj'  # 发件人邮箱密码
my_user = '1243998690@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        # mail_msg = """
        # <p>Python 邮件发送测试...</p>
        # <p><a href="http://www.runoob.com">这是一个链接</a></p>
        # """

        # msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg = MIMEMultipart()
        msg.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open('reports/1.html', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="1.html"'
        msg.attach(att1)

        # 构造附件2，传送当前目录下的 runoob.txt 文件
        att2 = MIMEText(open('reports/2.html', 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="2.html"'
        msg.attach(att2)

        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as err:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
        print('Error msg:', err)
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
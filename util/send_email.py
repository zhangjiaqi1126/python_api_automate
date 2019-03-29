#encoding = utf-8

import smtplib
from email.mime.text import MIMEText

class SendEmail:
    #设置全局变量，邮件服务器、用户名、密码
    global email_host
    global send_user
    global password
    send_user = "15600553885@163.com"
    password = "zjq@1126"
    email_host = "smtp.163.com"
    #定义发邮件方法，设置传入参数，接受邮件的用户列表、主题、正文
    def send_email(self,user_list,sub,content):
        # 实例化SMTP()
        server = smtplib.SMTP()
        # 指定连接的邮箱服务器
        server.connect(email_host)
        # 登录邮箱的用户名、密码
        server.login(send_user, password)
        # 构造一个邮件对象就是一个Message对象，这里的MIMEText对象，表示一个文本邮件对象
        # 第一个参数是邮件正文，第二个参数是MIME的subtype，最后一定要用utf-8编码保证多语言兼容性
        # 普通文本邮件发送的实现，关键是要将MIMEText中_subtype设置为plain
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        # 邮件主题
        message['Subject'] = sub
        message['From'] = send_user
        message['To'] = ';'.join(user_list)
        # 发宋邮件需要发件人，收件人，内容
        server.sendmail(send_user, user_list, message.as_string())
        server.close()

    def send_main(self,pass_count,fail_count):
        #pass_count是测试用例通过的列表，len(pass_count)是计算列表的长度，即通过的个数
        pass_num = len(pass_count)
        # fail_count是测试用例通过的列表，len(fail_count)是计算列表的长度，即失败的个数
        fail_num = len(fail_count)
        #计算中个数
        count_num = pass_num + fail_num
        #计算通过率
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        #计算失败率
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        #接受邮件的列表
        user_list = ['503659253@qq.com']
        #邮件主题
        sub = '接口自动化测试报告邮件'
        #邮件正文
        cotent = "本次测试共运行接口%s个，通过个数为%s个，失败个数为%s个，成功率为%s，失败率为%s" % (
        count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_email(user_list, sub, cotent)
if __name__ =="__main__":
    sendMail = SendEmail()
    sendMail.send_main([1,2,3,4,5,6],[11,22,33,44,55])
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpathInfo
import time

class sendReport:
    def sendReport(self):
        nowTime=time.strftime("%Y-%m-%d", time.localtime())
        resultPath=getpathInfo.set_reportPath()
        sender = '1096902145@qq.com'
        receiver = '18109045175@163.com,2537664035@qq.com'
        smtpserver = 'smtp.qq.com'
        username = '1096902145@qq.com'
        password = 'rwbqymuewstufdha'
        mail_title = nowTime+' API测试报告'

        # 读取html文件内容
        resultPath=getpathInfo.set_reportPath()
        f = open(resultPath, 'rb')  # HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
        mail_body = f.read()
        f.close()

        # filehtml = MIMEText(mail_body, 'base64', 'utf-8')
        # filehtml['Content-Type'] = 'application/octet-stream'
        # filehtml['Content-Disposition'] = 'attachment; filename="report.html"'html


        # 邮件内容, 格式, 编码
        message = MIMEText(mail_body, 'html', 'utf-8')
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = Header(mail_title, 'utf-8')
        #filehtml.attach(filehtml)
        try:
            smtp = smtplib.SMTP()
            smtp.connect('smtp.qq.com')
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, message.as_string())
            print("发送邮件成功！！！")
            smtp.quit()
        except smtplib.SMTPException:
            print("发送邮件失败！！！"+smtplib.SMTPException)



if __name__ == '__main__':
    sendReport().sendReport()
# # 创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = sender
# message['To'] = receiver
# message['Subject'] = Header(mail_title, 'utf-8')
#
# # 邮件正文内容
# message.attach(MIMEText('来来来，这是邮件的正文', 'plain', 'utf-8'))
#
#
# # 构造附件3（附件为HTML格式的网页）
# att3 = MIMEText(open(resultPath, 'rb').read(), 'base64', 'utf-8')
# att3["Content-Type"] = 'application/octet-stream'
# #att3["Content-Disposition"] = 'attachment; filename="report.html"'
# message.attach(att3)
#
# smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
# smtpObj.connect(smtpserver)
# smtpObj.login(username, password)
# smtpObj.sendmail(sender, receiver, message.as_string())
# print("邮件发送成功！！！")
# smtpObj.quit()
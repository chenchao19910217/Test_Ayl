import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'Test_Ayl.settings'

class Core():#核心复用方法

    def __init__(self):
        pass

    def send_mail(self,Subject,content,sender,receiver):
        send_mail(Subject,content,sender,receiver,)
        pass


if __name__ == '__main__':

    mail=Core()
    Subject = '来自www.douchacha.com的测试邮件'
    content = 'BUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUG'
    sender = '122903166@qq.com'
    receiver=['diao.guanguan@aiyingli.com', '642229662@qq.com']
    mail.send_mail(Subject,content,sender,receiver)
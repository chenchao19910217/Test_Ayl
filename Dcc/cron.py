from core.core import Core


def test():
    mail = Core()
    Subject = '来自www.douchacha.com的测试邮件'
    content = 'BUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUG'
    sender = '122903166@qq.com'
    receiver = ['diao.guanguan@aiyingli.com', '642229662@qq.com']
    mail.send_mail(Subject, content, sender, receiver)

if __name__ == "__main__":

    pass
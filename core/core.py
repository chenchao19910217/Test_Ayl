import requests,json,re,os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'Test_Ayl.settings'

class Core():#核心复用方法

    def __init__(self):
        pass

    def send_mail(self,Subject,content,sender,receiver):
        send_mail(Subject,content,sender,receiver,)
        pass

    def yellowlab(self, url):
        yellowlaburl = 'https://yellowlab.tools/api/runs'
        yellow = requests.Session()
        payload = {
            "url": url,
            "waitForResponse": False,
            "screenshot": True,
            "device": "desktop"
        }
        header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "content-type": "application/json;charset=UTF-8",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty"}
        response = yellow.post(yellowlaburl, data=json.dumps(payload), headers=header, verify=False)
        yellowlaburl = 'https://yellowlab.tools/api/runs/%s' % response.json()['runId']
        header = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty"
        }
        response = yellow.get(url=yellowlaburl, headers=header, verify=False)
        runId = response.json()['runId']
        return runId

    # mail=Core()
    # Subject = '来自www.douchacha.com的测试邮件'
    # content = 'BUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUG'
    # sender = '122903166@qq.com'
    # receiver=['diao.guanguan@aiyingli.com', '642229662@qq.com']
    # mail.send_mail(Subject,content,sender,receiver)
from django.shortcuts import render
from django.shortcuts import redirect
import requests,json,re
# Create your views here.
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from core.core import Core
def index(request):
    pass
    return render(request, 'login/index.html')


def webyh(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        print('aaaaaaaaaa')
    return render(request, 'login/login.html')


def yellowlab_test(request):
    if request.method == 'POST':
        yellowlaburl = 'https://yellowlab.tools/api/runs'
        url = request.POST.get('url')
        if (re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',url, flags=0)) != None:
            # yellow = requests.Session()
            # payload = {
            #     "url": url,
            #     "waitForResponse": False,
            #     "screenshot": True,
            #     "device": "desktop"
            # }
            # header = {
            #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            #     "content-type": "application/json;charset=UTF-8",
            #     "sec-fetch-site": "same-origin",
            #     "sec-fetch-mode": "cors",
            #     "sec-fetch-dest": "empty"}
            # response = yellow.post(yellowlaburl, data=json.dumps(payload), headers=header, verify=False)
            # yellowlaburl = 'https://yellowlab.tools/api/runs/%s' % response.json()['runId']
            # header = {
            #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            #     "sec-fetch-site": "same-origin",
            #     "sec-fetch-mode": "cors",
            #     "sec-fetch-dest": "empty"
            # }
            # response = yellow.get(url=yellowlaburl, headers=header, verify=False)
            # runId = response.json()['runId']
            # request.session['runId']=runId
            yellow = Core()
            request.session['runId']=yellow.yellowlab(url)

            return render(request, 'Dcc/yshowresult.html',locals())
        else:
            message = '请检查填写的内容！'
            return render(request, 'Dcc/yshow.html',locals())
    else:
        message = '测试失败请稍后重试！'
        return render(request, 'Dcc/yshow.html',locals())


def yellowlab(request):
    message = '例子url：https://www.douchacha.com/'
    pass
    return render(request, 'Dcc/yshow.html',locals())
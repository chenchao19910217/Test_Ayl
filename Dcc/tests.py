from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-
import requests,json,urllib3,logging
urllib3.disable_warnings()





if __name__ == "__main__":
    request = requests.Session()
    url = 'https://api.test.douchacha.com/api/user/login?ts=1592989548316&he=wrEGbQ5swobCh3bCtw8swp7DgcOUw4DDtlFmbz91wq4zFg%3D%3D&sign=112bce861670e6af'
    payload = {
        "phone": "17710937860",
        "password": "7e87d0177ef866685ec0f118771f406f64f497fb"
    }
    header = {
        "s-id": "371",
        "dcc-href": "https://www.douchacha.com/uppoint",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "dcc-r": "https://www.douchacha.com/monitorlive",
        "d-f": "MTU5Mjk4OTUwNDg3OTp3ckVHYlE1c3dvYkNoM2JDdHc4c3dwN0RnY09VdzRERHRsRm1iejkxd3E0ekZnJTNEJTNEOjI3MDAwNDU3Yjg5N2I2Yzg=",
        "j-id": "1m73",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty"
    }
    response = request.post(url, data=json.dumps(payload), headers=header, verify=False)
    print(response.json())



    url = 'https://api.test.douchacha.com/api/user/login_out'
    header = {
                    "d-f": "MTU5NTkyMzA5MDQwMDpVc0szdzZBaE1UTWh3N0ljd3IwaE9TSENoRCUyRkRyTU9uRWpNVXdyeCUyRnc2a093NjAlMkJ3cjhRR0ElM0QlM0Q6MDA1M2NhODRiYWUxMGQ3OQ==",
                    "dcc-href": "https://test.douchacha.com/workbench",
                    "Authorization": response.json()['data']['token'],
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                    "dcc-r": "",
                    "Sec-Fetch-Site": "same-site",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty"
                }
    response = request.get(url, headers=header, verify=False)
    print(response.json())

    # print(type(response.json()['data']['token']))
    # url = 'https://api.test.douchacha.com/api/user/info'
    # header = {
    #     "s-id": "371",
    #     "dcc-href": "https://www.douchacha.com/uppoint",
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    #     "Content-Type": "application/json;charset=UTF-8",
    #     "dcc-r": "https://www.douchacha.com/monitorlive",
    #     "d-f": "MTU5Mjk4OTU0ODM5MDpUY08lMkZGOE91RlUlMkZEaThPb1ppQkR3cnZDaXNPb3dvVERqQlVPdzVURGxRN0NsM3JEa2clM0QlM0Q6M2Q4ZjdjMWIzZTg2NzAzOA==",
    #     "j-id": "1m73",
    #     "Sec-Fetch-Site": "same-site",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Dest": "empty",
    #     "Authorization": response.json()['data']['token']
    # }
    #
    # response = request.get(url, headers=header)
    # print('aaaaaaaaa',response.json())
    # a=('["code"]', '["data"]["list"][0]["status"]', '["message"]')
    # Casebody="""('["code"]', '["data"]["user"]', '["msg"]')"""
    # Casebody='(code,msg)'
    # temp = Casebody.replace('(', '').replace(')', '')
    # a = tuple([int(i) for i in temp.split(',')])
    # print(a)


    #
    # ps = json.loads('{"code": 200, "msg": "\u767b\u5f55\u6210\u529f", "data": {"token": "eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTU0ODc1NjAsInVzZXJJZCI6MTI2NzI5MTQ2MjA4NjUxNjczNywiY3JlYXRlRGF0ZSI6IjIwMjAtMDctMTYgMTQ6NTk6MjAifQ.ljx00nlp7xmzXz0LO3UUoRQ6V4Cwrf60FpjAZGSwtpU", "rf_certificate": "eyJhbGciOiJIUzUxMiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTYwOTIzNjAsInVzZXJJZCI6MTI2NzI5MTQ2MjA4NjUxNjczNywidG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlKOS5leUowZVhCbElqb2lVRU1pTENKbGVIQWlPakUxT1RVME9EYzFOakFzSW5WelpYSkpaQ0k2TVRJMk56STVNVFEyTWpBNE5qVXhOamN6Tnl3aVkzSmxZWFJsUkdGMFpTSTZJakl3TWpBdE1EY3RNVFlnTVRRNk5UazZNakFpZlEubGp4MDBubHA3eG16WHowTE8zVVVvUlE2VjRDd3JmNjBGcGpBWkdTd3RwVSIsImNyZWF0ZURhdGUiOiIyMDIwLTA3LTE2IDE0OjU5OjIwIn0.cwaKeHKWhMJ7v8v2zLRkbITjJhlSKQ3ZY98BtjuwuGt1DDf0ptmpKvmXklMieWipAgyVYic44LR72zijhS4L8w", "user": {"user_id": "1267291462086516737", "phone": "17710937860", "nick_name": "\u9648\u8d85", "head_img": "http://thirdwx.qlogo.cn/mmopen/WAGMPKTGtRxyEnSm6iaj66ezxeIIFuHTWR6Hh4Eiam9DBppO46mWblZ4mWRSSoohedwDM6FVBXHf8DwpqhKIEzsISibCF6QZXyZ/132", "gender": "male", "grade": "SVIP"}, "user_id": "1267291462086516737"}}')
    # ps2 = json.loads('{"code": 200, "msg": "\u767b\u5f55\u6210\u529f", "data": {"token": "eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTU0OTIxMjQsInVzZXJJZCI6MTI2NzI5MTQ2MjA4NjUxNjczNywiY3JlYXRlRGF0ZSI6IjIwMjAtMDctMTYgMTY6MTU6MjQifQ.BTSLzfNEkwdk2-2AfDYiHScXrOrALmycR0DdttUmyZk", "rf_certificate": "eyJhbGciOiJIUzUxMiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTYwOTY5MjQsInVzZXJJZCI6MTI2NzI5MTQ2MjA4NjUxNjczNywidG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlKOS5leUowZVhCbElqb2lVRU1pTENKbGVIQWlPakUxT1RVME9USXhNalFzSW5WelpYSkpaQ0k2TVRJMk56STVNVFEyTWpBNE5qVXhOamN6Tnl3aVkzSmxZWFJsUkdGMFpTSTZJakl3TWpBdE1EY3RNVFlnTVRZNk1UVTZNalFpZlEuQlRTTHpmTkVrd2RrMi0yQWZEWWlIU2NYck9yQUxteWNSMERkdHRVbXlaayIsImNyZWF0ZURhdGUiOiIyMDIwLTA3LTE2IDE2OjE1OjI0In0.7EowSL-oKX73ed-EAArOSiXBWKB-QaI2wGCdZaE2hcdWsHeZrFMymSIlpZ7OVQ4TxQ8f6IwoWRb6t5ETH3J1PQ", "user": {"user_id": "1267291462086516737", "phone": "17710937860", "nick_name": "\u9648\u8d85", "head_img": "http://thirdwx.qlogo.cn/mmopen/WAGMPKTGtRxyEnSm6iaj66ezxeIIFuHTWR6Hh4Eiam9DBppO46mWblZ4mWRSSoohedwDM6FVBXHf8DwpqhKIEzsISibCF6QZXyZ/132", "gender": "male", "grade": "SVIP"}, "user_id": "1267291462086516737"}}')
    # r = '(["code"],["msg"],["data"]["user"])'
    # par_value_temp = None
    # expected_value_temp = None
    # temp = r.replace('(', '').replace(')', '')
    # a = tuple([str(i) for i in temp.split(',')])
    # print(type(ps))
    # print(type(ps2))
    # print (a)
    #
    # for key in a:
    #     print(key)
    #     exec("par_value_temp = ps%s" % key)
    #     exec("expected_value_temp = ps2%s" % key)
    #     print("expected_value_temp = ps2%s" % key)
    # print(par_value_temp)
    # print(expected_value_temp)

    # from django.shortcuts import render
    # from django.shortcuts import redirect
    # import requests, json, re
    # # Create your views here.
    # import urllib3
    #
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # from django.http import HttpResponse
    # from core.core import Core
    # from django.views.decorators.csrf import csrf_exempt
    # from django.views.decorators.csrf import ensure_csrf_cookie
    #
    #
    # def index(request):
    #     pass
    #     return render(request, 'login/index.html')
    #
    #
    # def webyh(request):
    #     if request.session.get('is_login', None):  # 不允许重复登录
    #         return redirect('/index/')
    #     if request.method == 'POST':
    #         print('aaaaaaaaaa')
    #     return render(request, 'login/login.html')
    #
    #
    # def yellowlab_test(request):
    #     if request.method == 'POST':
    #         yellowlaburl = 'https://yellowlab.tools/api/runs'
    #         url = request.POST.get('url')
    #         if (re.match(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url,
    #                      flags=0)) != None:
    #             # yellow = requests.Session()
    #             # payload = {
    #             #     "url": url,
    #             #     "waitForResponse": False,
    #             #     "screenshot": True,
    #             #     "device": "desktop"
    #             # }
    #             # header = {
    #             #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    #             #     "content-type": "application/json;charset=UTF-8",
    #             #     "sec-fetch-site": "same-origin",
    #             #     "sec-fetch-mode": "cors",
    #             #     "sec-fetch-dest": "empty"}
    #             # response = yellow.post(yellowlaburl, data=json.dumps(payload), headers=header, verify=False)
    #             # yellowlaburl = 'https://yellowlab.tools/api/runs/%s' % response.json()['runId']
    #             # header = {
    #             #     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    #             #     "sec-fetch-site": "same-origin",
    #             #     "sec-fetch-mode": "cors",
    #             #     "sec-fetch-dest": "empty"
    #             # }
    #             # response = yellow.get(url=yellowlaburl, headers=header, verify=False)
    #             # runId = response.json()['runId']
    #             # request.session['runId']=runId
    #             yellow = Core()
    #             request.session['runId'] = yellow.yellowlab(url)
    #
    #             return render(request, 'Dcc/yshowresult.html', locals())
    #         else:
    #             message = '请检查填写的内容！'
    #             return render(request, 'Dcc/yshow.html', locals())
    #     else:
    #         message = '测试失败请稍后重试！'
    #         return render(request, 'Dcc/yshow.html', locals())
    #
    #
    # def yellowlab(request):
    #     message = '例子url：https://www.douchacha.com/'
    #     pass
    #     return render(request, 'Dcc/yshow.html', locals())
    #
    #
    # def caseapi_index(request):
    #     pass
    #     return render(request, 'Dcc/caseapi_index.html', locals())
    #
    #
    # def case_add(request):
    #     pass
    #     return render(request, 'Dcc/caseadd.html', locals())
    #
    #
    # @csrf_exempt
    # @ensure_csrf_cookie
    # def case_test(request):
    #     result = {'resultkey': '', 'Response': ''}
    #
    #     if request.method == 'POST':
    #         # try:
    #         Caseurl = request.POST.get('Caseurl')
    #         Caserequest = request.POST.get('Caserequest')
    #         if Caserequest == 'POST':
    #             Casebody = json.loads(request.POST.get('Casebody'))
    #             Caseheaders = json.loads(request.POST.get('Caseheaders'))
    #             response = requests.post(Caseurl, data=json.dumps(Casebody), headers=Caseheaders, verify=False)
    #             Responsex = response.json()
    #             result['Response'] = Responsex
    #             if len(request.POST.get('Casekey')) != 0:
    #                 inerface_contrast = Core()
    #                 Caseexpected = json.loads(request.POST.get('Caseexpected'))
    #                 Casekey = request.POST.get('Casekey').replace('(', '').replace(')', '')
    #                 keys = tuple([str(i) for i in Casekey.split(',')])
    #                 result['resultkey'] = inerface_contrast.inerface_contrast(keys, response.json(), Caseexpected)
    #                 print(result['resultkey'])
    #             return HttpResponse(json.dumps(result))
    #
    #         elif Caserequest == 'GET':
    #             Caseheaders = json.loads(request.POST.get('Caseheaders'))
    #             response = requests.get(Caseurl, headers=Caseheaders, verify=False)
    #             Responsex = response.json()
    #             result['Response'] = Responsex
    #             if len(request.POST.get('Casekey')) != 0:
    #                 inerface_contrast = Core()
    #                 Caseexpected = json.loads(request.POST.get('Caseexpected'))
    #                 Casekey = request.POST.get('Casekey').replace('(', '').replace(')', '')
    #                 keys = tuple([str(i) for i in Casekey.split(',')])
    #                 result['resultkey'] = inerface_contrast.inerface_contrast(keys, response.json(), Caseexpected)
    #                 print(result['resultkey'])
    #
    #             return HttpResponse(json.dumps(result))
    #     # except:
    #     #     return HttpResponse('404')
    #     else:
    #         return HttpResponse('404')









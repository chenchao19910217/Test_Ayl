# import os
# import json
# import execjs
# import requests
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# url = "https://api.douchacha.com/api/s.js"
#
# heaser = {"accept": "*/*",
# "accept-encoding": "gzip, deflate, br",
# "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
# "cookie": "UM_distinctid=1735b62a0601a2-0148729ff0ea67-b7a1334-232800-1735b62a0616b7; Hm_lvt_5e3b865d73ba569c052e9fb5792de511=1594907117,1595211122,1595212420; Hm_lpvt_5e3b865d73ba569c052e9fb5792de511=1595930764",
# "if-modified-since": "Mon, 27 Jul 2020 08:57:28 GMT",
# "if-none-match": "0DA7B0C1073F5BDFB1C9A879AADA9F4D",
# "referer": "https://test.douchacha.com/",
# "sec-fetch-dest": "script",
# "sec-fetch-mode": "no-cors",
# "sec-fetch-site": "same-site",
# "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
#
# # os.environ["EXECJS_RUNTIME"] = "Node.js"
# # print(execjs.get().name)
# res = requests.get(url=url,headers=heaser,verify=False,timeout=4)
#
# # ctx2 = execjs.compile("""
# #     function add(){
# #         const jsdom = require("jsdom");
# #         const { JSDOM } = jsdom;
# #         const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
# #         window = dom.window;
# #         document = window.document;
# #         XMLHttpRequest = window.XMLHttpRequest;
# #
# #     }
# # """)
#
# # ctx2.call('add')
# print(execjs.get())
# ctx = execjs.compile(res.text)
#
# # ctx.call('he')
#
# print(res.text)

from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-
import requests,json,urllib3,logging
urllib3.disable_warnings()





if __name__ == "__main__":
    request = requests.Session()
    url = 'https://api.test.douchacha.com/api/user/login'
    payload = {	"phone":"18730301074",	"password":"9f993dbea21fa110e9933965c5f968d37e0e42ea"}

    header = {"User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.116Safari/537.36","Accept-Encoding":"gzip,deflate","Accept":",*/*","Connection":"keep-alive","Content-Type":"application/json;charset=UTF-8","dcc-href":"https://api.douchacha.com/api/tiktok/monitor/live/live_list","dcc-r":"https://api.douchacha.com/api/tiktok/monitor/live/live_list","d-f":"df-dcc","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-site","Content-Length":"80"}
    response = request.post(url, data=json.dumps(payload), headers=header, verify=False)
    print(response.json())
    print(type(response.json()['data']['token']))
    url = 'https://api.test.douchacha.com/api/tiktok/monitor/search/live?ts=1595905218541&he=ZeLaJ5Qo6syPWuPwFJSUDaKyotGHjcUh&sign=eb745035685029c8'
    payload ={"page_no":1,"page_size":3,"params_data":{"keyword":"陈赫"}}
    header = {"User-Agent":"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.116Safari/537.36","Accept-Encoding":"gzip,deflate","Accept":",*/*","Connection":"keep-alive","Content-Type":"charset=utf-8","dcc-href":"https://api.douchacha.com/api/tiktok/monitor/live/live_list","dcc-r":"https://api.douchacha.com/api/tiktok/monitor/live/live_list","d-f":"df-dcc","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-site","Content-Length":"80","Authorization": response.json()['data']['token']}

    response = request.post(url, data=json.dumps(payload), headers=header, verify=False)
    print('aaaaaaaaa',response.json())
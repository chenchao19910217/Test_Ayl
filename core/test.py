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
# res = requests.get(url=url,headers=heaser,verify=False,timeout=4)
# print(res.text)
# ctx = execjs.compile(res.content)
# c=ctx.call('window.he("uid")')
# print(c)

# ctx2 = execjs.compile("""
#     function add(){
#         const jsdom = require("jsdom");
#         const { JSDOM } = jsdom;
#         const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
#         window = dom.window;
#         document = window.document;
#         XMLHttpRequest = window.XMLHttpRequest;
#
#     }
# """)

# ctx2.call('add')
# ctx.call('he')
#
# print(res.text)

from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-
import requests,json,urllib3,logging,threading
urllib3.disable_warnings()

class MyThread(threading.Thread):
    def __init__(self, thread_name):
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        request = requests.Session()
        url = 'https://api.douchacha.com/api/tiktok/monitor/live/live_list?ts=1596459224454&he=w7a%2Fwqlvw40MdzhMHdfCw43TML5fBzS4Sh%3D%3D&sign=3823e93f0a431077'
        payload = {"page_no": 1, "page_size": 50,
                   "params_data": {"nick_name": "", "status": ["ING", "WAIT", "SUCCESS", "CANCEL"]}}
        header = {
            'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTcwNjM0ODYsInVzZXJJZCI6MTI4MjU3Njc5MjMwMjg0NTk1MywiY3JlYXRlRGF0ZSI6IjIwMjAtMDgtMDMgMjA6NDQ6NDYifQ.tX-1mZLWwd2ayqxLsCU4YP2uuyh30Ytj8JlWbg576Ao',
            'd-t': '1596455855549',
            'd-v': 'NCxaa1Z5WkhiakJkYll3b0hLdzUxMXdydlVuSGZsSG52VFBzZkR3cSUyRlVvaEFwYkhieXc1N1RNU3pUUEhiS3dxcER3NmRNZFRWVnc2RGljZGY3d3EwV2ZkYmp3b1A3d29NaWM4YmJ3N3pVcXNiNUlNWmp3NDlkd3I3VE9QQ1RPQk1XdzZDVExWWVV0aGREdzdPVW5PSE1ka1pNd3B6VHFIYnVnVTRNZGtWTXdvQ1RQOGZ1dzZPVG93JTNEJTNE',
            'Content-Type': 'application/json;charset=UTF-8'}

        response = request.post(url, data=json.dumps(payload), headers=header, verify=False)

        print(response.json())


if __name__ == "__main__":
    # for i in range(100000):
    #     MyThread("thread-" + str(i)).start()

    request = requests.Session()
    url = 'https://api.douchacha.com/api/user/login?ts=1596454744029&he=G2vTQ3GTulGTNjVwZHbcwqZrw4DwwoehwoL%3D&sign=ed68caf49871c9f6'
    payload = {"phone": "18730301074", "password": "9f993dbea21fa110e9933965c5f968d37e0e42ea"}
    header = {
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/83.0.4103.116Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8", "Content-Length": "80", "d-t": "1596454744029",
        "d-v": "NCx3b1B5ZkhieHc3aCUyQndwSU13cHJUcjhiUndxNU1FZGZiWnhHVW5zYmR3N1VUb3glMkZUblNsOWYzdlVRaEtUbnNmcHdyeEF3ckNVcE9RMWFkYjNobkNUdGtHVHNsS1VzamtVdGRmd3c2clRzeEVrYWRiRWFkYnN3NmdVTE5VVU5kYmxTMkNVbU9ZVW5OR1V2WXZVTXh6VG9zYjN3cmFjQUhiYnc0QXU="}
    response = request.post(url, data=json.dumps(payload), headers=header, verify=False)

    token = response.json()['data']['token']
    print(response.json())

    url = 'https://api.douchacha.com/api/tiktok/monitor/live/live_list?ts=1596462497068&he=wrRJwrHLZkVxZHfcGQkUu8f2wp7ULHfzwoOUq8ft&sign=78a93e9010e085fb'
    payload = {	"page_no":1,	"page_size":50,	"params_data":{		"nick_name":"",		"status":["ING","WAIT","SUCCESS","CANCEL"]	}}
    header = {'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTcwNjcwMTMsInVzZXJJZCI6MTI4MjU3Njc5MjMwMjg0NTk1MywiY3JlYXRlRGF0ZSI6IjIwMjAtMDgtMDMgMjE6NDM6MzMifQ.Su2AUulm665oIi7vjMRmKaVWKElMOnoo5Cb050zWksg', 'Content-Type': 'application/json;charset=UTF-8'}

    response = request.post(url, data=json.dumps(payload), headers=header, verify=False)

    print(response.json())
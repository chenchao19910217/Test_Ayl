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
    print(type(response.json()['data']['token']))
    url = 'https://api.test.douchacha.com/api/user/info'
    header = {
        "s-id": "371",
        "dcc-href": "https://www.douchacha.com/uppoint",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "dcc-r": "https://www.douchacha.com/monitorlive",
        "d-f": "MTU5Mjk4OTU0ODM5MDpUY08lMkZGOE91RlUlMkZEaThPb1ppQkR3cnZDaXNPb3dvVERqQlVPdzVURGxRN0NsM3JEa2clM0QlM0Q6M2Q4ZjdjMWIzZTg2NzAzOA==",
        "j-id": "1m73",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Authorization": response.json()['data']['token']
    }

    response = request.get(url, headers=header)
    print(response.json())




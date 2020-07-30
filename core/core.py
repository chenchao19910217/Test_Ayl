import requests,json,re,os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'Test_Ayl.settings'

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dict_to_object(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    inst = Dict()
    for k, v in dictObj.items():
        inst[k] = dict_to_object(v)
    return inst

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

    def inerface_contrast(self, contrast, parsing, expected_value):  # ---------------------检查接口返回参数
        par_value_temp = None
        expected_value_temp = None
        parsin = None
        expected = None
        error = []
        loc = locals()
        try:
            for key in contrast:
                exec("par_value_temp = parsing%s" % key)
                parsin = loc['par_value_temp']
                exec("expected_value_temp = expected_value%s" % key)
                expected=loc['expected_value_temp']
                # print("4444444444",parsin,expected)
                if parsin == expected:
                    # print('ffffffffffffffffff',str(key))
                    error.append(key+':pass')
                else:
                    # print(key)
                    error.append(key + ':error')
            # print('bbbbbbbbbbbbbbbbbb',error)
            return error
        except:
            error.append(key+":接口没有返回您指定检查得key")
            return error

    def replace(self, keys, Caseheaders,Caseurl,Casebody,Casedeliverlist_s):  # ---------------------检查接口返回参数

        loc = locals()
        for key in keys:
            if 'header' in key:
                Caseheaders=json.loads(Caseheaders)
                # print('1111111111111',keys[key])
                # print('2222222222222',Casedeliverlist_s)
                # print(Casedeliverlist_s['["data"]["token"]'])

                b = eval("""Casedeliverlist_s['%s']""" % keys[key])
                aaa=key.replace("['header']:", '')
                # print('2222222222222222222',aaa)
                exec('Caseheaders["%s"]=b'%aaa)
                Caseheaders = loc['Caseheaders']
                # print('11111111111111111111',Caseheaders)
            elif 'body' in str(key):
                # print(Casebody)
                if len(Casebody) != 0:
                    # print('aaaaaaaaaaa',Casebody)
                    Casebody = json.loads(Casebody)
                    b = eval("""Casedeliverlist_s['%s']""" % keys[key])
                    aaa = key.replace("['body']:", '')
                    # print(aaa)
                    exec('Casebody["%s"]=b' % aaa)
                    Casebody = loc['Casebody']
                else:
                    Casebody = None

            elif 'url' in str(key):
                # print(key)
                b = eval("""Casedeliverlist_s['%s']""" % keys[key])
                url = key.replace("['url']:", '')
                Caseurl = Caseurl + '%s'%url + '=' + b
                # print('33333333',Caseurl)
        return Caseheaders,Caseurl,Casebody



if __name__ == "__main__":

    # ps = json.loads(
    #     '{"code": 200, "msg": "\u767b\u5f55\u6210\u529f", "data": {"token": "eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTU0ODc1NjAsInVzZXJJZCI6MTI2NzI5MTQ2MjA4NjUxNjczNywiY3JlYXRlRGF0ZSI6IjIwMjAtMDctMTYgMTQ6NTk6MjAifQ.ljx00nlp7xmzXz0LO3UUoRQ6V4Cwrf60FpjAZGSwtpU", "rf_certificate": "eyJhbGciOiJIUzUxMiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTYwOTIzNjAsInVzZXJJZCI6MTI2NzI5MTQ2MjA4NjUxNjczNywidG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlKOS5leUowZVhCbElqb2lVRU1pTENKbGVIQWlPakUxT1RVME9EYzFOakFzSW5WelpYSkpaQ0k2TVRJMk56STVNVFEyTWpBNE5qVXhOamN6Tnl3aVkzSmxZWFJsUkdGMFpTSTZJakl3TWpBdE1EY3RNVFlnTVRRNk5UazZNakFpZlEubGp4MDBubHA3eG16WHowTE8zVVVvUlE2VjRDd3JmNjBGcGpBWkdTd3RwVSIsImNyZWF0ZURhdGUiOiIyMDIwLTA3LTE2IDE0OjU5OjIwIn0.cwaKeHKWhMJ7v8v2zLRkbITjJhlSKQ3ZY98BtjuwuGt1DDf0ptmpKvmXklMieWipAgyVYic44LR72zijhS4L8w", "user": {"user_id": "1267291462086516737", "phone": "17710937860", "nick_name": "\u9648\u8d85", "head_img": "http://thirdwx.qlogo.cn/mmopen/WAGMPKTGtRxyEnSm6iaj66ezxeIIFuHTWR6Hh4Eiam9DBppO46mWblZ4mWRSSoohedwDM6FVBXHf8DwpqhKIEzsISibCF6QZXyZ/132", "gender": "male", "grade": "SVIP"}, "user_id": "1267291462086516737"}}')
    # ps2 = json.loads(
    #     '{"code": 200, "msg": "\u767b\u5f55\u6210\u529f", "data": {"token": "eyJhbGciOiJIUzI1NiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTU0OTIxMjQsInVzZXJJZCI6MTI2NzI5MTQ2MjA4NjUxNjczNywiY3JlYXRlRGF0ZSI6IjIwMjAtMDctMTYgMTY6MTU6MjQifQ.BTSLzfNEkwdk2-2AfDYiHScXrOrALmycR0DdttUmyZk", "rf_certificate": "eyJhbGciOiJIUzUxMiJ9.eyJ0eXBlIjoiUEMiLCJleHAiOjE1OTYwOTY5MjQsInVzZXJJZCI6MTI2NzI5MTQ2MjA4NjUxNjczNywidG9rZW4iOiJleUpoYkdjaU9pSklVekkxTmlKOS5leUowZVhCbElqb2lVRU1pTENKbGVIQWlPakUxT1RVME9USXhNalFzSW5WelpYSkpaQ0k2TVRJMk56STVNVFEyTWpBNE5qVXhOamN6Tnl3aVkzSmxZWFJsUkdGMFpTSTZJakl3TWpBdE1EY3RNVFlnTVRZNk1UVTZNalFpZlEuQlRTTHpmTkVrd2RrMi0yQWZEWWlIU2NYck9yQUxteWNSMERkdHRVbXlaayIsImNyZWF0ZURhdGUiOiIyMDIwLTA3LTE2IDE2OjE1OjI0In0.7EowSL-oKX73ed-EAArOSiXBWKB-QaI2wGCdZaE2hcdWsHeZrFMymSIlpZ7OVQ4TxQ8f6IwoWRb6t5ETH3J1PQ", "user": {"user_id": "1267291462086516737", "phone": "17710937860", "nick_name": "\u9648\u8d85", "head_img": "http://thirdwx.qlogo.cn/mmopen/WAGMPKTGtRxyEnSm6iaj66ezxeIIFuHTWR6Hh4Eiam9DBppO46mWblZ4mWRSSoohedwDM6FVBXHf8DwpqhKIEzsISibCF6QZXyZ/132", "gender": "male", "grade": "SVIP"}, "user_id": "1267291462086516737"}}')
    # r = '(["code"],["msg"],["data"]["user"])'
    # temp = r.replace('(', '').replace(')', '')
    # a = tuple([str(i) for i in temp.split(',')])
    # # print(type(ps))
    # # print(type(ps2))
    # # print(a)
    # c=Core()
    # c.inerface_contrast(a,ps,ps2)


    mail=Core()
    Subject = '来自www.douchacha.com的测试邮件'
    content = 'BUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUGBUG'
    sender = '122903166@qq.com'
    receiver=['diao.guanguan@aiyingli.com', '642229662@qq.com']
    mail.send_mail(Subject,content,sender,receiver)
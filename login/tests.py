import requests,json
request = requests.Session()



yellowlaburl = 'https://yellowlab.tools/api/runs'
payload = {
            "url": "www.baidu.com",
            "waitForResponse": False,
            "screenshot":True,
            "device":"desktop"
        }
header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "content-type": "application/json;charset=UTF-8",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty"}
response = request.post(yellowlaburl, data=json.dumps(payload), headers=header, verify=False)
print(response.json()['runId'])



yellowlaburl='https://yellowlab.tools/api/runs/%s' % response.json()['runId']
header= {
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty"
                }
response = request.get(url=yellowlaburl, headers=header, verify=False)
print(response.json())

yellowlaburl = 'https://yellowlab.tools/queue/%s' % response.json()['runId']
response = request.get(url=yellowlaburl, headers=header, verify=False)




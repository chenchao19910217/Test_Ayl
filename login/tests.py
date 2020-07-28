# import requests,json
# request = requests.Session()
#
#
#
# yellowlaburl = 'https://yellowlab.tools/api/runs'
# payload = {
#             "url": "www.baidu.com",
#             "waitForResponse": False,
#             "screenshot":True,
#             "device":"desktop"
#         }
# header = {
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
#     "content-type": "application/json;charset=UTF-8",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-dest": "empty"}
# response = request.post(yellowlaburl, data=json.dumps(payload), headers=header, verify=False)
# print(response.json()['runId'])
#
#
#
# yellowlaburl='https://yellowlab.tools/api/runs/%s' % response.json()['runId']
# header= {
#                     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
#                     "sec-fetch-site": "same-origin",
#                     "sec-fetch-mode": "cors",
#                     "sec-fetch-dest": "empty"
#                 }
# response = request.get(url=yellowlaburl, headers=header, verify=False)
# print(response.json())
#
# yellowlaburl = 'https://yellowlab.tools/queue/%s' % response.json()['runId']
# response = request.get(url=yellowlaburl, headers=header, verify=False)
import execjs
import gevent
from locust import HttpUser, task, between
from locust.env import Environment
from locust.stats import stats_printer
from locust.log import setup_logging
#
# setup_logging("INFO", None)

if __name__ == "__main__":
    import execjs

    import execjs

    e = execjs.eval('a=new Array(1,2,3)')
    print(e)

    # class User(HttpUser):
    #     wait_time = between(1, 3)
    #     host = "https://docs.locust.io"
    #
    #     @task
    #     def my_task(self):
    #         self.client.get("/")
    #
    #     @task
    #     def task_404(self):
    #         self.client.get("/non-existing-path")
    #
    #
    #
    # # setup Environment and Runner
    # env = Environment(user_classes=[User])
    # env.create_local_runner()
    #
    # # start a WebUI instance
    # env.create_web_ui("127.0.0.1", 8089)
    #
    # # start a greenlet that periodically outputs the current stats
    # gevent.spawn(stats_printer(env.stats))
    #
    # # start the test
    # env.runner.start(100, hatch_rate=100)
    #
    # # in 60 seconds stop the runner
    # gevent.spawn_later(120, lambda: env.runner.quit())
    #
    # # wait for the greenlets
    # env.runner.greenlet.join()
    #
    # # stop the web server for good measures
    # env.web_ui.stop()


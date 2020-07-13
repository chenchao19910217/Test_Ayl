

# -*- coding: utf-8 -*-

import requests,logging,os,json

def log(func):

    def wrapper(*args, **kw):
        # 第一步，创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # Log等级总开关
        # 第二步，创建一个handler，用于写入日志文件
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Test_Ayl/Dcc/testapi/Logs/'
        log_name = log_path + func.__name__ + '.log'
        logfile = log_name
        print(logfile)
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
        # 第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 第四步，将logger添加到handler里面
        logger.addHandler(fh)

        return func(*args, **kw)
    return wrapper

class TestCaseCore():#核心复用方法

    def __init__(self):
        pass

    def requests_get(self,url,path,data,header,time,**kw):
        try:
            response = requests.get(url=url+path, params=data, headers=header,timeout=time)
            if response.status_code in [404,400,500,505]:
                print(response.json())
                return {'code':False,'status_code':response.status_code}
            else:
                print(response.json())
                return {'code':True,'content':response.json(),'cookies':response.cookies,'status_code':response.status_code}
        except:
            return {'code': False, 'status_code': response.status_code}


    def requests_post(self,url,path,data,header,time):
        try:
            response = requests.post(url+path, data=json.dumps(data), headers=header, verify=False,timeout=time)
            if response.status_code in [404,400,500,505]:
                return {'code':False,'status_code':response.status_code}
            else:
                return {'code':True,'content':response.json(),'cookies':response.cookies,'status_code':response.status_code}
        except:
            return {'code': False, 'status_code': response.status_code}

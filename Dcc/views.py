# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
import requests,json,re,time,ast
# Create your views here.
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from django.http import HttpResponse
from core.core import Core
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from . import models
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

def caseapi_index(request):
    caseapi_return = {
        "code": '',
        "msg": '',
        "equipment": {
            # 0: {
            #     'phonevendorname': '111111',
            #     'phoneequipmentname': '222222',
            #     'phoneserialnumber': '333333',
            #     'phone_state': '4444444',
            # },
        }
    }
    apilist = models.apilist()
    caselists = models.apilist.objects.all()

    for index in range(len(caselists)):
        caseapi_return['equipment'][index] = {
            'item': caselists[index].item,
            'release':caselists[index].release,
            'modules':caselists[index].modules,
            'casename': caselists[index].casename,
            'edit':caselists[index].case_id,
            'go':caselists[index].case_id
        }

    return render(request, 'Dcc/caseapi_index.html',locals())

def case_add(request):
    pass
    return render(request, 'Dcc/caseadd.html',locals())

@csrf_exempt
@ensure_csrf_cookie
def case_test(request):
    inerface_contrast = Core()
    Casedeliver= []
    Casedeliverlist_s={}
    gonumber = 1
    aaa=1
    if request.method == 'POST':
        caselist = request.POST.get('caselist_s')
        caselist = json.loads(caselist)
        result = []
        for case in caselist:
            aaa=aaa+1

            resultcase = {'resultkey': '', 'Response': ''}
            Caserequest = caselist[case]['Caserequest']

            if Caserequest == 'POST':
                Caseurl = caselist[case]['Caseurl']
                Casebody = caselist[case]['Casebody'].replace("'", '"').replace(" ", "")
                Caseheaders = caselist[case]['Caseheaders'].replace("'", '"').replace(" ", "")
                Casekey = caselist[case]['Casekey'].replace("'", '"').replace(" ", "")
                Caseexpected = caselist[case]['Caseexpected'].replace("'", '"').replace(" ", "")
                Casedeliver = caselist[case]['Casedeliver'].replace(" ", "")
                Casereplace = caselist[case]['Casereplace'].replace(" ", "")
                if len(Caseurl)<1 or len(Caseheaders)<1 or len(Casebody)<1 :

                    Response={
                        "code": '400',
                        "msg": '搞什么呢url和headers都不填等我填呢？body也是必填！'

                        }
                    return HttpResponse(json.dumps(Response))
                if len(Caseexpected)<1 or len(Casekey)<1 :

                    Response={
                        "code": '400',
                        "msg": '预期值和检查key不填你让我测啥！'

                        }
                    return HttpResponse(json.dumps(Response))


                if len(Casereplace) > 0 and len(Casedeliver) > 0:
                    Casereplace = eval(Casereplace)
                    Caseheaders, Caseurl, Casebody = inerface_contrast.replace(Casereplace, Caseheaders, Caseurl,Casebody, Casedeliverlist_s)

                    response = requests.post(Caseurl, data=Casebody.encode('utf-8'), headers=Caseheaders, verify=False)
                    Response = response.json()


                elif len(Casedeliver) > 0:
                    response = requests.post(Caseurl, data=Casebody.encode('utf-8'), headers=json.loads(Caseheaders), verify=False)
                    Response = response.json()
                    Casedeliverkeys = Casedeliver.replace('(', '').replace(')', '')
                    keys = tuple([str(i) for i in Casedeliverkeys.split(',')])
                    loc = locals()
                    for key in keys:
                        exec("Casedeliverlist = Response%s" % key)
                        Casedeliverlist_s[key] = loc['Casedeliverlist']


                elif len(Casereplace) > 0:
                    Casereplace = eval(Casereplace)
                    Caseheaders, Caseurl, Casebody = inerface_contrast.replace(Casereplace, Caseheaders, Caseurl,
                                                                               Casebody, Casedeliverlist_s)

                    time.sleep(5)

                    response = requests.post(Caseurl, data=Casebody.encode('utf-8'), headers=Caseheaders, verify=False)
                    Response = response.json()


                else:
                    response = requests.post(Caseurl, data=Casebody.encode('utf-8'), headers=json.loads(Caseheaders), verify=False)
                    Response = response.json()



                if len(Casekey) != 0 and len(Caseexpected) != 0:
                    try:
                        Caseexpected= Caseexpected.replace(" ", "")

                        Caseexpected = eval(Caseexpected)
                        # Caseexpected = json.loads(Caseexpected)
                        Casekeys = Casekey.replace('(', '').replace(')', '')
                        keys = tuple([str(i) for i in Casekeys.split(',')])
                        resultkey=inerface_contrast.inerface_contrast(keys, response.json(), Caseexpected)
                        resultcase['resultkey'] = resultkey
                        resultcase['Response'] = Response
                        result.append(resultcase)
                    except:
                        Response = {
                            "code": '400',
                            "msg": '预期值格式错误'

                        }
                        return HttpResponse(json.dumps(Response))


            elif Caserequest == 'GET':
                Caseurl = caselist[case]['Caseurl']
                Casebody = caselist[case]['Casebody'].replace("'", '"').replace(" ", "")
                Caseheaders = caselist[case]['Caseheaders'].replace("'", '"').replace(" ", "")
                Casekey = caselist[case]['Casekey'].replace("'", '"').replace(" ", "")
                Caseexpected = caselist[case]['Caseexpected'].replace("'", '"').replace(" ", "")
                Casedeliver = caselist[case]['Casedeliver'].replace(" ", "")
                Casereplace = caselist[case]['Casereplace'].replace(" ", "")
                if len(Caseurl)<1 or len(Caseheaders)<1:

                    Response={
                        "code": '400',
                        "msg": '搞什么呢url和headers都不填等我填呢？'

                        }
                    return HttpResponse(json.dumps(Response))
                if len(Caseexpected)<1 or len(Casekey)<1 :

                    Response={
                        "code": '400',
                        "msg": '预期值和检查key不填你让我测啥！'

                        }
                    return HttpResponse(json.dumps(Response))


                # print('ooooooooooooooooo', Casereplace)
                # print('eeeeeeeeeeeeeeeee', Casedeliver)

                if len(Casereplace) > 0 and len(Casedeliver)>0:
                    Casereplace = eval(Casereplace)
                    Caseheaders,Caseurl,Casebody=inerface_contrast.replace(Casereplace, Caseheaders, Caseurl, Casebody,Casedeliverlist_s)
                    response = requests.get(Caseurl, headers=json.loads(Caseheaders), verify=False)
                    Response = response.json()

                elif len(Casedeliver)>0:
                    response = requests.get(Caseurl, headers=json.loads(Caseheaders), verify=False)
                    Response = response.json()
                    Casedeliverkeys = Casedeliver.replace('(', '').replace(')', '')
                    keys = tuple([str(i) for i in Casedeliverkeys.split(',')])
                    loc = locals()
                    for key in keys:
                        exec("Casedeliverlist = Response%s" % key)
                        Casedeliverlist_s[key] = loc['Casedeliverlist']

                elif len(Casereplace) > 0:
                    Casereplace = eval(Casereplace)
                    Caseheaders, Caseurl, Casebody = inerface_contrast.replace(Casereplace, Caseheaders, Caseurl,
                                                                               Casebody, Casedeliverlist_s)
                    time.sleep(5)
                    response = requests.get(Caseurl, headers=Caseheaders, verify=False)
                    Response = response.json()

                else:
                    response = requests.get(Caseurl, headers=json.loads(Caseheaders), verify=False)
                    # print("wwwwwwwwwwwwwwwwwwwww",response.json())
                    Response = response.json()
                    # return HttpResponse(json.dumps(result))


                if len(Casekey) != 0 and len(Caseexpected) != 0:
                    try:
                        Caseexpected = eval(Caseexpected)
                        Casekeys = Casekey.replace('(', '').replace(')', '')
                        keys = tuple([str(i) for i in Casekeys.split(',')])
                        resultkey=inerface_contrast.inerface_contrast(keys, response.json(), Caseexpected)
                        resultcase['resultkey'] = resultkey
                        resultcase['Response'] = Response
                        result.append(resultcase)
                    except:
                        Response = {
                            "code": '400',
                            "msg": '预期值格式错误'

                        }
                        return HttpResponse(json.dumps(Response))


    return HttpResponse(json.dumps(result))

@csrf_exempt
@ensure_csrf_cookie
def case_save(request):
    apilist = {}
    if request.method == 'POST':
        caselist = request.POST.get('request_cases_s')
        caselist = caselist
        caselist = json.loads(caselist)
    if len(caselist)>0 and len(caselist['Items_list']['Items']) and len(caselist['Items_list']['Releases']) and len(caselist['Items_list']['Moduless']) and len(caselist['Items_list']['Casenames']) and(len(caselist['caselist'])):

        item = caselist['Items_list']['Items']
        release = caselist['Items_list']['Releases']
        modules = caselist['Items_list']['Moduless']
        casename = caselist['Items_list']['Casenames']
        caselists = caselist['caselist']

        apilist = models.apilist()
        apilist.item = item
        apilist.release = release
        apilist.modules = modules
        apilist.casename = casename
        apilist.caselists = caselists

        try:
            oldcase = models.apilist.objects.get(item=item,release = release,modules = modules,casename = casename)
            # oldcase.item = item
            # oldcase.release = release
            # oldcase.modules = modules
            # oldcase.casename = casename
            # oldcase.caselists = caselists
            # oldcase.save()
            print({'code': '200', 'message': '更新成功'})
            return HttpResponse(json.dumps({'code': '404', 'message': '已经存在相同用例可以到用例集更新用例'}))
        except:
            apilist.save()
            print({'code': '200', 'message': '添加成功'})
            return HttpResponse(json.dumps({'code': '200', 'message': '添加成功'}))

    else:
        print({'code': '404', 'message': '请检查用例，项目，迭代版本，模块，case名是必填选项'})
        return HttpResponse(json.dumps({'code': '404', 'message': '请检查用例，项目，迭代版本，模块，case名是必填选项'}))

@csrf_exempt
@ensure_csrf_cookie
def testlist_index(request):
    Casedeliver = []
    Casedeliverlist_s = {}
    if request.method == 'POST':
        result = []
        caselist = request.POST.get('caselist_s')
        user_name = request.POST.get('user_names')
        caselist = json.loads(caselist)
        apilist = models.apilist()
        inerface_contrast = Core()
        for caseid in caselist:
            case = models.apilist.objects.get(case_id=caselist[caseid])
            caselists=case.caselists.replace(r"\n", '').replace(" ", "").replace(r"\\", '')
            caselists=eval(caselists)
            for case in caselists:

                Caserequest = caselists[case]['Caserequest']
                if Caserequest == 'POST':
                    resultcase = {'resultkey': '', 'Response': '', 'url': '','Caseexpected':'','Casereplace':'','Casedeliver':''}
                    Caseurl = caselists[case]['Caseurl']
                    resultcase['url'] = Caseurl
                    Casebody = caselists[case]['Casebody']
                    Caseheaders = caselists[case]['Caseheaders']
                    Casekey = caselists[case]['Casekey']
                    Caseexpected = caselists[case]['Caseexpected']
                    Casedeliver = caselists[case]['Casedeliver']
                    Casereplace = caselists[case]['Casereplace']
                    resultcase['Caseexpected'] = Caseexpected
                    resultcase['Casereplace'] = Casereplace
                    resultcase['Casedeliver'] = Casedeliver

                    if len(Caseurl) < 1 or len(Caseheaders) < 1 or len(Casebody) < 1:
                        Response = {
                            "code": '400',
                            "msg": '搞什么呢url和headers都不填等我填呢？body也是必填！'

                        }
                        return HttpResponse(json.dumps(Response))
                    if len(Caseexpected) < 1 or len(Casekey) < 1:
                        Response = {
                            "code": '400',
                            "msg": '预期值和检查key不填你让我测啥！'

                        }
                        return HttpResponse(json.dumps(Response))

                    # print('111111111111111111',Casereplace)
                    if len(Casereplace) > 0 and len(Casedeliver) > 0:
                        Casereplace = eval(Casereplace)
                        Caseheaders, Caseurl, Casebody = inerface_contrast.replace(Casereplace, Caseheaders, Caseurl,
                                                                                   Casebody, Casedeliverlist_s)
                        # print(type(Caseheaders))
                        response = requests.post(Caseurl, data=Casebody.encode('utf-8'), headers=Caseheaders, verify=False)
                        Response = response.json()
                        # print('len(Casereplace) > 0 and len(Casedeliver) > 0', Response)

                    elif len(Casedeliver) > 0:
                        response = requests.post(Caseurl, data=Casebody.encode('utf-8'), headers=json.loads(Caseheaders), verify=False)
                        Response = response.json()
                        Casedeliverkeys = Casedeliver.replace('(', '').replace(')', '')
                        keys = tuple([str(i) for i in Casedeliverkeys.split(',')])
                        loc = locals()
                        for key in keys:
                            exec("Casedeliverlist = Response%s" % key)
                            Casedeliverlist_s[key] = loc['Casedeliverlist']
                        # print(Casedeliverlist_s)
                        # print('len(Casedeliver) > 0', Response)

                    elif len(Casereplace) > 0:
                        Casereplace = eval(Casereplace)
                        Caseheaders, Caseurl, Casebody = inerface_contrast.replace(Casereplace, Caseheaders, Caseurl,
                                                                                   Casebody, Casedeliverlist_s)
                        # print(type(Caseheaders))
                        time.sleep(5)
                        response = requests.post(Caseurl, data=Casebody.encode('utf-8'), headers=Caseheaders, verify=False)
                        Response = response.json()

                        # print('len(Casereplace) > 0 and len(Casedeliver) > 0', Response)

                    else:
                        response = requests.post(Caseurl, data=Casebody.encode('utf-8'), headers=json.loads(Caseheaders), verify=False)
                        Response = response.json()
                        # print('最后', Response)

                    if len(Casekey) != 0 and len(Caseexpected) != 0:
                        try:
                            Caseexpected = eval(Caseexpected)
                            # Caseexpected = json.loads(Caseexpected)
                            Casekeys = Casekey.replace('(', '').replace(')', '')
                            keys = tuple([str(i) for i in Casekeys.split(',')])
                            resultkey = inerface_contrast.inerface_contrast(keys, response.json(), Caseexpected)
                            resultcase['resultkey'] = resultkey
                            resultcase['Response'] = Response

                            result.append(resultcase)
                        except:
                            resultcase['resultkey'] = "格式错误"
                            resultcase['Response'] ="格式错误"
                            result.append(resultcase)

                elif Caserequest == 'GET':
                    resultcase = {'resultkey': '', 'Response': '', 'url': '','Caseexpected':'','Casereplace':'','Casedeliver':''}
                    Caseurl = caselists[case]['Caseurl']
                    resultcase['url'] = Caseurl
                    Casebody = caselists[case]['Casebody']
                    Caseheaders = caselists[case]['Caseheaders']
                    Casekey = caselists[case]['Casekey']
                    Caseexpected = caselists[case]['Caseexpected']
                    Casedeliver = caselists[case]['Casedeliver']
                    Casereplace = caselists[case]['Casereplace']
                    resultcase['Caseexpected'] = Caseexpected
                    resultcase['Casereplace'] = Casereplace
                    resultcase['Casedeliver'] = Casedeliver

                    if len(Caseurl) < 1 or len(Caseheaders) < 1:
                        Response = {
                            "code": '400',
                            "msg": '搞什么呢url和headers都不填等我填呢？'

                        }
                        return HttpResponse(json.dumps(Response))
                    if len(Caseexpected) < 1 or len(Casekey) < 1:
                        Response = {
                            "code": '400',
                            "msg": '预期值和检查key不填你让我测啥！'

                        }
                        return HttpResponse(json.dumps(Response))

                    if len(Casereplace) > 0 and len(Casedeliver) > 0:
                        Casereplace = eval(Casereplace)
                        Caseheaders, Caseurl, Casebody = inerface_contrast.replace(Casereplace, Caseheaders, Caseurl,
                                                                                   Casebody, Casedeliverlist_s)
                        response = requests.get(Caseurl, headers=json.loads(Caseheaders), verify=False)
                        Response = response.json()

                    elif len(Casedeliver) > 0:
                        response = requests.get(Caseurl, headers=json.loads(Caseheaders), verify=False)
                        Response = response.json()
                        Casedeliverkeys = Casedeliver.replace('(', '').replace(')', '')
                        keys = tuple([str(i) for i in Casedeliverkeys.split(',')])
                        loc = locals()
                        for key in keys:
                            exec("Casedeliverlist = Response%s" % key)
                            Casedeliverlist_s[key] = loc['Casedeliverlist']


                    elif len(Casereplace) > 0:
                        Casereplace = eval(Casereplace)
                        Caseheaders, Caseurl, Casebody = inerface_contrast.replace(Casereplace, Caseheaders, Caseurl,
                                                                                   Casebody, Casedeliverlist_s)
                        time.sleep(5)
                        response = requests.get(Caseurl, headers=Caseheaders, verify=False)
                        Response = response.json()

                    else:
                        response = requests.get(Caseurl, headers=json.loads(Caseheaders), verify=False)
                        # print("wwwwwwwwwwwwwwwwwwwww",response.json())
                        Response = response.json()


                    if len(Casekey) != 0 and len(Caseexpected) != 0:
                        try:
                            Caseexpected = eval(Caseexpected)
                            Casekeys = Casekey.replace('(', '').replace(')', '')
                            keys = tuple([str(i) for i in Casekeys.split(',')])
                            resultkey = inerface_contrast.inerface_contrast(keys, response.json(), Caseexpected)
                            resultcase['resultkey'] = resultkey
                            resultcase['Response'] = Response

                            result.append(resultcase)
                        except:
                            resultcase['resultkey'] = "格式错误"
                            resultcase['Response'] = "格式错误"
                            result.append(resultcase)

    reportlist = models.reportlist()

    localtime = time.asctime( time.localtime(time.time()) )

    reportlist.reportname = user_name+':'+localtime.replace(r" ", '_')

    reportlist.report = str(result)

    reportlist.reportclass = "API"

    reportlist.save()


    request_code={'code': '200', 'message': '测试结束'}

    return HttpResponse(json.dumps(request_code))

@csrf_exempt
@ensure_csrf_cookie
def case_edit(request):

    if request.method == 'POST':
        caseapi_return = []
        caselist = request.POST.get('caselist_s')
        # print(caselist)
        case = models.apilist.objects.get(case_id=caselist)
        case = eval(case.caselists.replace(' ', '').replace(r'\n', ''))
        # print(type(case))
        for x in case:
            caseapi_return.append(case[x])
        print(caseapi_return)
        return HttpResponse(json.dumps(caseapi_return))
    else:
        apilist = {}
        case_id = request.GET.get('case_id')
        # print(case_id)
        apilist = models.apilist()
        case = models.apilist.objects.get(case_id=case_id)
        item = case.item
        release = case.release
        modules = case.modules
        casename = case.casename
        caselists = case.caselists.replace(' ', '').replace(r'\n', '')
        caselists = eval(caselists)
        x=len(caselists)-1
        # print(caselists)
        for case in caselists:
            print(caselists[case]['Casereplace'])

        return render(request, 'Dcc/caseedit.html', locals())

@csrf_exempt
@ensure_csrf_cookie
def case_update(request):
    apilist = {}
    if request.method == 'POST':
        caselist = request.POST.get('request_cases_s')
        case_ids = request.POST.get('case_ids')
        # print('case_ids',case_ids)
        caselist = caselist
        caselist = json.loads(caselist)
        case_ids = json.loads(case_ids)
    if len(caselist)>0 and len(caselist['Items_list']['Items']) and len(caselist['Items_list']['Releases']) and len(caselist['Items_list']['Moduless']) and len(caselist['Items_list']['Casenames']) and(len(caselist['caselist'])):

        item = caselist['Items_list']['Items']
        release = caselist['Items_list']['Releases']
        modules = caselist['Items_list']['Moduless']
        casename = caselist['Items_list']['Casenames']
        caselists = caselist['caselist']

        try:
            oldcase = models.apilist.objects.get(case_id=case_ids)
            oldcase.item = item
            oldcase.release = release
            oldcase.modules = modules
            oldcase.casename = casename
            oldcase.caselists = caselists
            oldcase.save()

            # print({'code': '200', 'message': '添加成功'})
            return HttpResponse(json.dumps({'code': '200', 'message': '更新成功'}))
        except:
            # print({'code': '404', 'message': '已经存在相同用例可以到用例集更新用例'})
            return HttpResponse(json.dumps({'code': '404', 'message': '更新失败'}))

    else:
        # print({'code': '404', 'message': '请检查用例，项目，迭代版本，模块，case名是必填选项'})
        return HttpResponse(json.dumps({'code': '404', 'message': '请检查用例，项目，迭代版本，模块，case名是必填选项'}))

@csrf_exempt
@ensure_csrf_cookie
def case_report(request):
    caseapi_return = {
        "code": '',
        "msg": '',
        "equipment": {
            # 0: {
            #     'phonevendorname': '111111',
            #     'phoneequipmentname': '222222',
            #     'phoneserialnumber': '333333',
            #     'phone_state': '4444444',
            # },
        }
    }
    if request.method == 'POST':
        return HttpResponse(json.dumps("我还没写完"))
    else:
        reportlist = models.reportlist()
        report = models.reportlist.objects.all()
        for index in range(len(report)):
            caseapi_return['equipment'][index] = {
                'reportclass': report[index].reportclass,
                'reportname': report[index].reportname,
                'go': report[index].report_id
            }
        # print(caseapi_return)
        return render(request, 'Dcc/report_list.html', locals())


@csrf_exempt
@ensure_csrf_cookie
def case_report_index(request):
    caseapi_return = {
        "code": '',
        "msg": '',
        "equipment": {
            # 0: {
            #     'phonevendorname': '111111',
            #     'phoneequipmentname': '222222',
            #     'phoneserialnumber': '333333',
            #     'phone_state': '4444444',
            # },
        }
    }
    if request.method == 'POST':
        report_id = request.GET.get('report_id')

        return HttpResponse(json.dumps("我还没写完"))
    else:
        report_id = request.GET.get('report_id')
        reportlist = models.reportlist()
        report = models.reportlist.objects.get(report_id=report_id)
        reportname=report.reportname
        reportclass=report.reportclass
        # print(report)
        # print(report.reportclass)
        # print(report.reportname)
        index = eval(report.report)
        # print(index)
        for n in range(len(index)):
            # print(index[n])
            caseapi_return['equipment'][n]=index[n]
        # print(caseapi_return)
        # for reports in range(len(index)):
        #     caseapi_return['equipment'][index] = {
        #         'reportclass': report[index].reportclass,
        #         'reportname': report[index].reportname,
        #         'report': report[index].report_id
        #     }
        return render(request, 'Dcc/report_index.html', locals())


@csrf_exempt
@ensure_csrf_cookie
def searchcase(request):
    apilist = {}

    if request.method == 'POST':
        Item = request.POST.get('Items')
        Release = request.POST.get('Releases')
        Modules= request.POST.get('Moduless')
        Casename = request.POST.get('Casenames')

        apilist = models.apilist()

        # print(len(Item))
        # print(len(Release))
        # print(len(Modules))
        # print(len(Casename))


        if len(Item)==0 and len(Release)==0 and len(Modules)==0 and len(Casename)==0:
            caseapi_return = {
                "code": '',
                "msg": '',
                "equipment": {
                    # 0: {
                    #     'phonevendorname': '111111',
                    #     'phoneequipmentname': '222222',
                    #     'phoneserialnumber': '333333',
                    #     'phone_state': '4444444',
                    # },
                }
            }
            case = models.apilist.objects.all()
            for index in range(len(case)):
                caseapi_return['equipment'][index] = {
                    'item': case[index].item,
                    'release': case[index].release,
                    'modules': case[index].modules,
                    'casename': case[index].casename,
                    'edit': case[index].case_id,
                    'go': case[index].case_id
                }
            # print(caseapi_return)
            return render(request, 'Dcc/caseapi_index.html', locals())
        elif len(Item)>0:
            # print("111111111111")
            caseapi_return = {
                "code": '',
                "msg": '',
                "equipment": {
                    # 0: {
                    #     'phonevendorname': '111111',
                    #     'phoneequipmentname': '222222',
                    #     'phoneserialnumber': '333333',
                    #     'phone_state': '4444444',
                    # },
                }
            }
            case = models.apilist.objects.filter(item=Item)

            for index in range(len(case)):
                caseapi_return['equipment'][index] = {
                    'item': case[index].item,
                    'release': case[index].release,
                    'modules': case[index].modules,
                    'casename': case[index].casename,
                    'edit': case[index].case_id,
                    'go': case[index].case_id
                }
            # print(caseapi_return)
            return render(request, 'Dcc/caseapi_index.html', locals())

        elif len(Release)>0:
            caseapi_return = {
                "code": '',
                "msg": '',
                "equipment": {
                    # 0: {
                    #     'phonevendorname': '111111',
                    #     'phoneequipmentname': '222222',
                    #     'phoneserialnumber': '333333',
                    #     'phone_state': '4444444',
                    # },
                }
            }
            case = models.apilist.objects.filter(release=Release)

            for index in range(len(case)):
                caseapi_return['equipment'][index] = {
                    'item': case[index].item,
                    'release': case[index].release,
                    'modules': case[index].modules,
                    'casename': case[index].casename,
                    'edit': case[index].case_id,
                    'go': case[index].case_id
                }
            # print(caseapi_return)
            return render(request, 'Dcc/caseapi_index.html', locals())

        elif len(Modules)>0:
            caseapi_return = {
                "code": '',
                "msg": '',
                "equipment": {
                    # 0: {
                    #     'phonevendorname': '111111',
                    #     'phoneequipmentname': '222222',
                    #     'phoneserialnumber': '333333',
                    #     'phone_state': '4444444',
                    # },
                }
            }
            case = models.apilist.objects.filter(modules=Modules)

            for index in range(len(case)):
                caseapi_return['equipment'][index] = {
                    'item': case[index].item,
                    'release': case[index].release,
                    'modules': case[index].modules,
                    'casename': case[index].casename,
                    'edit': case[index].case_id,
                    'go': case[index].case_id
                }
            # print(caseapi_return)
            return render(request, 'Dcc/caseapi_index.html', locals())

        elif len(Casename)>0:
            caseapi_return = {
                "code": '',
                "msg": '',
                "equipment": {
                    # 0: {
                    #     'phonevendorname': '111111',
                    #     'phoneequipmentname': '222222',
                    #     'phoneserialnumber': '333333',
                    #     'phone_state': '4444444',
                    # },
                }
            }
            case = models.apilist.objects.filter(casename=Casename)

            for index in range(len(case)):
                caseapi_return['equipment'][index] = {
                    'item': case[index].item,
                    'release': case[index].release,
                    'modules': case[index].modules,
                    'casename': case[index].casename,
                    'edit': case[index].case_id,
                    'go': case[index].case_id
                }
            # print(caseapi_return)
            return render(request, 'Dcc/caseapi_index.html', locals())


@csrf_exempt
@ensure_csrf_cookie
def searchreport(request):
    caseapi_return = {
        "code": '',
        "msg": '',
        "equipment": {
            # 0: {
            #     'phonevendorname': '111111',
            #     'phoneequipmentname': '222222',
            #     'phoneserialnumber': '333333',
            #     'phone_state': '4444444',
            # },
        }
    }
    if request.method == 'POST':
        reportclass = request.POST.get('reportclasss')
        reportname = request.POST.get('reportnames')
        reportlist = models.reportlist()

    if len(reportclass) == 0 and len(reportname) == 0:
        caseapi_return = {
            "code": '',
            "msg": '',
            "equipment": {
                # 0: {
                #     'phonevendorname': '111111',
                #     'phoneequipmentname': '222222',
                #     'phoneserialnumber': '333333',
                #     'phone_state': '4444444',
                # },
            }
        }
        case = models.reportlist.objects.all()
        for index in range(len(case)):
            caseapi_return['equipment'][index] = {
                'reportclass': case[index].reportname,
                'reportname': case[index].reportclass,
                'go': case[index].report_id
            }
        # print(caseapi_return)
        return render(request, 'Dcc/report_list.html', locals())

    if len(reportclass) > 0 :
        caseapi_return = {
            "code": '',
            "msg": '',
            "equipment": {
                # 0: {
                #     'phonevendorname': '111111',
                #     'phoneequipmentname': '222222',
                #     'phoneserialnumber': '333333',
                #     'phone_state': '4444444',
                # },
            }
        }
        case = models.reportlist.objects.filter(reportclass=reportclass)
        for index in range(len(case)):
            caseapi_return['equipment'][index] = {
                'reportclass': case[index].reportname,
                'reportname': case[index].reportclass,
                'go': case[index].report_id
            }
        # print(caseapi_return)
        return render(request, 'Dcc/report_list.html', locals())

    if len(reportname) > 0 :
        caseapi_return = {
            "code": '',
            "msg": '',
            "equipment": {
                # 0: {
                #     'phonevendorname': '111111',
                #     'phoneequipmentname': '222222',
                #     'phoneserialnumber': '333333',
                #     'phone_state': '4444444',
                # },
            }
        }
        case = models.reportlist.objects.filter(reportname=reportname)
        for index in range(len(case)):
            caseapi_return['equipment'][index] = {
                'reportclass': case[index].reportname,
                'reportname': case[index].reportclass,
                'go': case[index].report_id
            }
        # print(caseapi_return)
        return render(request, 'Dcc/report_list.html', locals())

    if len(reportclass) > 0 and len(reportname) > 0:
        caseapi_return = {
            "code": '',
            "msg": '',
            "equipment": {
                # 0: {
                #     'phonevendorname': '111111',
                #     'phoneequipmentname': '222222',
                #     'phoneserialnumber': '333333',
                #     'phone_state': '4444444',
                # },
            }
        }
        case = models.reportlist.objects.filter(reportname=reportname,reportclass=reportclass)
        for index in range(len(case)):
            caseapi_return['equipment'][index] = {
                'reportclass': case[index].reportname,
                'reportname': case[index].reportclass,
                'go': case[index].report_id
            }
        # print(caseapi_return)
        return render(request, 'Dcc/report_list.html', locals())









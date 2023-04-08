import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user import models

def userRegister(request):
    username = str(request.POST.get('username')).strip()
    password = str(request.POST.get('password')).strip()
    # print('>>>>', username)
    # print('>>>>', password)
    if username != '' and password != '' and username != None and password != None:
        filter_user = list(models.UserInfo.objects.filter(username=username).values())
        print('>>>',filter_user)
        if filter_user == []:
            models.UserInfo.objects.create(username=username, password=password)
            resp_ = {'status':'success','error_message':''}
            resp = json.dumps(resp_)
            # print('>>>>',username)
            # print('>>>>',password)
            # 编写业务:调用session保存数据,维持作用域通信...
            request.session['username'] = username
            request.session['password'] = password
            return HttpResponse(content=resp,content_type='application/json')
        resp_ = {'status': 'error','error_message':'用户已存在!!😥😥'}
        resp = json.dumps(resp_)
        return HttpResponse(content=resp, content_type='application/json')
    resp_ = {'status': 'error','error_message':'填写信息有误!请重新填写!!😑😑'}
    resp = json.dumps(resp_)
    return HttpResponse(content=resp,content_type='application/json')
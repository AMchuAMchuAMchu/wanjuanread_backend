import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user import models

#  注册功能的实现
def userRegister(request):
    username = str(request.POST.get('username')).strip()
    password = str(request.POST.get('password')).strip()
    # print('>>>>', username)
    # print('>>>>', password)
    if username != '' and password != '' and username != None and password != None:
        filter_user = list(models.UserInfo.objects.filter(username=username).values())
        # print('>>>',filter_user)
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


#  登录功能的实现
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print('>>>',username)
    print('>>>',password)
    if username != '' and password != '' and username != None and password != None:
        user_list_username = list(models.UserInfo.objects.filter(username=username))
        user_list_password = list(models.UserInfo.objects.filter(password=password))
        if user_list_username != [] and user_list_password != []:
            request.session['username'] = username
            request.session['password'] = password
            resp_ = {'status':'success','error_message_login':''}
            resp = json.dumps(resp_)
            return HttpResponse(content=resp,content_type='application/json')
        if user_list_username == []:
            resp_ = {'status': 'error', 'error_message_login': '用户不存在!!😥😥'}
            resp = json.dumps(resp_)
            return HttpResponse(content=resp,content_type='application/json')
        if user_list_username != [] and user_list_password == []:
            resp_ = {'status': 'error', 'error_message_login': '密码错误!!😂😂'}
            resp = json.dumps(resp_)
            return HttpResponse(content=resp,content_type='application/json')
    resp_ = {'status': 'error', 'error_message_login': '输入非法!!请重新输入!🥱🥱'}
    resp = json.dumps(resp_)
    return HttpResponse(content=resp,content_type='application/json')

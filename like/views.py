import json
import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from like import models


def likeData(request):
    pic_list_img = []
    pic_set = set()
    for i in range(10):
        pic = random.randint(1,110)
        # print(pic)
        pic_set.add(pic)
        # 用set去重
        if len(pic_set) == 4:
            pic_list_img = list(pic_set)
            break
    # picture = list(models.LikeData.objects.filter(pic=pic))
    picture = list(models.LikeData.objects.filter(pic__in=pic_list_img) .values())
    # res_list = json.dumps()
    # print('>>',res_list)
    # print('>>',picture)
    picture = json.dumps(picture)
    return HttpResponse(content=picture,content_type='application/json')



def allBooks(request):
    b_list = list(models.LikeData.objects.all().values())
    res = json.dumps(b_list)
    # print(res)
    return HttpResponse(content=res,content_type='application/json')
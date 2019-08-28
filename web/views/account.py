from django.shortcuts import HttpResponse,render,redirect
from rbac import models
from rbac.service.init_permission import init_permission

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    obj = models.UserInfo.objects.filter(name=user,password=pwd).first()

    if not obj:
        return render(request,'login.html',{"msg":"輸入的用戶名和密碼錯誤"})

    init_permission(obj,request)

    return redirect('/customer/list/')
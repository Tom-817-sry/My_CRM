from django.shortcuts import HttpResponse,render,redirect
from rbac import models


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    obj = models.UserInfo.objects.filter(name=user,password=pwd).first()

    if not obj:
        return render(request,'login.html',{"msg":"輸入的用戶名和密碼錯誤"})

    permission_queryset = obj.role.filter(permission__isnull=False).values("permission__id","permission__url").distinct()

    permission_list = [item['permission__url'] for item in permission_queryset]

    request.session['luffy_permission_url_list_key'] = permission_list

    return redirect('/customer/list/')
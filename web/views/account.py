from django.shortcuts import HttpResponse,render
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




    return HttpResponse('Hello!')
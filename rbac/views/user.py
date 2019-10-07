from django.shortcuts import render,HttpResponse,redirect,reverse
from rbac.forms.user import UserModeForm,UpdateUserModeForm,ResetPasswordUserModeForm
from rbac import models


def user_list(request):
    """
    角色列表
    :param request:
    :return:
    """

    user_queryset = models.UserInfo.objects.all()
    return render(request,'rbac/user_list.html',{'users':user_queryset})


def user_add(request):
    '''
    添加角色
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = UserModeForm()
        return render(request,'rbac/change.html',{'form':form})

    form = UserModeForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))

    return render(request, 'rbac/change.html', {'form': form})

def user_edit(request,pk):
    obj = models.UserInfo.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('角色不存在')

    if request.method == 'GET':
        form = UpdateUserModeForm(instance=obj)
        return render(request,'rbac/change.html',{'form':form})

    form = UpdateUserModeForm(instance=obj,data = request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))

    return render(request,'rbac/change.html',{'form':form})

def user_del(request,pk):
    """
    删除角色
    :param request:
    :param pk:
    :return:
    """
    origin_url = reverse('rbac:user_list')     #反向生成URL

    if request.method == 'GET':
        return  render(request,'rbac/delete.html',{'cancel':origin_url})

    models.UserInfo.objects.filter(id=pk).delete()
    return redirect(origin_url)


def user_ResetPassword(request,pk):
    obj = models.UserInfo.objects.filter(id=pk).first()

    if request.method == 'GET':
        form = ResetPasswordUserModeForm()
        return render(request,'rbac/change.html',{'form':form})

    form = ResetPasswordUserModeForm(instance=obj,data = request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:user_list'))

    return render(request,'rbac/change.html',{'form':form})
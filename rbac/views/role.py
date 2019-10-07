from django.shortcuts import render,HttpResponse,redirect,reverse
from rbac.forms.role import RoleModeForm
from rbac import models



def role_list(request):
    role_queryset = models.Role.objects.all()

    return render(request,'rbac/role_list.html',{'roles':role_queryset})


def role_add(request):
    '''
    添加角色
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = RoleModeForm()
        return render(request,'rbac/change.html',{'form':form})

    form = RoleModeForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))

    return render(request, 'rbac/change.html', {'form': form})

def role_edit(request,pk):
    obj = models.Role.objects.filter(id=pk).first()
    if not obj:
        return HttpResponse('角色不存在')

    if request.method == 'GET':
        form = RoleModeForm(instance=obj)
        return render(request,'rbac/change.html',{'form':form})

    form = RoleModeForm(instance=obj,data = request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('rbac:role_list'))

    return render(request,'rbac/change.html',{'form':form})

def role_del(request,pk):
    """
    删除角色
    :param request:
    :param pk:
    :return:
    """
    origin_url = reverse('rbac:role_list')     #反向生成URL

    if request.method == 'GET':
        return  render(request,'rbac/delete.html',{'cancel':origin_url})

    models.Role.objects.filter(id=pk).delete()
    return redirect(origin_url)




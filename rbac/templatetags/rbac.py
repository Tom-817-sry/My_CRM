from django.template import Library
from django.conf import settings
import re
from django.urls import reverse
from collections import OrderedDict
from django.http import QueryDict
from rbac.service import urls


register = Library()    # 必须叫register


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
    '''
    创建一级菜单
    :param request:
    :return:
    '''
    menu_list = request.session[settings.PERMISSION_MENU_SESSION_KEY]
    return {'menu_list': menu_list}

@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
    """
        创建二级菜单
        :return:
        """
    menu_dict = request.session[settings.PERMISSION_MENU_SESSION_KEY]

    # 对字典的key进行排序
    key_list = sorted(menu_dict)

    # 空的有序字典
    ordered_dict = OrderedDict()

    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'

        for per in val['children']:

            if per['id'] == request.current_selected_permission:
                per['class'] = 'active'
                val['class'] = ''
        ordered_dict[key] = val

    return {'menu_dict': ordered_dict}


    return {'menu_dict': ordered_dict}

@register.inclusion_tag('rbac/breadcrumb.html')
def breadcrumb(request):

    return {'record_list':request.breadcrumb}

@register.filter
def has_permission(request, name):
    """
    判断是否有权限，最多可以有两个参数
    :param request:
    :param name:
    :return:
    """
    permission_dict = request.session.get(settings.PERMISSION_MENU_SESSION_KEY)
    if name in permission_dict:
        return True

@register.simple_tag
def memory_url(request, name, *args, **kwargs):
    """
    生成带有原搜索条件的URL（替代了模板中的url）
    :param request:
    :param name:
    :return:
    """
    return urls.memory_url(request, name, *args, **kwargs)
from django.template import Library
from django.conf import settings
import re
from collections import OrderedDict

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
    '''
    创建二级菜单
    :param request:
    :return:
    '''
    menu_dict = request.session[settings.PERMISSION_MENU_SESSION_KEY]

    # 对字典进行有序排序
    key_list = sorted(menu_dict)

    # 空的有序字典
    ordered_dict = OrderedDict()

    print('key_list:',key_list)
    print('menu_dict:',menu_dict)
    for key in key_list:
        val = menu_dict[key]
        val['class'] = 'hide'

        for per in val['children']:
            regex = "^%s$" % (per['url'],)
            if re.match(regex, request.path_info):
                per['class'] = 'active'
                val['class'] = ''
        ordered_dict[key] = val

    print('ordered_dict:',ordered_dict)
    print('ordered_dict(type):',type(ordered_dict))
    return {'menu_dict': ordered_dict}

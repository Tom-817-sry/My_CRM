from django.conf import settings
def init_permission(obj,request):

    '''
    用户权限的初始化
    :param obj:
    :param request:
    :return:
    '''

    permission_queryset = obj.role.filter(permission__isnull=False).values("permission__id",
                                                                           "permission__url",
                                                                           "permission__is_menu",
                                                                           "permission__icon",
                                                                           "permission__title",
                                                                           ).distinct()

    menu_list = []
    permission_list = []                # 增加menu_list 来判断是否可以做菜单，是的就导入
    for item in permission_queryset:
        permission_list.append(item['permission__url'])
        if item['permission__is_menu']:
            temp = {
                'title': item['permission__title'],
                'url': item['permission__url'],
                'icon': item['permission__icon'],
            }

            menu_list.append(temp)
    # permission_list = [item['permission__url'] for item in permission_queryset]

    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.PERMISSION_MENU_SESSION_KEY] = menu_list


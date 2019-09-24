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
                                                                           "permission__title",
                                                                           "permission__name",
                                                                           "permission__pid_id",
                                                                           "permission__pid__title",
                                                                           "permission__pid__url",
                                                                           "permission__menu_id",
                                                                           "permission__menu__icon",
                                                                           "permission__menu__title",
                                                                           ).distinct()
    menu_dict = {}
    permission_dict = {}           # 增加menu_list 来判断是否可以做菜单，是的就导入



    for item in permission_queryset:
        # print('1',item['permission__title'])
        # print('2',item['permission__pid__title'])
        permission_dict[item["permission__name"]] = {'id':item['permission__id'],
                                'url':item['permission__url'],
                                'pid':item['permission__pid_id'],
                                'title':item['permission__title'],
                                'p_title':item['permission__pid__title'],
                                'p_url':item['permission__pid__url'],
                                }

        menu_id = item['permission__menu_id']
        if not menu_id:
            continue
        node = {'title': item['permission__title'], 'url': item['permission__url'],'id':item['permission__id']}
        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permission__menu__title'],
                'icon': item['permission__menu__icon'],
                'children': [node, ]
            }

    # permission_list = [item['permission__url'] for item in permission_queryset]

    #print('menu_dict:',menu_dict)

    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.PERMISSION_MENU_SESSION_KEY] = menu_dict


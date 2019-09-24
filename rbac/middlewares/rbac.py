from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from CRM import settings
import re


class RbacMiddleware(MiddlewareMixin):
    def process_request(self, request):
        '''
        1.获取当前用户请求的URL
        2.获取当前用户在session中保存的权限列表['/customer/list/',......]
        3.权限信息匹配
        :param request:
        :return:
        '''

        # 设置白名单，当用户访问时，可以使得各个用户都可以访问，无需任何权限

        current_url = request.path_info   # 获取用户请求的URL
        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)    # 获取用户在session中存在的权限列表
        for vaild_url in settings.VALID_URL_LIST:
            if re.match(vaild_url,current_url):               # 先循环白名单
                return None

        if not permission_dict:                     # 如果没有在session中，判断你是没有登陆的用户
            return HttpResponse('你还没有登陆 ')

        flag = False          # 设置flag，当匹配成功后就没有需要继续往下匹配

        url_record = [
            {'title':'首页','url':'#'}
        ]

        for name,item in permission_dict.items():
            reg = "^%s$" % item['url']
            if re.match(reg, current_url):
                flag = True
                request.current_selected_permission = item['pid'] or item['id']
                if not item['pid']:
                    url_record.extend([{'title': item['title'], 'url': item['url'], 'class': 'active'}])
                else:
                    url_record.extend([
                        {'title': item['p_title'], 'url': item['p_url']},
                        {'title': item['title'], 'url': item['url'], 'class': 'active'},
                    ])
                request.breadcrumb = url_record
                break


        if not flag:
            return HttpResponse('你没有权限未登陆')

# class RbacMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         """
#         验证用户
#         :param request:
#         :return:
#         """
#         # 1. 获取白名单，让白名单中的所有url和当前访问url匹配
#         for reg in settings.VALID_URL_LIST:
#             if re.match(reg, request.path_info):
#                 return None
#
#         # 2. 获取权限
#         permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
#         if not permission_dict:
#             return HttpResponse('无权限信息，请重新登录')
#
#         flag = False
#
#         # 3. 对用户请求的url进行匹配
#         request.current_breadcrumb_list = [
#             {'title': '首页', 'url': '#'}
#         ]
#
#         for name, item in permission_dict.items():
#             url = item['url']
#             regex = "^%s$" % (url,)
#             if re.match(regex, request.path_info):
#                 flag = True
#                 pid = item['pid']
#                 pid_name = item['pid_name']
#                 pid_url = item['pid_url']
#                 if pid:
#                     request.current_permission_pid = item['pid']
#                     request.current_breadcrumb_list.extend([
#                         {'title': permission_dict[pid_name]['title'], 'url': pid_url},
#                         {'title': item['title'], 'url': url, 'class': 'active'}
#                     ])
#                 else:
#                     request.current_permission_pid = item['id']
#                     request.current_breadcrumb_list.append(
#                         {'title': item['title'], 'url': url, 'class': 'active'}
#                     )
#                 break
#
#         if not flag:
#             return HttpResponse('无权访问')

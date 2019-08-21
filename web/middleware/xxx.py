from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re

class middle_test(MiddlewareMixin):
    def process_request(self, request):
        '''
        1.获取当前用户请求的URL
        2.获取当前用户在session中保存的权限列表['/customer/list/',......]
        3.权限信息匹配
        :param request:
        :return:
        '''

        # 设置白名单，当用户访问时，可以使得各个用户都可以访问，无需任何权限
        vaild_list = [
            '/login/',
            '/admin/*',
        ]

        current_url = request.path_info                 # 获取用户请求的URL
        permission_list = request.session.get('luffy_permission_url_list_key')    # 获取用户在session中存在的权限列表
        for vaild_url in vaild_list:
            if re.match(vaild_url,current_url):               # 先循环白名单
                return None

        if not permission_list:                     # 如果没有在session中，判断你是没有登陆的用户
            return HttpResponse('你还没有登陆 ')

        flag = False          # 设置flag，当匹配成功后就没有需要继续往下匹配

        for url in permission_list:
            reg = "^%s$" % url                              # 通过正则表达式，实现完全的匹配
            if re.match(reg,current_url):
                flag = True
                break
        if not flag:
            return HttpResponse('你没有权限未登陆')

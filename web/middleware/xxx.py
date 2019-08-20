from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class middle_test(MiddlewareMixin):
    def process_request(self, request):
        '''
        1.获取当前用户请求的URL
        2.获取当前用户在session中保存的权限列表['/customer/list/',......]
        3.权限信息匹配
        :param request:
        :return:
        '''

        current_url = request.path_info
        permission_list = request.session.get('luffy_permission_url_list_key')

        if not permission_list:
            return HttpResponse('未登陆')

        print(current_url)
        print(permission_list)
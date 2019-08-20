"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from web.views import account
from web.views import customer
from web.views import payment

urlpatterns = [
    url(r'^customer/list/$', customer.customer_list),
    # url(r'^customer/add/$', customer.customer_add),
    # url(r'^customer/edit/(?P<cid>\d+)/$', customer.customer_edit),
    # url(r'^customer/del/(?P<cid>\d+)/$', customer.customer_del),
    # url(r'^customer/import/$', customer.customer_import),
    # url(r'^customer/tpl/$', customer.customer_tpl),
    #
    # url(r'^payment/list/$', payment.payment_list),
    # url(r'^payment/add/$', payment.payment_add),
    # url(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit),
    # url(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del),
    # url(r'^login/$', account.login),
    url(r'^login$',account.login)
]

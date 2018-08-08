"""mysite6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from account import views
from django.contrib.auth import views as auth_views
app_name = 'account'

urlpatterns = [
    # url('admin/', admin.site.urls),
    # url('^blog/', include('blog.urls',namespace='blog')),
    url(r'^login/$', auth_views.login,
        {'template_name':"account/login.html"},
        name='user_login'),

    url(r'^logout/$', auth_views.logout,
        {'template_name':"account/logout.html"},
        name='user_logout'),

    url(r'^register/$', views.register,name='user_register'),



    url(r'^password-change/$',
        auth_views.password_change,
        {
            'template_name': 'account/password_change_form.html',
            'post_change_redirect':'/account/password-change-done',
        },
        name='password_change'),

    url(r'^password-change-done/$',
        auth_views.password_change_done,
        {'template_name':'account/password_change_done.html',},
        name='password_change_done'),

    url(r'^password-reset/$',
        auth_views.password_reset,
        {
            'template_name':'account/password_reset_form.html',
            'email_template_name':'account/password_reset_email.html',
            'subject_template_name':'account/password_reset_subject.txt',
            'post_reset_redirect':'/account/password-reset-done',
         },
        name='password_reset'),

    url(r'^password-reset-done/$',
        auth_views.password_reset_done,
        {'template_name':'account/password_reset_done.html',},
        name='password_reset_done'),

    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.password_reset_confirm,
        {
            'template_name':'account/password_reset_confirm.html',
            'post_reset_redirect': '/account/password-reset-complete',
        },
        name='password_reset_confirm'),

    url(r'^password-reset-complete/$',
        auth_views.password_reset_complete,
        {'template_name':'account/password_reset_complete.html',},
        name='password_reset_complete'),

    url(r'^my-information/$',views.myself,name='my_information'),

    url(r'^edit-my-information/$',views.myself_edit,name='edit_my_information'),

    url(r'^my-image/$',views.my_image,name='my_image'),
]

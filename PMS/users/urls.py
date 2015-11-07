from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^users/login/$', views.user_login, name='login'),
        url(r'^users/home/$', views.admin_home, name='home'),
        url(r'^users/logout/$', views.user_logout, name='logout'),
        )
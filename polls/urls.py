# from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib import admin
urlpatterns = [
    url('api/polls/', views.TodoEvenListCreate.as_view() ),
    url('index', views.index, name='index'),
    url(r'^(?P<todoEven_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<todoEven_id>[0-9]+)/id/$', views.id, name='id'),
    url('admin/', admin.site.urls),
]

    # url('user=<int:userId>/', views.TodoEvenListCreate.as_view()),
    # url('user=<int:userId>/edit', views.TodoEvenListCreate.as_view()),
    # url('login/', views.UserListCreate.as_view() )
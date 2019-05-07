from django.conf.urls import url
from . import views
urlpatterns = [
    url('react_table', views.index ),
]
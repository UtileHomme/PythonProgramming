from django.conf.urls import url
from testApp import views

urlpatterns=[
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)S', views.departmentApi)
]
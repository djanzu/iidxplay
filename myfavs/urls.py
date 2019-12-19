from django.urls import path, re_path
from . import views

app_name = 'myfavs'

urlpatterns = [
    re_path('^$', views.Top.as_view(), name='top'),
    re_path(r"^login/$", views.Login.as_view(), name='login'),
    re_path(r"^logout/$", views.Logout.as_view(), name='logout'),
]

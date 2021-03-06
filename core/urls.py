from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('register/categories/', views.category_list, name='category-list'),
    path('register/messages/', views.message_list, name='message-list'),
    path('register/workers/', views.worker_list, name='worker-list'),
]

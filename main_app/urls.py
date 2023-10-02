from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('posts/', views.posts_index, name='index'),
  path('posts/<int:post_id>/', views.posts_detail, name='detail')

]

from django.urls import path
from . import views
urlpatterns = [
    # path('hello/', views.hello, name ='hello'),
    path('post',views.blog_all,name='posts'),
    path('posts/<int:id>/', views.blog_detail_view, name='detail'),
    path('add-tv/',views.create_post_view, name='create')

]
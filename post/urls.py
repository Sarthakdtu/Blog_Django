from django.urls import path
from post import views


urlpatterns = [
     path('', views.post_list, name='post_list'), 
     #path('create', views.create_post, name='create_post'),
     path('post/<int:post_id>', views.view_post, name='view_post'),
     path('category/<slug:category_name>', views.post_list, name='post_list_category'),
     path('search', views.search, name='search'),
    
    
]

from django.urls import path
from . import views

urlpatterns = [ # 서버IP/blog
#    path('<int:pk>/', views.post_detail),
#    path('', views.post_list),   

    path('tag/<str:slug>', views.tag_page), #서버IP/blog/tag/slug
    path('category/<slug>', views.category_page),   # 서버IP/blog/category/slug
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]
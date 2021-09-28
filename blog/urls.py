from django.urls import path
from . import views

urlpatterns = [ # 서버IP/blog
#    path('<int:pk>/', views.post_detail),
#    path('', views.post_list),   

    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]
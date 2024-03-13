from django.urls import path
from .views import  PostListView, PublishPostView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/', PublishPostView.as_view(), name='update_post'),
    path('post/<int:post_id>/', PublishPostView.as_view(), name='update_post'),

]

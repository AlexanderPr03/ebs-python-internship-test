from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, BlogItemCreate, CommentItemView, CommentItemCreate, CommentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create', BlogItemCreate.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('<int:pk>/comments/', CommentListView.as_view(), name='comments_list'),
    path('comment/create', CommentItemCreate.as_view(), name='comment_create'),
]

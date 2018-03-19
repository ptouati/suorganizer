from django.urls import path

from .views import PostList, post_detail, PostCreate, PostUpdate

urlpatterns = [
    path(r'', PostList.as_view(template_name='blog/post_list.html'), name='blog_post_list'),
    path(r'<year>/' r'<month>/' r'<slug>/', post_detail, {'parent_template': 'base.html'},
         name='blog_post_detail'),
    path(r'<year>/' r'<month>/' r'<slug>/' r'update/', PostUpdate.as_view(), name='blog_post_update'),
    path(r'<year>/' r'<month>/' r'<slug>/' r'delete/', PostDelete.as_view(), name='blog_post_delete'),
    path(r'create/', PostCreate.as_view(), name='blog_post_create'),
]

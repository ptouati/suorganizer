from django.urls import path

from .views import PostList, post_detail

urlpatterns = [
    path(r'', PostList.as_view(template_name='blog/post_list.html'), name='blog_post_list'),
    path(r'<year>/' r'<month>/' r'<slug>/', post_detail, {'parent_template': 'base.html'},
         name='blog_post_detail'),
]

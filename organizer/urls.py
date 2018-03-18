from django.urls import path


from .views import (startup_list, startup_detail, tag_detail, tag_list, TagCreate, StartupCreate, NewsLinkCreate,
                    TagUpdate, StartupUpdate, NewsLinkUpdate)


urlpatterns = [
    path(r'startup/', startup_list, name='organizer_startup_list'),
    path(r'startup/create/', StartupCreate.as_view(), name='organizer_startup_create'),
    path(r'startup/<slug>/', startup_detail, name='organizer_startup_detail'),
    path(r'startup/<slug>/update/', StartupUpdate.as_view(), name='organizer_startup_update'),
    path(r'tag/', tag_list, name='organizer_tag_list'),
    path(r'tag/create/', TagCreate.as_view(), name='organizer_tag_create'),
    path(r'tag/<slug>/', tag_detail, name='organizer_tag_detail'),
    path(r'tag/<slug>/update/', TagUpdate.as_view(), name='organizer_tag_update'),
    path(r'newslink/create/', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    path(r'newslink/update/<pk>/', NewsLinkUpdate.as_view(), name='organizer_newslink_update'),
]

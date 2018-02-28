from django.urls import path


from .views import startup_list, startup_detail, tag_detail, tag_list


urlpatterns = [
    path(r'startup/', startup_list, name='organizer_startup_list'),
    path(r'startup/<slug>/', startup_detail, name='organizer_startup_detail'),
    path(r'tag/', tag_list, name='organizer_tag_list'),
    path(r'tag/<slug>/', tag_detail, name='organizer_tag_detail')
]

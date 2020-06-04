from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/posts/(?P<pk>[0-9]+)$',
        views.get_delete_update_post,
        name='get_delete_update_post'
    ),
    url(
        r'^api/v1/posts/$',
        views.get_post_post,
        name='get_post_post'
    )
]

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url('^$',views.posts_of_day,name='postsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_posts,name = 'pastposts'),
    url(r'^new/post', views.new_post, name='new-post')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
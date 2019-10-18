from django.conf.urls import url
from . import views



urlpatterns=[
    url('',views.posts_of_day,name='postsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_posts,name = 'pastposts')
]
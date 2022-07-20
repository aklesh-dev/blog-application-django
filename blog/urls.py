from django import views
from django.urls import path
from . import views
from .feeds import LatestPostsFeed

# an application namespace with the app_name variable.
# this allows us to organize URLs by application and use the name when referring to them.
app_name = 'blog'

urlpatterns = [
    # post views tag/<slug:tag_slug>/
    path('', views.post_list, name='post_list_by_tag'),
    # cbv postListView
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_details'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search')
]

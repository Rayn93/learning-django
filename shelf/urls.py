from django.conf.urls import url
from shelf.views import AuthorListView, AuthorDetailView


# app_name = 'shelf'
urlpatterns = [
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='author-detail'),
]

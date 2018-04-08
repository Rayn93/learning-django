from django.conf.urls import url
from shelf.views import AuthorListView, AuthorDetailView, BookListView, BookDetailView

# app_name = 'shelf'
urlpatterns = [
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^ksiazki/$', BookListView.as_view(), name='book-list'),
    url(r'^ksiazka/(?P<pk>[0-9]+)/$', BookDetailView.as_view(), name='book-detail'),

]


from django.urls import path,re_path
from . import views

app_name='book'
urlpatterns = [
    path('',views.index,name='index'),
    re_path(r'^list/$',views.BookListView.as_view(),name='bookList'),
    re_path(r'^detail/(?P<pk>\d+)/$',views.BookDetailView.as_view(),name='bookDetail'),
]
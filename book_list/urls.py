from django.urls import path

from . import views

app_name = 'book_list'
urlpatterns = [
    path('', views.IndexView.as_view(), name='base'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
]
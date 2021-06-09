from django.urls import path

from . import views

app_name = 'book_list'
urlpatterns = [
    path('', views.IndexView.as_view(), name='base'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book_create/', views.BookCreateView.as_view(), name='book_create'),
    path('book_delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
]
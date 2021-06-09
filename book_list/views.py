from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'base.html'


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 10

    def get_queryset(self):
        books = Book.objects.filter(user=self.request.user).order_by('-created_at')
        return books

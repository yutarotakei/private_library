from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .forms import BookCreateForm
from django.urls import reverse_lazy


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


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    template_name = 'book_create.html'
    form_class = BookCreateForm
    success_url = reverse_lazy('book_list:book_list')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list:book_list')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


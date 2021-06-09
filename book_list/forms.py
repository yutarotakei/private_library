from django import forms
from .models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'photo', 'ISBN',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title'}),
            'author': forms.TextInput(attrs={'placeholder': 'author'}),
            'ISBN': forms.TextInput(attrs={'placeholder': 'ハイフンなしで入力してください'}),
        }

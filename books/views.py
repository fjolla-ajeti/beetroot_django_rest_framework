# Importing the necessary modules
from django.views.generic import ListView
from .models import Book

# Creating a class-based view for the home page
class HomeBookView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'all_books_list'

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from .models import *

# Create your views here.
class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 4

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()

    if request.method == 'POST':
        comment_form = commentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = commentForm()
    else:
        comment_form = commentForm()

    context = {
        'book' : book,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'books/book_detail.html', context)


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'content', 'price' , 'covers']
    template_name = 'books/book_create.html'

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'content', 'price', 'covers']
    template_name = 'books/book_update.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list') # Redirect to Index page

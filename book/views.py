from django.shortcuts import render

from .models import Book,BookInstance,Author,Genre

from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.all().count()
    context={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_author':num_author,
    }
    return render(request,'book/index.html',context)

class BookListView(LoginRequiredMixin,generic.ListView):
    model = Book
    paginate_by = 5

class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book

class LoanedBookByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name = 'book/bookinstance_list_borrower_user.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
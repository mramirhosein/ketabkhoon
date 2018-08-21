from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse



from .models import Book,BookInstance,Author,Genre
from .forms import RenewBookForm

from django.views import generic

import datetime

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

class BookBorrowListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name = 'book/book_borrows.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.all().filter(status__exact='o').order_by('due_back')


class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book



class LoanedBookByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name = 'book/bookinstance_list_borrower_user.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

    
@login_required
def renew_book_librarian(request,pk):
    bookinst = get_object_or_404(BookInstance, pk = pk)

    if request.method == 'POST':
        form = RenewBookForm(request.POST)

        if form.is_valid():
            bookinst.due_back = form.cleaned_data['renewal_data']
            bookinst.save()

            return HttpResponseRedirect(reverse('book:allBorrowed'))
    
    else:
        proposed_renewal_data = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookForm(initial={'renewal_data':proposed_renewal_data})

    context = {
        'form':form,
        'bookinst':bookinst,
    }
    return render(request,'book/book_renewal_librarian.html',context)


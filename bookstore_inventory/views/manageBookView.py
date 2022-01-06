from django.shortcuts import render, redirect
from bookstore_inventory.models import Book


def list_create_view(request):
    if request.method == 'GET':
        queryset = Book.objects.all()

        return render(request, 'crud/manage_books.html',
                      context={'books': queryset})
    elif request.method == 'POST':
        book_data = {
            'title': request.POST["title"],
            'author': request.POST["author"],
            'editorial': request.POST["editorial"],
            'gender': request.POST["gender"],
            'pub_date': request.POST["pub_date"],
            'num_pages': request.POST["num_pages"],
        }

        Book.objects.create(**book_data)

        return redirect("/book/")


def delete_view(request, pk):
    Book.objects.filter(pk=pk).delete()
    return redirect("/book/")


def update_view(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)

        return render(request, 'crud/edit_books.html',
                      context={'book': book})
    elif request.method == 'POST':
        book_data = {
            'title': request.POST["title"],
            'author': request.POST["author"],
            'editorial': request.POST["editorial"],
            'gender': request.POST["gender"],
            'pub_date': request.POST["pub_date"],
            'num_pages': request.POST["num_pages"],
        }

        Book.objects.filter(pk=pk).update(**book_data)
        return redirect("/book/")

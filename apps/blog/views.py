from django.shortcuts import render
def index(request):
    return render(request, "index.html") 
def list_books(request):
    return render(request, 'list_books.html')
def viewbook(request, bookId):
    return render(request, 'one_book.html')
def aboutus(request):
    return render(request, 'aboutus.html')
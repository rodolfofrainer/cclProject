from django.shortcuts import render

def customers(request):
    """ A view to return the index page """

    return render(request, 'customers/index.html')
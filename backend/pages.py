from django.shortcuts import render

def some_view(request):
    return render(request, './page1.html')
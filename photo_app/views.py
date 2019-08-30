from django.shortcuts import render

# Create your views here.

def user_page(request):
    if request.method == 'GET':
        return render(request, 'user_page.html')

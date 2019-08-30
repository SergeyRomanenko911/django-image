from django.shortcuts import render
from django.http import HttpResponseRedirect

from photo_app.models import Picture

# Create your views here.

def user_page(request):
    if request.method == 'GET':
        pictures = Picture.objects.all()
        return render(request, 'user_page.html', {'pictures': pictures})
    elif request.method == 'POST':
        picture = Picture(description = request.POST['description'], field = request.FILES['picture'])
        picture.save()
        return HttpResponseRedirect('/user')

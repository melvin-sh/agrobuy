from django.shortcuts import render

# Create your views here.

def req(request):

    return render(request, 'ml/show.html',{})
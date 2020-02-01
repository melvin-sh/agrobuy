from django.shortcuts import render , HttpResponse
from farmer.models import Farmer
# Create your views here.

def see(request):
    farm = None
    farm = Farmer.objects.all()
    
    
    return render(request,
                  'farmer/farmerdb.html',
                  {'farm':farm})
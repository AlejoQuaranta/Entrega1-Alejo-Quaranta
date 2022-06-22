from django.shortcuts import render
from familia.models import Family


# Create your views here.
def family(request):
        familia = Family.objects.all()
        context = {'familia':familia}
        return render(request, 'family.html', context=context)
from django.shortcuts import render
from .models import *
def index(request):
    records=Record.objects.all()
    context={'records':records}
    return render(request, 'web/index.html', context)

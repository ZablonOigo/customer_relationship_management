from django.shortcuts import render
from .models import *
from django.db.models import Q
def index(request):
    records=Record.objects.all()
    departments=Department.objects.all()
    context={'records':records,
             'departments':departments
             }
    return render(request, 'web/index.html', context)

def search_field(request):
    query=request.GET.get('query','')
    department_id=request.GET.get('department',0)
    departments=Department.objects.all()
    records=Record.objects.all()
    if department_id:
        departments=departments.filter(department_id=department_id)
    if query:
        records=records.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query))
            
    return render(request, 'web/staff.html',{
        'query':query,
        'department_id':int(department_id),
        'departments':departments,
        ' records': records,
    })
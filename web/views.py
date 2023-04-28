from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
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




def create(request):
    if request.method =="GET":
        form=RecordForm()
        return render(request, 'web/create.html',{'form':form} )
    elif request.method == 'POST':
        form=RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New record has been added successfully")
            return redirect('web:index')
        else:
            return render(request, 'web/create.html', {'form':form})
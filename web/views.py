from django.shortcuts import render, redirect,get_object_or_404
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
        

def edit(request,id):
    record=get_object_or_404(Record, id=id)

    if request.method == 'GET':
        form=RecordForm(instance=record)
        context={'form':form,
                 'id':id}
        return render(request, 'web/create.html', context)
    elif request.method =="POST":
        form=RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "the record has been edited successfully")
            return redirect('web:index')
        else:
            return render(request,'web/create.html',{'form:form'})
        



def delete_record(request, id):
    record=get_object_or_404(Record, id=id)
    context={'record':record}
    if request.method == "GET":
        return render(request,'web/delete.html', context)
   
    elif request.method == "POST":
        record.delete()
        messages.success(request, 'The record has been deleted successfully')
        return redirect('web:index')


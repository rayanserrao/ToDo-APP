from django.shortcuts import render,redirect
from mytodo.models import ToDo
from mytodo.forms import ToDoform
from django.contrib import messages

# Create your views here.
def index(request):
    obj_list=ToDo.objects.all()  # to get all data
    title='home ' 
    form=ToDoform()
    context={'obj_list':obj_list,'title':title,'form':form}
    return render(request,'index.html',context)


def todo_add(request):
    if request.method =='POST':
        # todo=request.POST.get('todo_text')
        # ToDo.objects.create(title=todo)

        form=ToDoform(request.POST)
        if form.is_valid():
            todo=form.cleaned_data.get('todo_text')
            ToDo.objects.create(title=todo)
            messages.success(request,"Todo added succesfully")


        
    return redirect('index')


def todo_delete(request,del_id):
    if request.method =='POST':
        todo_obj=ToDo.objects.get(pk=del_id)
        todo_obj.delete()
        messages.info(request,"Todo deleted successfully")

    return redirect('index')


def todo_edit(request,edit_id):
    todo_obj=ToDo.objects.get(pk=edit_id)
    if request.method=='POST':
        form=ToDoform(request.POST)
        if form.is_valid():
            todo_obj.title = form.cleaned_data.get('todo_text')
            todo_obj.save()
            messages.success(request,"ToDo edited successfully")
            return redirect('index')
    
    
    
    form=ToDoform(initial={'todo_text':todo_obj.title})
    context={'form':form,'todo_obj':todo_obj}
    return render(request,'edit.html',context)


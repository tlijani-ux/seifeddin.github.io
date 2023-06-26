from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
# function define index---> retuyrn template fichier html

# temchi lel les object task tamlhom stocks f tasks
def index(request):

    tasks = Task.objects.all()

    if request.method=='POST':
        if "addtask" in request.POST:
         new_task_name=request.POST['taskName']

         new_task=Task(name=new_task_name)
         new_task.save()
         return redirect('index')
       
    context=  {'all_tasks':tasks}

    return render(request,'todo/index.html',context )

#def about(request):
 #  return render(request,'todo/about.html')


#def Delete_task(request,task_id):
 # task=Task.objects.get(id=task_id)
  #task.delete()  #delete the task
  #return redirect('index')


def complete_task(request,task_id):
   task=Task.objects.get(id=task_id)
   task.completed=True
   task.save()
   return redirect('index')

def delete_completed(request):
    taskcompleted=Task.objects.filter(completed=True)
    taskcompleted.delete()
    return redirect('index')

def delete_all(request):
    tasks=Task.objects.all()
    tasks.delete()
    return redirect('index')





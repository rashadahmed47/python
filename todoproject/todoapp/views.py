from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import UpdateView,DeleteView

class homeView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'
class detailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class updateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','date','priority')

    def get_success_url(self):
        return reverse_lazy('detailView',kwargs={'pk':self.object.id})
class deleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('homeView')

# Create your views here.

def add(request):
    tasks=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'tasks':tasks})
def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,taskid):
    task = Task.objects.get(id=taskid)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TaskForm
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView,DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin




class TaskDview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'detk'


class updatwview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'updtk'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvd',kwargs={'pk':self.object.id})

class Deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbv')




def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        age= request.POST.get('age', '')
        task = Task(name=name, dob=dob, gender=gender, age=age)
        task.save()
    return render(request, 'home.html', {'task1': task1})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('view')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TaskForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('view')
    return render(request, 'edit.html', {'f': f, 'task': task})
def view(request):

    return render(request, "index.html")
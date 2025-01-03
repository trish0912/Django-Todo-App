from django.shortcuts import render, redirect
#from .forms import TodoForm
from .models import Todo
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class TodoListView(ListView):
    model = Todo
    paginate_by = 3
    
    def get_queryset(self): 
        search = self.request.GET.get('search', '') 
        task = Todo.objects.filter(title__icontains=search).order_by('-date')
        if not task:
            messages.info(self.request, 'Sorry, no data available. Please create a task!')
        return task
 
class ItemCreate(CreateView):
    model = Todo
    fields = ['title','description', 'date']
    success_url = '/about'

 
class todoupdateview(UpdateView):
    model = Todo
    fields = ['title','description', 'date']
    success_url = '/about'

    
class tododeleteview(DeleteView):
    model = Todo
    success_url = '/about'

def about(request):
    return render(request, 'todo/home.html')





    
    

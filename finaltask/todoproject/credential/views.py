from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from todoapp.models import Task
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')



def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first name']
        secondname = request.POST['last name']
        email = request.POST['email']
        passw1 = request.POST['psw']
        passw2 = request.POST['psw-repeat']

        if passw1 == passw2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Already exist user name")
                return redirect('registration')

            elif User.objects.filter(email=email).exists():
              messages.info(request, "Already exist email")
              return redirect('registration')

            else:
             user =User.objects.create_user(username=username, password=passw1, email=email, first_name=firstname,
                                        last_name=secondname)

             user.save();
             return redirect('login')


        else:
            messages.info(request,"paasswrd no mtch")
            return redirect('registration')
        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('view')

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        age= request.POST.get('age', '')
        materials=request.POST.get('materials', '')
        materialss = request.POST.get('materialss', '')
        materialsq = request.POST.get('materialsq', '')
        account=request.POST.get('account', '')
        email=request.POST.get('email', '')
        subject=request.POST.get('subject', '')
        topic=request.POST.get('topic', '')
        txt=request.POST.get('txt', '')
        phone=request.POST.get('phone', '')




        task = Task(name=name, dob=dob, gender=gender, age=age,materials=materials,account=account,email=email,subject=subject,topic=topic,txt=txt,phone=phone,materialsq=materialsq,materialss=materialss)
        task.save()
        messages.success(request, 'Submitted the form.')
    return render(request, 'home.html', {'task1': task1})
class Taskview(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'taskk'
    login_url = "home"

    def get_queryset(self):
        return self.request.User.taskk.all()
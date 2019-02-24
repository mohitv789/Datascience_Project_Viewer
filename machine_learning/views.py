from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MachineLearning
from django.utils import timezone

# Create your views here.
def machinelearning(request):
    projects = MachineLearning.objects
    return render(request , 'machine_learning/machine_learning.html', {'projects':projects})
#

@login_required(login_url = "accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.POST['code'] and request.FILES['output']:
            project = MachineLearning()
            project.title = request.POST['title']
            project.body = request.POST['body']
            if request.POST['url'].startswith("http://") or request.POST['url'].startswith("https://"):
                project.url = request.POST['url']
            else:
                project.url = "http://" + request.POST['url']
            project.code = request.POST['code']
            project.output = request.FILES['output']
            project.post_date = timezone.datetime.now()
            project.site_user = request.user
            project.save()
            return redirect('/machine_learning/' + str(project.id))
        else:
            return render(request , 'machine_learning/create.html',{'error':'All fields are required.'})
    else:
        return render(request , 'machine_learning/create.html')

def detail(request , machine_learning_id):
    project = get_object_or_404(MachineLearning , pk = machine_learning_id)
    return render(request,'machine_learning/detail.html', {'project':project})

def home(request):
    return render(request , 'machine_learning/home.html')

def about(request):
    return render(request , "machine_learning/about.html")

def guide(request):
    return render(request , "machine_learning/guide.html")

def contact(request):
    return render(request , "machine_learning/contact.html")

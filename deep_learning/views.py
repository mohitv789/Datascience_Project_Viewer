from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DeepLearning
from django.utils import timezone

# Create your views here.

@login_required(login_url = "accounts/signup")
def dl_create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.POST['code'] and request.FILES['output']:
            project = DeepLearning()
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
            return redirect('/deep_learning/' + str(project.id))
        else:
            return render(request , 'deep_learning/create.html',{'error':'All fields are required.'})
    else:
        return render(request , 'deep_learning/create.html')


def detail2(request , deep_learning_id):
    project = get_object_or_404(DeepLearning , pk = deep_learning_id)
    return render(request,'deep_learning/detail.html', {'project2':project})

def deeplearning(request):
    projects = DeepLearning.objects
    return render(request , 'deep_learning/deep_learning.html', {'projects2':projects})

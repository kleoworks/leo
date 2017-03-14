from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
        'description': Description.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    if len(request.POST['name']) < 2:
        messages.error(request, 'Enter valid course name')
        return redirect('/')

    context = {
        'name': request.POST['name'],
        'description': request.POST['description']
    }

    course = Course.objects.create(name=context['name'])
    Description.objects.create(description=context['description'], course=course)

    return redirect('/')

def destroy(request, id):
    if request.method == 'GET':
        context = {
            'id': id,
            'course': Course.objects.get(id=id)
        }
        return render(request, 'courses/confirm_delete.html', context)

    else:
        Course.objects.get(id=id).delete()
        return redirect('/')

from django.shortcuts import render

# Create your views here.
from .models import Equipment,Parameter,Var

def equipments(request):
    context = {
        'equipments1':Equipment.objects.filter(condition_code__startswith='OPERATING'),
        'equipments2':Equipment.objects.filter(condition_code__startswith='UNAVAILABLE'),
        'equipments3':Equipment.objects.filter(condition_code__startswith='IDLE'),
    }
    return render(request, 'blog/equipments.html', context)

def eq1(request):
    context = {
        'eq1':Equipment.objects.filter(condition_code__startswith='OPERATING'),
    }
    return render(request, 'blog/equipments_op.html', context)
def eq2(request):
    context = {
        'eq2':Equipment.objects.filter(condition_code__startswith='UNAVAILABLE'),
    }
    return render(request, 'blog/equipments_un.html', context)
def eq3(request):
    context = {
        'eq3':Equipment.objects.filter(condition_code__startswith='IDLE'),
    }
    return render(request, 'blog/equipments_id.html', context)

def eq(request):
    return render(request, 'blog/eq_stat.html')

def parameters(request):
    context = {
        'parameters': Parameter.objects.all()
    }
    return render(request, 'blog/parameter.html', context)

def vars(request):
    context = {
        'vars': Var.objects.all()
    }
    return render(request, 'blog/var_list.html', context)

def home(request):
    return render(request, 'blog/home.html')

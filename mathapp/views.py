from django.shortcuts import render

# Create your views here.

def mathvolume(request):
    context = {}
    return render(request, 'mathapp/mathvolume.html', context)

def matharea(request):
    context = {}
    return render(request, 'mathapp/matharea.html', context)
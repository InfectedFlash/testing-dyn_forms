from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import DynamicForm
from .models import Inputs
import json

def index(request):
    form = DynamicForm()
    if request.method == "POST":
        form = DynamicForm(request.POST)
        if form.is_valid():
            text = {}
            for name, value in request.POST.items():
                if name.startswith('text'):
                    text[name] = value
            new_data = Inputs(input_data=text)
            new_data.save()
            return render(request, 'answer.html', {"text":text})
        else:
            form = DynamicForm()
    return render(request, 'index.html', {"form":form})
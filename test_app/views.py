from django.shortcuts import render
from django.http import JsonResponse
from .forms import EditorTestForm
from .models import Blog


# Create your views here.

def editor_md_test(request):
    if request.method == "POST":
        form = EditorTestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(dict(success=1, message="submit success!"))
        else:
            return JsonResponse(dict(success=0, message="submit error"))
    else:
        form = EditorTestForm()
        return render(request, 'test.html', {'form': form})


def edit_test(request):
    if request.method == "GET":
        b = Blog.objects.last()
        form = EditorTestForm(instance=b)
        return render(request, 'test.html', {'form': form})
    if request.method == "POST":
        form = EditorTestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(dict(success=1, message="submit success!"))
        else:
            return JsonResponse(dict(success=0, message="submit error"))


def show_test(request):
    if request.method == "GET":
        b = Blog.objects.last()
        form = EditorTestForm(instance=b)
        return render(request, 'show_test.html', {'form': form})

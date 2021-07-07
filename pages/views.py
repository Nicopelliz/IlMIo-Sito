from django.shortcuts import render

# def bio(request):
#     return render(request, 'biography.html')


def home(request):
    return render(request, 'home.html')


def music(request):
    return render(request, 'music_page.html')


def crypto(request):
    return render(request, 'under-construction.html')


def coding(request):
    return render(request, 'under-construction.html')


def projects(request):
    return render(request, 'coming-soon.html')


def organic(request):
    return render(request, 'under-construction.html')

from django.shortcuts import render

def home(request):
    return render(request, "Index.html", {})

def testpage(request):
    return render(request, "test.html", {})

def thankspage(request):
    return render(request, "thanks.html", {})

from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

    # You can use 'home.html' also but if project is big then 
    # there will be lot of templates and we might end up with 
    # more than one template with same name.
    # To avoid that make new directory inside templates directory.

def contact(request):
    return render(request, 'personal/contact.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'list.html', {'contacts': contacts})

def contact_detail(request, pk):
    pass

def contact_new(request):
    pass

def contact_edit(request, pk):
    pass

def contact_delete(request, pk):
    pass
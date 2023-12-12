from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'list.html', {'contacts': contacts})

def contact_detail(request, pk):
    pass

def contact_new(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'create.html', {'form': form})

def contact_edit(request, pk):
    pass

def contact_delete(request, pk):
    pass
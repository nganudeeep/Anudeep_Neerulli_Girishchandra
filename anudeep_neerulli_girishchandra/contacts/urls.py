# contacts/urls.py
from django.urls import path
from .views import contact_list, contact_new

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('contact/new/', contact_new, name='contact_new'),

]

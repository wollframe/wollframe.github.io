from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from . import forms
from .forms import Cl, OrderForm

def index(request):

    form = forms.Cl()
    context = {
        'form': form,
        }

    return render (request, 'traffic/index.html', context)


class BbCreateView(CreateView):
    template_name = 'traffic/create.html'
    form_class = OrderForm
    success_url = reverse_lazy('index')


def price (request):
    form = forms.Cl()
    context = {
        'form': form,
        }

    if request.method == "POST":
        form = forms.Cl(request.POST)
        if form.is_valid():
            print("Result")
            ml = (form.cleaned_data['km'])
            result = ml*16+150

            return render (request, 'traffic/detail.html', {'result': result})

    return render (request, 'traffic/price.html', context)

def contacts (request):
    
    return render (request, 'traffic/contacts.html')

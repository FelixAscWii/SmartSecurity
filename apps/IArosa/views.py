from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, TemplateView, UpdateView

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from unipath import Path

# Create your views here.
class NameView(TemplateView):
    # la nueva direccion de los template es Album/----.html
    template_name = 'example.html'

class Map1View(ListView):
    template_name = 'IAmap.html'
    context_object_name = 'maps'

    def get_queryset(self):
        pkMonth = self.kwargs['month']
        pkYear = self.kwargs['year']
        # peticion o logica
        alc = []
        for x in range(16):
            alc.append(['alcadia1', x+1])
        query = ['anio', 'mes', alc]
        return query

def error_404_view(request, exception):
    return render(request, 'index/page404.html')
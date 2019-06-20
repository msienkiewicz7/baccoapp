# from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sandwich
from .forms import SandwichForm

# Create your views here.
class SandwichListView(ListView):
    model = Sandwich
    context_object_name = "all_sandwiches"

    def get_context_data(self, **kwargs):
        context = super(SandwichListView, self).get_context_data(**kwargs)
        context['sandwich_list'] = Sandwich.objects.all()
        return context


class SandwichDetailView(DetailView):
    model = Sandwich
    context_object_name = "sandwich"

    def get_context_data(self, **kwargs):
        context = super(SandwichDetailView, self).get_context_data(**kwargs)
        context['sandwich_list'] = Sandwich.objects.all()
        return context


def add_sandwich(request):
    if request.method == 'POST':
        form = SandwichForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SandwichForm()

    # return render(request, 'sandwiches/sandwich_add.html', {'form': form})
    return render(request, '../templates/mysandwich.html', {'form': form})

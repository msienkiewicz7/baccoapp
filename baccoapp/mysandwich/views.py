# from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Sandwich
from .forms import SandwichForm
from .models import Ingredient
# from .forms import IngredientForm

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

class SearchResultsView(ListView):
    model = Sandwich
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Sandwich.objects.filter(
            Q(name__icontains = query) |
            Q(ingredients__name__icontains = query)

        ).distinct()

class MySandwich(ListView):
    model = Sandwich



# def add_sandwich(request):
#     if request.method == 'POST':
#         form = SandwichForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = SandwichForm()
#
#     # return render(request, 'sandwiches/sandwich_add.html', {'form': form})
#     # context = IngredientsListView.get_context_data(IngredientsListView.context_object_name)
#     return render(request, 'mysandwich/mysandwich.html', {'form': form})


def add_sandwich(request):
    if request.method == 'POST':
        form = SandwichForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            ingredients = form.data['all_selected_ingredient_ids'] # When I used cleaned_data, the string is omitted
            ingredient_ids = ingredients.split(',')
            sandwich = Sandwich(name = name, price = price)
            sandwich.save() # Must save once first, otherwise cannot add ingredients
            for ingredient_id in ingredient_ids:
                sandwich.ingredients.add(Ingredient.objects.get(id=ingredient_id))
            sandwich.save() # Save again with all the ingredients
    else:
        form = SandwichForm()

    return render(request, 'mysandwich/mysandwich.html', {'form': form})


class IngredientsListView(ListView):
    model = Ingredient
    context_object_name = "all_ingredients"

    def get_context_data(self, **kwargs):
        context = super(IngredientsListView, self).get_context_data(**kwargs)
        context['ingredient_list'] = Ingredient.objects.all()
        return context

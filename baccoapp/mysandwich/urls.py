from django.urls import path
from .views import SandwichListView
from .views import SandwichDetailView
from .views import add_sandwich
from .views import SearchResultsView
from .views import IngredientsListView

# from . import views

urlpatterns = [
    path('', add_sandwich, name='sandwich-add'),
    path('show', SandwichListView.as_view(), name='all-sandwiches'),
    path('show/<int:pk>', SandwichDetailView.as_view(), name='sandwich'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('ingredients', IngredientsListView.as_view(), name='ingredient_list'),
]

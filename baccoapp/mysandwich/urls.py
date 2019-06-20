from django.urls import path
from .views import SandwichListView
from .views import SandwichDetailView
from .views import add_sandwich
from .views import SearchResultsView

# from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', create_sandwich, name='create-sandwich'),
    path('', add_sandwich, name='sandwich-add'),
    path('show', SandwichListView.as_view(), name='all-sandwiches'),
    path('show/<int:pk>', SandwichDetailView.as_view(), name='sandwich'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]

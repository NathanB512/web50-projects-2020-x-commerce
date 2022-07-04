from django.urls import path
from . import views

urlpatterns = [
    #Path to create listing
    path("create/", views.createListing, name="create")
    #Path displaying listings
    #Path to display individual listing 
    #path("<str:product>", views.product, name="product")
    #Path to display categories
    #Path to display products for each particular category

]
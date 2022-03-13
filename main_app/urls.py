from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    
    path('grocerieslist/', views.GroceriesList.as_view(), name="grocerieslist"),
    
    path('groceries/', views.Groceries.as_view(), name="groceries"),
    
    path('groceries/new/', views.GroceriesCreate.as_view(), name="groceries_create"),
    
    path('groceries/<int:pk>/', views.GroceriesDetail.as_view(), name="groceries_detail"),
    path('groceries/<int:pk>/update',views.GroceriesUpdate.as_view(), name="groceries_update"),
    path('groceries/<int:pk>/delete',views.GroceriesDelete.as_view(), name="groceries_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('grocerylist/<int:grocery_pk>/add', views.AddGrocery.as_view(), name="add_grocery"),
    path('grocerylist/<int:grocerylist_pk>/remove', views.RemoveGrocery.as_view(), name="remove_grocery"),
]
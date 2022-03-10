from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    
    path('grocerieslist/<int:pk>/groceries/<int:grocery_pk>', views.GroceriesListAssoc.as_view(), name="groceries_list_assoc"),
    
    path('groceries/', views.Groceries.as_view(), name="groceries"),
    
    path('groceries/new/', views.GroceriesCreate.as_view(), name="groceries_create"),
    
    path('groceries/<int:pk>/', views.GroceriesDetail.as_view(), name="groceries_detail"),
    path('groceries/<int:pk>/update',views.GroceriesUpdate.as_view(), name="groceries_update"),
    path('groceries/<int:pk>/delete',views.GroceriesDelete.as_view(), name="groceries_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),

    # path('grocerylist', views..as_view(), name="grocery_list")
]
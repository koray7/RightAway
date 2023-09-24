from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Grocery, GroceryList
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class CheckOut(TemplateView):
    template_name = "check_out.html"

class Home(TemplateView):
    template_name = "home.html"


@method_decorator(login_required, name='dispatch')
class GroceriesList(TemplateView):
    template_name = "groceries_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["grocerylists"] = GroceryList.objects.filter(user=self.request.user)
        return context

class AddGrocery(View):
    def get(self, request, grocery_pk):
        current_grocery = Grocery.objects.get(pk=grocery_pk)
        grocery_list = GroceryList.objects.create(user=self.request.user, name=current_grocery.name, image=current_grocery.image, groceries=current_grocery)
        return redirect("groceries")

class RemoveGrocery(View):
    def get(self, request, grocerylist_pk):
        grocery_list = GroceryList.objects.get(pk=grocerylist_pk)
        grocery_list.delete()
        return redirect("groceries")




# class Groceries:
#     def __init__(self, name, image, category):
#         self.name = name
#         self.image = image
#         self.category = category
# groceries = [
#     Groceries("Carrot", "https://www.economist.com/img/b/1280/720/90/sites/default/files/20180929_BLP506.jpg", "Vegetable"),
#     Groceries("Apple", "https://www.goodfruit.com/wp-content/uploads/Snapdragon-single.jpg", "Fruit"),
#     Groceries("Milk", "https://images.immediate.co.uk/production/volatile/sites/30/2020/02/Glass-and-bottle-of-milk-fe0997a.jpg?quality=90&resize=960,872", "Dairy"),
# ]

class Groceries(TemplateView):
    template_name = "groceries.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get("category")

        if category != None:
            context["groceries"] = Grocery.objects.filter(category__icontains=category)
        else:
            context["groceries"] = Grocery.objects.all()
        return context


class GroceriesCreate(CreateView):
    model = Grocery
    fields = ['name', 'image', 'category', 'organic']
    template_name ="groceries_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GroceriesCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('groceries_detail', kwargs={'pk': self.object.pk})

class GroceriesDetail(DetailView):
    model = Grocery
    template_name = "groceries_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_groceries = Grocery.objects.all()
        all_groceries_list = GroceryList.objects.filter(user=self.request.user).values_list("name", flat=True)
        available=all_groceries.exclude(name__in=all_groceries_list)
        context['available'] = available
        return context

class GroceriesUpdate(UpdateView):
    model = Grocery
    fields = ['name', 'image', 'category', 'organic']
    template_name ="groceries_update.html"
    def get_success_url(self):
        return reverse('groceries_detail', kwargs={'pk': self.object.pk})

class GroceriesDelete(DeleteView):
    model = Grocery
    template_name = "groceries_delete_confirmation.html"
    success_url = "/groceries/"



class Signup(View):
    
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
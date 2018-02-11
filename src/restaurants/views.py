from django.db.models import Q
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import RestaurantLocation

# Create your views here.
# function based view
# def home(request):
#     html_var = 'nestle strings'
#     html_ = f"""<!DOCTYPE html>
#     <head>
#     </head>
#     <body>
#     <h1>Hello World!</h1>
#     <p>This is {html_var} coming through!</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)

def home(request):
    num = None
    some_list = [
        randint(1, 1000000), 
        randint(1, 1000000), 
        randint(1, 1000000)
        ]
    cond_bool_item = False
    if cond_bool_item:
        num = randint(1,20000000)
    context =  {
        "num": num,
        "some_list": some_list
    }
    return render(request, "home.html", context)

def about(request):
    context =  {}
    return render(request, "about.html", context)

def contact(request):
    context =  {}
    return render(request, "contact.html", context)


class ContactView(TemplateView):
    template_name = 'contact.html'


class HomeView(TemplateView):
    template_name = 'home.html'
    #Overriding method
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        #print(context)
        num = None
        some_list = [
            randint(1, 1000000), 
            randint(1, 1000000), 
            randint(1, 1000000)
            ]
        cond_bool_item = True
        if cond_bool_item:
            num = randint(1,20000000)
        context =  {
            "num": num,
            "some_list": some_list
        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

def restaurant_listview(request):
    template_name = 'restaurants/restaurant_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    #queryset = RestaurantLocation.objects.all()
    template_name = 'restaurants/restaurant_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
                )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class JapaneseListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='japanese')
    template_name = 'restaurants/restaurant_list.html'

class AsianFusionListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='asian fusion')
    template_name = 'restaurants/restaurant_list.html'
    
class SearchRestaurantListView(ListView):
    template_name = 'restaurants/restaurant_list.html'

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
                )
        else:
            queryset = RestaurantLocation.objects.none()
        return queryset
    










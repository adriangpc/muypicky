from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

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
    










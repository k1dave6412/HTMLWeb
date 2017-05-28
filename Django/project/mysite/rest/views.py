from .models import Restaurant,Menu
from django.template import loader
from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):
    restaurant_list = Restaurant.objects.order_by('-restaurant_name')[:5]
    context = {'restaurant_list': restaurant_list}
    return render(request, 'rest/index.html', context)


#def detail(request, restaurant_id):
#    try:
#        restaurant = Restaurant.objects.get(pk=restaurant_id)
#    except Restaurant.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'rest/detail.html', {'restaurant': restaurant})

#def results(request, restaurant_id):
#    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
#    return render(request, 'rest/results.html', {'restaurant': restaurant})

def vote(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    restaurant_list = Restaurant.objects.order_by('-restaurant_name')[:5]
   
    try:
        selected_choice = restaurant.menu_set.get(pk=request.POST['menu'])
    except (KeyError, Menu.DoesNotExist):
        return render(request, 'rest/index.html', {
            'restaurant_list': restaurant_list,
            'error_message': "You didn't select a meal.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return render(request, 'rest/index.html', {'restaurant_list': restaurant_list,
        })
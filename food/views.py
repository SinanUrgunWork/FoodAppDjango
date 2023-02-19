from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)
    # return HttpResponse(template.render(context, request))
    # template = loader.get_template('food/index.html')


def items(request):
    return HttpResponse('<h1>items</h1>')


def detail(request, item_id):
    item_detail = Item.objects.get(pk=item_id)
    context = {
        'item': item_detail,
    }
    return render(request, 'food/detail.html', context)

# --*-- encoding utf-8
from django.shortcuts import render
from .models import Category, Page


def index(request):
    category_list = Category.objects.order_by('likes')[0:5]
    context_list = {'categories': category_list, }
    return render(request, 'rango/index.html', context_list)


def category(request, category_name_slug):
    context_list = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_list['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_list['pages'] = pages
        context_list['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_list)


def about(request):
    return render(request, 'rango/about.html')

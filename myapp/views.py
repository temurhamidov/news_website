from django.shortcuts import render, HttpResponse, get_list_or_404
from .models import News, Category, Region
from taggit.models import Tag
# Create your views here.

def home(request):
    text = request.GET.get("search")
    if text:
        news = News.objects.filter(title__icontains=text).order_by('-created')
    else:
        news = News.objects.all().order_by('-created')

    category_list = Category.objects.all()
    region_list = Region.objects.all()
    context = {
        'news' : news,
        'category_list' : category_list,
        'region_list' : region_list
    }
    return render(request, 'home.html', context)

def news_detail(request, news_id):
    news = get_list_or_404(News, pk=news_id)
    category_list = Category.objects.all()
    region_list = Region.objects.all()
    last_news = News.objects.all().order_by('-created')[:3]
    context = {
        'news': news,
        'last_news': last_news,
        'category_list': category_list,
        'region_list': region_list
    }
    return render(request, 'detail.html', context)


def news_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    news = News.objects.filter(category=category).order_by('-created')
    category_list = Category.objects.all()
    region_list = Region.objects.all()
    context = {
        'category' : category,
        'news': news,
        'category_list': category_list,
        'region_list': region_list,

    }
    return render(request, 'news_category.html', context)


def news_region(request, region_id):
    region = Region.objects.get(pk=region_id)
    news = News.objects.filter(region=region).order_by('-created')
    category_list = Category.objects.all()
    region_list = Region.objects.all()
    context = {
        'category': region,
        'news': news,
        'category_list': category_list,
        'region_list': region_list,
    }

    return render(request, 'news_region.html', context)

def news_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    news = News.objects.filter(tags=tag).order_by('-created')
    category_list = Category.objects.all()
    region_list = Region.objects.all()

    context = {
        'news': news,
        'category_list': category_list,
        'region_list': region_list,
    }

    return render(request, 'home.html', context)


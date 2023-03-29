from django.urls import path
from .views import home, news_detail, news_category, news_region, news_tag

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:news_id>', news_detail, name='news_detail'),
    path('category/<int:category_id>', news_category, name='news_category'),
    path('region/<int:region_id>', news_region, name='news_region'),
    path('tag/<slug:slug>', news_tag, name='news_tag'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('top-stories/', views.top_stories_view, name='Top Stories'),
    path('local-news/', views.local_news_view, name='Local News'),
    path('', views.home, name='Express_Update')
]
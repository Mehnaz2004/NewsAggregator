from django.urls import path
from . import views

urlpatterns = [
    path('top-stories/', views.top_stories_view, name='top_stories'),
    path('for-you/', views.for_you_view, name='for_you'),
    path('', views.home, name='Express_Update')
]
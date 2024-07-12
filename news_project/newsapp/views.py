
from django.shortcuts import render
import requests
from .scrapper import article_scrapper

def top_stories_view(request):
    base_url = "https://news.google.com/"
    url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"            # Assuming url is passed in query parameters

    # Scrape articles for Top Stories
    articles_data = article_scrapper(url, base_url)

    if articles_data:
        top_stories = articles_data  # This can be filtered or sliced as needed
    else:
        top_stories = []

    return render(request, 'newsapp/topstories.html', {
        'top_stories': top_stories,
    })

def for_you_view(request):
    base_url = "https://news.google.com/"
    url = "https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREUyYlhBNWVnc0tDUzl0THpBeE5tMXdPU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREUyYlhBNUtBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"

    # Scrape articles for For You section
    articles_data = article_scrapper(url, base_url)

    if articles_data:
        for_you = articles_data  # This can be filtered or sliced as needed
    else:
        for_you = []

    return render(request, 'newsapp/foryou.html', {'for_you': for_you,})
    

def home(request):
    return render(request, 'newsapp\home.html')
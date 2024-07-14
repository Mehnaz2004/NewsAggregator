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

def local_news_view(request):
    base_url = "https://news.google.com/"
    url = "https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREUyYlhBNWVnc0tDUzl0THpBeE5tMXdPU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREUyYlhBNUtBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"

    # Scrape articles for For You section
    articles_data = article_scrapper(url, base_url)

    if articles_data:
        local_news = articles_data  # This can be filtered or sliced as needed
    else:
        local_news = []

    return render(request, 'newsapp/localnews.html', {'local_news': local_news,})
    

def home(request):
    topurl = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen" 
    localurl = "https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREUyYlhBNWVnc0tDUzl0THpBeE5tMXdPU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREUyYlhBNUtBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
    base_url = "https://news.google.com/"
    
    top_articles = article_scrapper(topurl, base_url)
    local_articles = article_scrapper(localurl, base_url)
    
    if top_articles and local_articles:
        top5_articles = top_articles[:5]
        local5_articles = local_articles[:5]
    else:
        top5_articles = []
        local5_articles = []
    context = {
        'top5_articles': top5_articles,
        'local5_articles': local5_articles
    }
    return render(request, 'newsapp/home.html', context)
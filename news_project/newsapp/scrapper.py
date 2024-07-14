import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime
import humanize

def article_scrapper(url, base_url):
    articles_data = []
    page_data = requests.get(url)
    if page_data.status_code == 200:
        soup= BeautifulSoup(page_data.text, 'html.parser')
        content = soup.find_all(name='article')
        
        for article in content:
            HeadLine_tag = article.find("a", class_="gPFEn")
            if not HeadLine_tag:
                continue  # Skip this article if headline tag is not found
            HeadLine = HeadLine_tag.text
            relative_link = HeadLine_tag.get("href")
            link = urljoin(base_url, relative_link)

            # Find author and handle if not found
            author_tag = article.find("span", class_="PJK1m")
            if author_tag:
                author = author_tag.text
            else:
                author = "Anonymous"
                
            #find time of each article's posting and converting it into mysql datetime format
            time=article.find("time", class_="hvbAAd")['datetime']
            mysql_datetime=datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
            article_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
            time_ago = humanize.naturaltime(datetime.now() - article_datetime)
            article_data= {
                'Headline': HeadLine,
                'Link': link,
                'Author': author,
                'Timestamp': time_ago
            }
            articles_data.append(article_data)
        return articles_data
    else:
        print(f"Failed to retrieve the webpage. Status code: {page_data.status_code}")
        return None
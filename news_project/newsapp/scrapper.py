import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

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
            
            # Find image source and handle if not found
            img_tag = article.find("img", class_="Quavad vwBmvb")
            if img_tag and img_tag.has_attr('src'):
                img_rel=img_tag['src']
                img_src = urljoin(base_url, img_rel)
            else:
                img_src = None
                
            #find time of each article's posting and converting it into mysql datetime format
            
            time=article.find("time", class_="hvbAAd")['datetime']
            mysql_datetime=datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
            article_data= {
                'Headline': HeadLine,
                'Link': link,
                'Author': author,
                'ImageSource': img_src,
                'Timestamp': mysql_datetime
                
            }
            articles_data.append(article_data)
        return articles_data
    else:
        print(f"Failed to retrieve the webpage. Status code: {page_data.status_code}")
        return None
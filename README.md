# News Aggregator

## Overview
The News Aggregator project is a web application built using Django, designed to aggregate and display news articles fetched from various websites using web scraping techniques. It incorporates JavaScript for dynamic user interactions such as theme toggling and event handling.

## Features
- **Top News Section:** Displays top news articles scraped from multiple sources.
  
- **Personalized News:** Users can view articles based on different categories.
  
- **Dark/Light Mode:** Toggle between dark and light themes for better readability, implemented using JavaScript event listeners and CSS manipulation.
  
- **Search Functionality:** Allows users to search for specific news topics.
  
- **Web Scraping:** Utilizes Beautiful Soup for fetching and parsing news articles.
  
- **Human Readable Timestamps:** Converts timestamps into a human-readable format using the humanize library.

## Technologies Used
- **Django**: Powerful web framework for backend development and rendering HTML templates. JavaScript used for dynamic client-side interactions.
  
- **HTML/CSS/JavaScript**: Frontend development and interactivity. JavaScript is used for theme toggling, event handling, and dynamic content updates.
  
- **Beautiful Soup**: Python library for web scraping, used to retrieve and parse news articles from various websites.
- **Humanize**: Python library for converting timestamps into human-readable format for enhanced user experience.
  
- **Git**: Version control system for tracking changes in the project codebase.
  
- **GitHub**: Platform for hosting the project repository and collaboration.


## Getting Started
To run this project locally, follow these steps:
1. Clone this repository.
   ```bash
   git clone https://github.com/Mehnaz2004/NewsAggregator.git
  
2. Navigate to the project directory.
   ```bash
   cd NewsAggregator
   
3. Install dependencies.
   ```bash
   pip install -r requirements.txt
   
5. Perform database migrations.
   ```bash
   python manage.py makemigrations
	 python manage.py migrate
   
7. Start the development server
   ```bash
   python manage.py runserver

10. Open the web browser and go to [http://localhost:8000] to view the application

## Acknowledgments
inspiration and references:
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Humanize Documentation](https://django-humanize.readthedocs.io/en/stable/)
- [JavaScript MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Stack Overflow Community](https://stackoverflow.com/)

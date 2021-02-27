import src.parsers as prs
import src.web as web

def scrape_shoes_from_url(url):
    page_data = web.get_web_page_json(url)
    
    if not page_data:
        return None

    shoes = prs.parse_shoes_from_page_data(page_data)
    return shoes
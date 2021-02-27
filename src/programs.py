import src.parsers as prs
import src.web as web

def get_shoes_from_url(url):
    page_json = web.get_web_page_json(url)
    
    if not page_json:
        return None

    shoes = prs.parse_shoes_data(page_json)
    return shoes
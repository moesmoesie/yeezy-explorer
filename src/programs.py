import src.parsers as prs
import src.web as web

def scrape_shoes_from_url(url):
    shoes = []
    while True:
        page_data = web.get_web_page_json(url)
        
        if not page_data:
            return None

        pagination = prs.parse_pagination_from_page_data(page_data)
        new_shoes = prs.parse_shoes_from_page_data(page_data)
        shoes.extend(new_shoes)
        url = pagination.get_next_page_url()

        if not url:
            break

    return shoes
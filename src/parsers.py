from src.models import Shoe
from src.models import Pagination

def parse_shoe_from_shoe_data(shoe_data):
    return Shoe(
        identifier = shoe_data["id"],
        release_time = shoe_data["releaseTime"],
        name = shoe_data["title"],
        catagory = shoe_data["shoe"],
        sub_catagory = shoe_data["name"],
        colors = shoe_data["colorway"]
    )

def parse_shoes_from_page_data(page_data):
    shoes_data = page_data["Products"]
    return [parse_shoe_from_shoe_data(shoe_data) for shoe_data in shoes_data]

def parse_pagination_from_page_data(page_data):
    pagination_data = page_data["Pagination"]
    next_page = pagination_data["nextPage"]
    if next_page and "/v3/" in next_page:
        next_page = next_page.replace("/v3/","/")

    return Pagination(
        next_page = next_page
    )
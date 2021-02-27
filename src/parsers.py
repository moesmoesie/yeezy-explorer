from src.models import Shoe
from src.models import Pagnation

def parse_shoes_data(json_data):
    products = json_data["Products"]
    return [Shoe(shoe_data) for shoe_data in products]

def parse_pagnation_data(json_data):
    pagnation_data = json_data["Pagination"]
    return Pagnation(pagnation_data)
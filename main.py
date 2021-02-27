import src.web as web
from src.models import Tag

if __name__ == "__main__":
    base = "https://stockx.com/api/browse?_tags=yeezy,adidas&productCategory=sneakers"
    base_tags = [
        Tag("gender",["men"]),
        Tag("year",["2015","2016","2017","2018","2019","2020","2021"]),
    ]
    url = web.create_url(base,tags)
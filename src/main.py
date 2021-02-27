import requests

class Shoe():
    def __init__(self,data):
        self.identifier = data["id"]
        self.release_time = data["releaseTime"]
        self.name = data["title"]
        self.type = data["shoe"]
        self.sub_type = data["name"]
        self.colors = data["colorway"]

    def to_dict(self):
        return {
            "id" : self.identifier,
            "releaseTime": self.release_time,
            "name": self.name,
            "type": self.type,
            "subType": self.subType,
            "colors" : self.colors
        }

    def __str__(self):
        return f"{self.identifier}: {self.name}, {self.colors}"

def get_web_page_json(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def parse_shoes_data(json_data):
    products = json_data["Products"]
    return [Shoe(shoe_data) for shoe_data in products]

if __name__ == '__main__':

    shoes = []
    url = "https://stockx.com/api/browse?_tags=yeezy,adidas&productCategory=sneakers"
    page_json = get_web_page_json(url)
    if page_json:
        shoes.extend(parse_shoes_data(page_json))
    else:
        print("Error")

    for shoe in shoes:
        print(shoe)
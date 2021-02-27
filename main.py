import src.programs as programs

if __name__ == "__main__":
    url = "https://stockx.com/api/browse?_tags=yeezy%2Cadidas&productCategory=sneakers"
    shoes = programs.get_shoes_from_url(url)
    print(len(shoes))
    
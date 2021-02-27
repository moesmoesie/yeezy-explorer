class Pagnation():
    def __init__(self,data):
        next_page = data["nextPage"]
        if next_page and "/v3/" in next_page:
            next_page = next_page.replace("/v3/","/")
        self.next_page = next_page

    def get_next_page_url(self):
        if self.next_page:
            return "".join(["https://stockx.com", self.next_page])
        else:
            return None 

    def to_dict(self):
        pass
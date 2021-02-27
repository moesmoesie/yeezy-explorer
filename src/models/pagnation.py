class Pagnation():
    def __init__(self,next_page):
        self.next_page = next_page

    def get_next_page_url(self):
        if self.next_page:
            return "".join(["https://stockx.com", self.next_page])
        else:
            return None 

    def to_dict(self):
        return {
            self.next_page
        }
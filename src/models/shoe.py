class Shoe():
    def __init__(self,identifier,release_time,name,catagory,sub_catagory,colors):
        self.identifier = identifier
        self.release_time = release_time
        self.name = name
        self.catagory = catagory
        self.sub_catagory = sub_catagory
        self.colors = colors

    def to_dict(self):
        return {
            "id" : self.identifier,
            "releaseTime": self.release_time,
            "name": self.name,
            "type": self.catagory,
            "subType": self.sub_catagory,
            "colors" : self.colors
        }

    def __str__(self):
        return f"{self.identifier}: {self.name}, {self.colors}"
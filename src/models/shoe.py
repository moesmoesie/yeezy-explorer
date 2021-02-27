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
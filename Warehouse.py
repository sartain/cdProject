class Warehouse:
    def __init__(self):
        self.cd_list = [("c", "d")]

    def findCD(self, artist, title):
        return self.cd_list.__contains__((artist, title))
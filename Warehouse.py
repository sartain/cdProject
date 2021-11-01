class Warehouse:
    def __init__(self, cd_list):
        self.cd_list = cd_list

    def findCD(self, artist, title):
        return self.cd_list.__contains__((artist, title))
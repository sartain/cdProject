class Warehouse:
    def __init__(self, cd_list):
        self.cd_list = cd_list

    def findCD(self, artist, title):
        for cd in self.cd_list:
            if cd["artist"] == artist and cd["title"] == title:
                if cd["stock"] > 0:   #cd in stock
                    cd["stock"] -= 1
                    return True
                return False
        return False

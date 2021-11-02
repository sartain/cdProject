class Warehouse:
    def __init__(self, cd_list):
        self.cd_list = cd_list

    def findCD(self, artist, title):
        for cd in self.cd_list:
            cd_artist = cd[0]
            cd_title = cd[1]
            cd_stock = cd[2]
            if cd_artist == artist and cd_title == title:
                if cd_stock > 0:   #cd in stock
                    cd[2] -= 1
                    return True
                return False
        return False

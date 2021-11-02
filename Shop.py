class Shop:
    def __init__(self, warehouse):
        self.warehouse = warehouse

    def buy_cd(self, artist, title, credit_card):
        if self.warehouse.findCD(artist, title):
            return credit_card.payment_accepted
        return False
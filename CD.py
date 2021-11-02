class CD:
    def __init__(self, artist, title, stock):
        self.artist = artist
        self.title = title
        self.stock = stock

    def buy_cd(self, credit_card):
        if credit_card.payment_accepted:
            if self.stock > 0:
                self.stock -= 1
                return True
            return False #not in stock
        return False #payment not accepted
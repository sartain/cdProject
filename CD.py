class CD:
    def __init__(self, artist, title, stock, price):
        self.artist = artist
        self.title = title
        self.stock = stock
        self.price = price

    def buy_cd(self, credit_card, quantity, charts, competitorPrice):
        chart_position = charts.current_chart_position(self.artist, self.title)
        competitor_price = competitorPrice.get_price()
        price_to_pay = self.price
        if charts.in_top_100():
            price_to_pay = competitor_price - 1.00
        if credit_card.can_afford(price_to_pay):
            if self.stock - quantity >= 0:
                self.stock -= quantity
                charts.sale_update(self.artist, self.title, quantity)
                return True
            return False #not in stock
        return False #payment not accepted
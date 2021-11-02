class CreditCardProvider:
    def __init__(self, payment_accepted):
        self.payment_accepted = payment_accepted

    def can_afford(self, price):
        return self.payment_accepted
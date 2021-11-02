import unittest

from Warehouse import Warehouse


class CD:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title


class Shop:
    def __init__(self, warehouse):
        self.warehouse = warehouse

    def buy_cd(self, artist, title, credit_card):
        if self.warehouse.findCD(artist, title):
            return credit_card.payment_accepted
        return False


class CreditCardProvider:
    def __init__(self, payment_accepted):
        self.payment_accepted = payment_accepted


class CDTest(unittest.TestCase):

    def test_buy_cd_when_payment_accepted_and_in_stock(self):
        warehouse = Warehouse([["artist_c", "title_d", 1]])
        shop = Shop(warehouse)
        credit_card = CreditCardProvider(True)
        self.assertEqual(True, shop.buy_cd("artist_c", "title_d", credit_card))

    def test_buy_cd_when_payment_not_accepted_and_in_stock(self):
        warehouse = Warehouse([["artist_c", "title_d", 1]])
        shop = Shop(warehouse)
        credit_card = CreditCardProvider(False)
        self.assertEqual(False, shop.buy_cd("artist_c", "title_d", credit_card))

    def test_buy_cd_when_not_in_stock_payment_accepted(self):
        warehouse = Warehouse([])
        shop = Shop(warehouse)
        credit_card = CreditCardProvider(True)
        self.assertEqual(False, shop.buy_cd("artist_c", "title_d", credit_card))

    def test_buy_one_cd_remove_one_cd_stock_from_warehouse_out_of_stock(self):
        warehouse = Warehouse([["artist_c", "title_d", 1]])
        shop = Shop(warehouse)
        credit_card = CreditCardProvider(True)
        shop.buy_cd("artist_c", "title_d", credit_card) #Buy cd to reduce stock level
        #cd out of stock cannot buy again
        self.assertEqual(False, shop.buy_cd("artist_c", "title_d", credit_card))
        #We buy a cd, then the stock is reduced by one
        #We want to check

    # def test_get_cd_from_artist_and_title_when_not_exist(self):
    #    warehouse = Warehouse()
    #    self.assertEqual(False, warehouse.findCD("artist_a", "title_b"))

    # def test_get_cd_when_exist(self):
    #    warehouse = Warehouse()
    #    self.assertEqual(True, warehouse.findCD("artist_c", "title_d"))

    # def test_get_cd_object_when_exist(self):
    #    warehouse = Warehouse()
    #    self.assertEqual(CD("artist_e", "title_f"), warehouse.findCD("artist_e", "title_f"))


if __name__ == '__main__':
    unittest.main()

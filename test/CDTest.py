import unittest

from CD import CD
from CreditCardProvider import CreditCardProvider
from Shop import Shop
from Warehouse import Warehouse


class CDTest(unittest.TestCase):

    def test_buy_cd_when_payment_accepted_and_in_stock(self):
        cd = CD("artist_c", "title_d", 1)
        credit_card = CreditCardProvider(True)
        self.assertEqual(True, cd.buy_cd(credit_card))

    def test_buy_cd_when_payment_not_accepted_and_in_stock(self):
        cd = CD("artist_c", "title_d", 1)
        credit_card = CreditCardProvider(False)
        self.assertEqual(False, cd.buy_cd(credit_card))

    def test_buy_cd_when_not_in_stock_payment_accepted(self):
        cd = CD("artist_c", "title_d", 0)
        credit_card = CreditCardProvider(True)
        self.assertEqual(False, cd.buy_cd(credit_card))

    def test_buy_one_cd_remove_one_cd_stock_from_warehouse_out_of_stock(self):
        cd = CD("artist_c", "title_d", 1)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card) #Buy cd to reduce stock level
        #cd out of stock cannot buy again
        self.assertEqual(False, cd.buy_cd(credit_card))

    def test_buy_two_cd_in_a_row_in_stock_payment_accepted(self):
        cd = CD("artist_c", "title_d", 2)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card) #Buy cd to reduce stock level
        #cd out of stock cannot buy again
        self.assertEqual(True, cd.buy_cd(credit_card))


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

import unittest
from unittest.mock import MagicMock

from CD import CD
from Charts import Charts
from CreditCardProvider import CreditCardProvider


class CDTest(unittest.TestCase):
    """
    def test_buy_cd_when_payment_accepted_and_in_stock(self):
        cd = CD("artist_c", "title_d", 1, 9.99)
        credit_card = CreditCardProvider(True)
        self.assertEqual(True, cd.buy_cd(credit_card, 1))

    def test_buy_cd_when_payment_not_accepted_and_in_stock(self):
        cd = CD("artist_c", "title_d", 1, 9.99)
        credit_card = CreditCardProvider(False)
        self.assertEqual(False, cd.buy_cd(credit_card, 1))

    def test_buy_cd_when_not_in_stock_payment_accepted(self):
        cd = CD("artist_c", "title_d", 0, 9.99)
        credit_card = CreditCardProvider(True)
        self.assertEqual(False, cd.buy_cd(credit_card, 1))

    def test_buy_one_cd_remove_one_cd_stock_from_warehouse_out_of_stock(self):
        cd = CD("artist_c", "title_d", 1, 9.99)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card, 1) #Buy cd to reduce stock level
        #cd out of stock cannot buy again
        self.assertEqual(False, cd.buy_cd(credit_card, 1))

    def test_buy_two_cd_in_a_row_in_stock_payment_accepted(self):
        cd = CD("artist_c", "title_d", 2, 9.99)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card, 1) #Buy cd to reduce stock level
        self.assertEqual(True, cd.buy_cd(credit_card, 1))
"""
    def test_charts_alerted_when_sale_made(self):
        charts = Charts(10)
        charts.sale_update = MagicMock()
        cd = CD("artist_a", "title_b", 5, 9.99)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card, 3, charts)
        charts.sale_update.assert_called_once_with("artist_a", "title_b", 3)

    def test_cd_buy_function_receives_current_chart_position(self):
        charts = Charts(10)
        charts.current_chart_position = MagicMock()
        cd = CD("artist_a", "title_b", 5, 9.99)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card, 3, charts)
        charts.current_chart_position.assert_called_once_with("artist_a", "title_b")

if __name__ == '__main__':
    unittest.main()

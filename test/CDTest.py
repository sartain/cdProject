import unittest
from unittest.mock import MagicMock

from CD import CD
from Charts import Charts
from Competitor import Competitor
from CreditCardProvider import CreditCardProvider


class CDTest(unittest.TestCase):

    def test_buy_cd_when_payment_accepted_and_in_stock(self):
        charts = Charts(10)
        cd = CD("artist_c", "title_d", 1, 9.99)
        credit_card = CreditCardProvider(True)
        self.assertEqual(True, cd.buy_cd(credit_card, 1, charts, Competitor(8.99)))

    def test_buy_cd_when_payment_not_accepted_and_in_stock(self):
        charts = Charts(10)
        cd = CD("artist_c", "title_d", 1, 9.99)
        credit_card = CreditCardProvider(False)
        self.assertEqual(False, cd.buy_cd(credit_card, 1, charts, Competitor(8.99)))

    def test_buy_cd_when_not_in_stock_payment_accepted(self):
        charts = Charts(10)
        cd = CD("artist_c", "title_d", 0, 9.99)
        credit_card = CreditCardProvider(True)
        self.assertEqual(False, cd.buy_cd(credit_card, 1, charts, Competitor(8.99)))

    def test_buy_one_cd_remove_one_cd_stock_from_warehouse_out_of_stock(self):
        charts = Charts(10)
        cd = CD("artist_c", "title_d", 1, 9.99)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card, 1, charts, Competitor(8.99)) #Buy cd to reduce stock level
        #cd out of stock cannot buy again
        self.assertEqual(False, cd.buy_cd(credit_card, 1, charts, Competitor(8.99)))

    def test_buy_two_cd_in_a_row_in_stock_payment_accepted(self):
        charts = Charts(10)
        cd = CD("artist_c", "title_d", 2, 9.99)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card, 1, charts, Competitor(8.99)) #Buy cd to reduce stock level
        self.assertEqual(True, cd.buy_cd(credit_card, 1, charts, Competitor(8.99)))

    def test_charts_alerted_when_sale_made(self):
        charts = Charts(10)
        charts.sale_update = MagicMock()
        cd = CD("artist_a", "title_b", 5, 9.99)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card, 3, charts, Competitor(8.99))
        charts.sale_update.assert_called_once_with("artist_a", "title_b", 3)

    def test_cd_buy_function_receives_current_chart_position(self):
        charts = Charts(10)
        charts.in_top_100 = MagicMock()
        cd = CD("artist_a", "title_b", 5, 9.99)
        credit_card = CreditCardProvider(True)
        cd.buy_cd(credit_card, 3, charts, Competitor(8.99))
        charts.in_top_100.assert_called_once

    def test_when_in_top100_cd_buy_gets_lowest_competitor_price_from_charts(self):
        charts = Charts(10)
        competitor_price = Competitor(8.99)
        competitor_price.get_price = MagicMock()
        cd = CD("artist_a", "title_b", 5, 9.99)
        cd.buy_cd(CreditCardProvider(True), 3, charts, competitor_price)
        competitor_price.get_price.assert_called_once()

    def test_when_buying_cd_out_of_top_100_price_passed_to_card_provider(self):
        charts = Charts(10000)
        competitor_price = Competitor(8.99)
        credit_card_provider = CreditCardProvider(True)
        credit_card_provider.can_afford = MagicMock()
        cd = CD("artist_a", "title_b", 5, 9.99)
        cd.buy_cd(credit_card_provider, 3, charts, competitor_price)
        credit_card_provider.can_afford.assert_called_with(9.99)

    def test_when_buying_cd_in_top_100_reduce_price_by_one_pound(self):
        charts = Charts(10)
        competitor_price = Competitor(8.99)
        credit_card_provider = CreditCardProvider(True)
        credit_card_provider.can_afford = MagicMock()
        cd = CD("artist_a", "title_b", 5, 9.99)
        cd.buy_cd(credit_card_provider, 3, charts, competitor_price)
        credit_card_provider.can_afford.assert_called_with(7.99)

if __name__ == '__main__':
    unittest.main()

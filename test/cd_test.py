import unittest

from Warehouse import Warehouse


class cd_test(unittest.TestCase):

    def test_get_cd_from_artist_and_title_when_not_exist(self):
        warehouse = Warehouse()
        self.assertEqual(False, warehouse.findCD("a", "b"))

    def test_get_cd_when_exist(self):
        warehouse = Warehouse()
        self.assertEqual(True, warehouse.findCD("c", "d"))

if __name__ == '__main__':
    unittest.main()

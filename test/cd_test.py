import unittest


class Warehouse:
    def __init__(self):
        pass

    def findCD(self, artist, title):
        return False

class cd_test(unittest.TestCase):

    def test_get_cd_from_artist_and_title_when_not_exist(self):
        warehouse = Warehouse()
        self.assertEqual(False, warehouse.findCD("a", "b"))

if __name__ == '__main__':
    unittest.main()

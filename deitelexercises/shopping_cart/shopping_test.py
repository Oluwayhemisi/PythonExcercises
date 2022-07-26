import unittest
import shopping


class ShoppingTest(unittest.TestCase):
    def test_that_you_basket_is_not_empty(self):
        item1 = shopping.Basket(0,0)
        self.assertIsNotNone(item1,shopping.Basket)

    def test_that_you_can_add(self):
        item1 = shopping.Basket(3, 500)
        item1.add("shoe", 100)
        self.assertEqual(1, item1.get_length())

        item1.add("bag", 200)
        self.assertEqual(2, item1.get_length())
        self.assertEqual([["shoe", 100], ["bag", 200]], item1.get_basket())


    def test_the_length_of_the_item(self):
        item1 = shopping.Basket(3, 500)
        item1.add("shoes",200)
        item1.add("bag",200)
        item1.add("perfume",100)
        item1.add("gold",200)
        self.assertEqual(3, item1.get_length())

    def test_that_the_amount_doesnt_exceed_fixed_price(self):
        item1 = shopping.Basket(3, 500)
        item1.add("rice", 100)
        item1.add("garri", 200)
        item1.add("sugar", 100)
        item1.add("hotdog", 100)
        self.assertEqual([["garri",200],["sugar",100],["hotdog",100]], item1.get_basket())
    def test_that_the_item_automatically_replaces_itself(self):
        item1 = shopping.Basket(3,1000)
        item1.add("gown",300)
        item1.add("shoes",500)
        item1.add("hair",200)
        item1.add("bag",300)
        self.assertEqual(3, item1.get_length())
        self.assertEqual([["shoes",500],["hair",200],["bag",300]], item1.get_basket())






if __name__ == '__main__':
    unittest.main()

import unittest
import play_ground



class PlaygroundTest(unittest.TestCase):
    def setUp(self) -> None:
        print("i am running")
    def tearDown(self) -> None:
        print("I am walking")

    def test_can_create_playground(self):
        basket1 = play_ground.Playground()
        self.assertIsNotNone(basket1)
        self.assertIsInstance(basket1,play_ground.Playground)



if __name__ == '__main__':
    unittest.main()

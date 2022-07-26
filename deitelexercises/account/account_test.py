import unittest
import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account("Tolani","1234")
        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """
        GIVEN:
        WHEN:
        THEN:

        """
        account1 = account.Account("Ernest")
        name = account1.name
        self.assertEqual("Ernest", name)

    # def test_that_account_has_password(self):
    #     account1 = account.Account("Ernest")
    #     password = account1.password
    #     self.assertEqual("1234", password)
    #
    # def test_that_account_has_phonenumber(self):
    #     account1 = account.Account("Ernest", "1234", "07062396366")
    #     phonenumber = account1.phonenumber
    #     self.assertEqual("07062396366", phonenumber)

    def test_that_you_can_deposit(self):
        """
        GIVEN:
        WHEN:
        THEN:

        :return:
        """
        account1 = account.Account("Tolani")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        account1 = account.Account("Stephen","1234")
        account1.deposit(500)
        self.assertRaises(ValueError, account1.deposit, -1000)
        # self.assertEqual(500, account1.balance)

    def test_that_you_can_withdraw(self):
        account1 = account.Account("Segun")
        account1.deposit(2000)
        self.assertRaises(ValueError, account1.withdraw, 5000)
        # self.assertEqual(2000,account1.balance)

    def test_that_you_can_do_transfer(self):
        account1 = account.Account("Ola")
        account2 = account.Account("Folake")

        account1.deposit(6000)
        account1.transfer(2000)
        account2.deposit(2000)
        self.assertEqual(4000, account1.balance)
        self.assertEqual(2000, account2.balance)

    def test_that_you_can_load_airtime(self):
        account1 = account.Account("Femi")
        account1.deposit(500)
        account1.withdraw(100)
        self.assertEqual(400, account1.balance)


if __name__ == '__main__':
    unittest.main()

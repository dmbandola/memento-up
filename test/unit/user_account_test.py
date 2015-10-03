import unittest
import json


class TestCreateUserAccount(unittest.TestCase):
    
    def test_if_new_user_account_is_added(self):

        user = UserAccount()

        self.assertEqual(json.loads(user.add_user_account('jennie','password')),'OK')

    def test_if_username_already_exists(self):

        user = UserAccount()

        username = 'jennie'

        self.assertEqual(json.loads(user.add_user_account(username)), 'jennie')






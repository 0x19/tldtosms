import unittest
import os
import time
from tldtosms import Connect
from telapi   import rest

# TODO
# TODO - TODO - TODO
class TestREST(unittest.TestCase):

    def setUp(self):

        # Environment variables must be set for TELAPI_ACCOUNT_SID, TELAPI_AUTH_TOKEN and TELAPI_TEST_FROM_NUMBER, TELAPI_TEST_TO_NUMBER
        self.test_from_number    = os.environ.get('TELAPI_TEST_FROM_NUMBER')
        self.test_to_number      = os.environ.get('TELAPI_TEST_TO_NUMBER')
        self.telapi_account_sid  = os.environ.get('TELAPI_ACCOUNT_SID')
        self.telapi_access_token = os.environ.get('TELAPI_AUTH_TOKEN')

        if not os.environ.get('TELAPI_ACCOUNT_SID'):
            raise Exception("Please set the TELAPI_ACCOUNT_SID, TELAPI_AUTH_TOKEN and TELAPI_TEST_FROM_NUMBER, TELAPI_TEST_TO_NUMBER environment variables to run the tests!")

    def verify_if_available(self):
    	pass

    def verify_sent_smss(self):
    	pass

if __name__ == '__main__':
    unittest.main()
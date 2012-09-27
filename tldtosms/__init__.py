import os

from tldtosms.utils import memoized, filter_e164, validate_e164
from tldtosms       import exceptions, sync, constants

from telapi         import rest

class Connect(object):

    def __init__(self, telapi_account_sid=None, telapi_auth_token=None, from_address=None, to_address=None, cache_file=None, *args, **kwargs):
        object.__init__(self)

        self.telapi_account_sid = telapi_account_sid or os.environ.get('TELAPI_ACCOUNT_SID')
        self.telapi_auth_token  = telapi_auth_token  or os.environ.get('TELAPI_AUTH_TOKEN')
        self.from_address       = from_address       or os.environ.get('TLDTOSMS_FROM_ADDRESS')
        self.to_address         = to_address         or os.environ.get('TLDTOSMS_TO_ADDRESS')
        self.sent_messages      = []
        self.cache_handler      = None
        self.cache_file         = cache_file

        if not self.telapi_account_sid or not self.telapi_account_sid.startswith("AC"):
            raise exceptions.AccountSidError()

        if not self.telapi_auth_token or len(self.telapi_auth_token) != 32:
            raise exceptions.AuthTokenError()

        if not validate_e164(self.from_address):
            raise exceptions.SourceAddressError()

        self.from_address = filter_e164(self.from_address)

        if not validate_e164(self.to_address):
            raise exceptions.DestinationAddressError()

        self.to_address  = filter_e164(self.to_address)

        try:
            self.cache_handler = open(self.cache_file, 'r+w')
        except Exception as e:
            raise exceptions.CacheHandlerError()

        if type(self.cache_handler) is not file:
            raise exceptions.CacheHandlerError()

        # Let's go now just instanciate updater class ...
        self.updater = sync.Updater( self.cache_handler, self.cache_file )

        self.telapi_client = rest.Client(self.telapi_account_sid, self.telapi_auth_token)


    def is_update_available(self):
        return self.updater.update_schema()


    def send_sms(self):
        
        account  = self.telapi_client.accounts[self.telapi_client.account_sid]

        for tld in self.updater.get_differences():
            
            sms_message = account.sms_messages.create(
                from_number = self.from_address,
                to_number   = self.to_address,
                body        = constants.SMS_NEW_TLD % (tld),
            )

            if sms_message:
                self.sent_messages.insert(len(self.sent_messages), sms_message)

    def get_sent_smss(self):
        return self.sent_messages


if __name__ == '__main__':
    tts_connect = Connect(
        telapi_account_sid = 'ACadea151d708d45febbbb5104c98977ca',
        telapi_auth_token  = '096353c24f3845678de1f5f5f5a7d694',
        from_address       = '(732) 733 6676',
        to_address         = '+385994512444',
        #to_address         = '+385915256970',
        cache_file         = os.path.join(os.path.dirname(__file__), 'data', 'tlds_current.dat')
    )

    # In case that update is available, loop throu and Send SMS messages
    if tts_connect.is_update_available():
        tts_connect.send_sms()

        for sms in tts_connect.get_sent_smss():
            print "SMS that is sent: %s" % sms.sid
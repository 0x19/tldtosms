class RestError(Exception):
    def __init__(self, message, error_code=None, http_code=None):
        Exception.__init__(self, message)
        self.message    = message
        self.error_code = error_code
        self.http_code  = http_code

class AccountSidError(RestError):
    message = "Please pass account_sid when instantiating the REST API Client or set the environment variable `TELAPI_ACCOUNT_SID`.\
        An account SID is a 34 character string that starts with the letters 'AC'."

class AuthTokenError(RestError):
    message = "Please pass auth_token when instantiating the REST API Client or set the environment variable `TELAPI_AUTH_TOKEN`.\
        An auth token is 32 characters long."

class SourceAddressError(RestError):
    message = "Please pass from_address when instantiating TldToSms or set the environment variable `TTS_FROM_ADDRESS`.\
        An from_address should be TelAPI number in E.164 format."


class DestinationAddressError(RestError):
    message = "Please pass to_address when instantiating TldToSms or set the environment variable `TTS_TO_ADDRESS`.\
        An from_address should be destination number in E.164 format that is capable to receive SMS messages.\
        Usually, your mobile phone number!"

class RequestError(RestError):
    pass
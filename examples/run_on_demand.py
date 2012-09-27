from tldtosms import Connect

# ALL parameters that are passed in Connect are REQUIRED
tts_connect = Connect(
    telapi_account_sid = 'account_sid',
    telapi_auth_token  = 'auth_token',
    from_address       = 'from_e164_number',
    to_address         = 'to_e164_number',
    cache_file         = '/full/path/to/tldtosms_cache.dat'
)

# In case that update is available, loop throu and Send SMS messages
if tts_connect.is_update_available():
    tts_connect.send_sms()

    for sms in tts_connect.get_sent_smss():
    	print "SMS that is sent: %s" % sms.sid
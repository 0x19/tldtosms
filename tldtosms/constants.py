''' This file is here to help out with ... '''
import os

### PACKAGE-WIDE CONSTANTS ###

PACKAGE_VERSION = '0.1.0.4'

### SYNCRONIZATION CONSTANTS ###

# Here the latest TLD list can be found. It's DAT file so we will need to 
SYNC_DATA_URL = 'http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1'

# Every 5 minutes is the minimum. You can't request update sooner
SYNC_MIN_UPDATE_INTERVAL = 300 

### TELAPI CONSTANTS ###

# When the new TLD is being applied to the sync data url above
SMS_NEW_TLD   = "New TLD '%s' is now available!"

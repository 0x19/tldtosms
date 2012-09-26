''' This file is here to help out with ... '''
import sys, os


### SYNCRONIZATION CONSTANTS ###

# Here the latest TLD list can be found. It's DAT file so we will need to 
SYNC_DATA_URL = 'http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1'

# Main data file where complete dat file will be stored out
SYNC_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'tlds_current.dat')

# Latest will be fetch here and than compared over difflib to see if there are any differences in files other than comments
# If there are, those will be consider as "new ones"
SYNC_DIFF_FILE = os.path.join(os.path.dirname(__file__), 'data', 'tlds_diff.dat')

# Every 5 minutes is the minimum. You can't request update sooner
SYNC_MIN_UPDATE_INTERVAL = 300 

### TELAPI CONSTANTS ###
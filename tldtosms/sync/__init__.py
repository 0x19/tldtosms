import sys, os, logging, time, datetime, urllib, tempfile
from tldtosms import exceptions, constants

class Updater(object):

    def __init__(self, cache_sync_handler=None, cache_sync_file=None):
        object.__init__(self)

        self.update_data_url        = constants.SYNC_DATA_URL
        self.tld_data_file          = cache_sync_handler
        self.tld_diff_file          = tempfile.NamedTemporaryFile(delete=False)
        self.last_modification_time = None
        self.first_run              = False
        self.is_updated             = False
        self.differences            = []
        self.cache_sync_file        = cache_sync_file
        
        
    def update_allowed(self):
        self.last_modification_time = os.stat(self.cache_sync_file).st_mtime
        minimum_modification_time   = self.last_modification_time + constants.SYNC_MIN_UPDATE_INTERVAL

        d = datetime.datetime.now()
        current_timestamp = time.mktime(d.timetuple())

        return True if minimum_modification_time <= current_timestamp else False

    def _attempt_to_update(self):

        if not self.update_allowed(): return False

        url_handler = urllib.urlopen(self.update_data_url)
        buffer_data = url_handler.read()
        
        # Do this only in case that document status is OK and if update is allowed ...
        if url_handler.getcode() >= 200 and url_handler.getcode() < 300:

            if os.path.getsize(self.cache_sync_file) == 0:
                self.first_run  = True
                self.tld_data_file.write(buffer_data)
                self.tld_data_file.close()
                return False

            # Now what we need to do is to "diff stuff"
            self.tld_diff_file.write(buffer_data)
            self.tld_diff_file.close()

            tld_diff_file_buff       = open(self.tld_diff_file.name, 'r')
            local_tld_sync_file_buff = open(self.cache_sync_file, 'r' )

            local_diff_set_file = set(tld_diff_file_buff)
            local_data_set_file = set(local_tld_sync_file_buff)

            file_differences    = local_diff_set_file.difference(local_data_set_file)
            tld_diff_file_buff.close()
            local_tld_sync_file_buff.close()

            requires_write      = False

            for difference in file_differences:
                if len(difference) > 2 and not difference.startswith("//"):
                    diff_final = difference.replace("\n", "")
                    diff_final = diff_final.replace("*.", "")
                    diff_final = diff_final.replace("!", "")
                    self.differences.insert(len(self.differences), diff_final)
                    requires_write = True

            if requires_write:
                self.is_updated = True
                self.tld_data_file.truncate()
                self.tld_data_file.write(buffer_data)
                self.tld_data_file.close()
                return True

            # Touch the file
            os.utime(self.cache_sync_file, None)
            os.unlink(self.tld_diff_file.name)

            print self.tld_diff_file.name
            print os.path.exists(self.tld_diff_file.name)

        return False


    def get_differences(self):
        return self.differences

    def update_schema(self):
        return self._attempt_to_update()
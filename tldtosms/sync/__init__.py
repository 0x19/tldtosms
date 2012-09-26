import sys, os, logging, time, datetime, urllib
from tldtosms import exceptions, constants

class Updater(object):

    def __init__(self):
        object.__init__(self)

        self.update_data_url        = constants.SYNC_DATA_URL
        self.tld_data_file          = constants.SYNC_DATA_FILE
        self.tld_diff_file          = constants.SYNC_DIFF_FILE
        self.last_modification_time = None
        self.first_run              = False
        self.is_updated             = False
        self.differences            = []
        
        self._calculate_minimum_update_interval()


    def _calculate_minimum_update_interval(self):
         d = datetime.datetime.now()
         self.minimum_update_interval = time.mktime(d.timetuple()) + constants.SYNC_MIN_UPDATE_INTERVAL


    def _attempt_to_update(self):
        
        # First let's go get latest file update ...
        self.last_modification_time = os.path.getmtime(self.tld_data_file)
        
        # Minimum update interval lock is OK
        if self.last_modification_time < self.minimum_update_interval:

            # Now let's go grab the file ...
            dat_handler = urllib.urlopen(self.update_data_url)
            buffer_data = dat_handler.read()

            # Write that file buffer to local diff file...
            local_diff_file = open(self.tld_diff_file, "w+")
            local_diff_file.write(buffer_data)
            local_diff_file.close()

            # In case that current dat file is empty, just write dat handler into
            # that file as well. If not, well....
            current_filesize = os.path.getsize(self.tld_data_file)

            # If filesize is less or equal to zero. 
            # That means that this is first update and therefore, there is no reason to do any diffs
            if current_filesize <= 0:
                self.first_run  = True
                local_data_file = open(self.tld_data_file, "w+")
                local_data_file.write(buffer_data)
                local_data_file.close()

            local_diff_file = open(self.tld_diff_file, "r")
            local_data_file = open(self.tld_data_file, "r")

            local_diff_set_file = set(local_diff_file)
            local_data_set_file = set(local_data_file)

            file_differences    = local_diff_set_file.difference(local_data_set_file)
            requires_write      = False

            for difference in file_differences:
                if len(difference) > 2 and not difference.startswith("//"):
                    diff_final = difference.replace("\n", "")
                    diff_final = diff_final.replace("*.", "")
                    diff_final = diff_final.replace("!", "")
                    self.differences.insert(len(self.differences), diff_final)
                    requires_write = True

            if requires_write:
                local_data_file = open(self.tld_data_file, "w+")
                local_data_file.write(buffer_data)
                local_data_file.close()
                self.is_updated = True
                return True

            # No update is available at this moment...
            return False


    def get_differences(self):
        return self.differences

    def update_schema(self):
        return self._attempt_to_update()
# single machine, many core and many spinning disks
# - durable before put returns
# - all of the data fits in memory
# - maximize throughtput of get/put

# File Size Limit
# Concurrency


# p(a, 1) ---- p(a, 2) --- at the same time from two different threads
# --- both operations have completed ---

# g(a) = 1
# g(a) = 1

# g(a) = 2
# g(a) = 2

# g(a) = 1
# g(a) = 2 --- not okay ---


# T1.     T2
# disk
#.        disk
#.        mem
# mem
    

SEP = "\t"

class EmbeddedDB(object):
    def __init__(self, db_file):
        self.fname = db_file
        try:
            fd = open(self.fname, 'w')
            # if file doesn't exist, need to create
            self.items_file = fd
        except ReadError:
            raise DBNotAvailableError
        self.loadDB()
       
    def loadDB(self):
        for line in self.items_file.read_lines():
            k, v = line.split(SEP)
            self.items[k] = v
   
    # Returns True on durable put to disk.
    # If False, user should retry put (no durability guarantee).
    def put(self, key, value):
        err = self.items_file.write("%s%s%s" % (key, SEP, value))
        if err is not None:
            # can crash here, but put will not have succeeded
            self.items[key] = value
            return True
        else:
            return False
   
    # Return None if key doesn't exist.
    def get(self, key):
        if key not in self.items:
            return None
        else:
            return self.items[key]
        
# Client code        
db = EmbeddedDB("items.txt")

db.put()
db.get()

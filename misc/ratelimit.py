import time

class RateLimiter(object):
    def __init__(self, N, T):
        self.N = N
        self.T = T
        self.client_requests = {}

    def is_rate_limited(self, client_id):
        now = time.time()
        # no recent requests
        if client_id not in self.client_requests:
            self.client_requests[client_id] = [now]
            return False
        else:
            requests = self.client_requests[client_id]
            recent_requests = filter(lambda ts: ts > now - self.T, requests)
            # print "Recent_requests"
            if len(recent_requests) < self.N:
                rec
                requests.append(now)
                
                return False
            else:
                return True
            
    def trim_request_logs(self, client_id):
        now = time.time()
         

rlim = RateLimiter(10, 60)

client1 = 1

for i in xrange(100):
    result = rlim.is_rate_limited(client1)
    print "Request(%d) -> %s" % (i, result)

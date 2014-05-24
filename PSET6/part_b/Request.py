# Code below is given to you as infrastructure
# You do not need to (nor should yoU) make any changes to the code below
#
#  Request := a named request i of size [a,b] that can be queried by:
#  len(i) := length of the request (# of time slots in request)
#  name(i) := string name associated with the request
#  start(i) := first time slot of the request (a)
#  end(i) := last time slot of the request (b)
#  INVARIANT: start(i) <= end(i)
#  The following functions are also defined:
class Request:
  def __init__(self, name, start, end):
    if (start > end):
      raise Exception("Error: attempted to create an request with end < start")
      
    self.name = name
    self.start = start
    self.end = end
    
  def __len__(self):
    return self.end - self.start + 1
  
  def __repr__(self):
    return str(self)
  
  def __str__(self):
    return self.name + ': [' + str(self.start) + ", " + str(self.end) + "]"
        
start = lambda i: i.start
end = lambda i: i.end
name = lambda i: i.name

# is_overlapping: return true if time slots specified by request a overlaps request b
# return valse otherwise
def is_overlapping(a, b):
  return ((b.start <= a.end) and (a.start <= b.end))

# sort_requests: sorts a list of requests by a given criteria
# sort_by can be one of : {name, len, start, end}
def sort_requests(requests, sort_by):
  key_function = lambda i: sort_by(i)
  sorted_requests = sorted(requests, key=key_function)
  return sorted_requests

# Randomized test generation
# Note - this does not tell you what the optimal schedule utilization is!
# Use as you see fit if you wish
def make_requests(num_requests, max_time, max_length, min_length):
  requests = []
  import random
  for i in range(0, num_requests):
    length = min_length + random.randint(0,max_length-min_length)
    start_time = random.randint(0,max_time - length - 1)
    requests.append(Request(str(i), start_time, start_time+length+1))
  return requests
  
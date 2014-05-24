# Code below is given to you as infrastructure
# You do not need to (nor should yoU) make any changes to the code below

from Request import sort_requests, start

# verify: validates a proposed schedule
# A valid schedule must consist of a non-overlapping subset of requests
# Such that the sum of the lengths of scheduled requests is maximal
def verify(requests, schedule, optimal_utilization):
  utilization = validate_and_measure_schedule(requests, schedule)
  if (utilization != optimal_utilization):
    raise Exception("ERROR: the proposed schedule is not optimal!", schedule, utilization, optimal_utilization)

# helper function for verify routines
# makes sure the proposed schedule is a subset of requests, and measures its utilization.
def validate_and_measure_schedule(requests, schedule):
  # requests given as an unordered list
  # schedule also given as unordered list

  # make a set of requests for efficient membership checks
  from sets import Set
  requests_set = Set(requests)

  # check for intersections
  # this can be done efficiently with an request tree,
  # but request trees are complicated, and we don't need a dynamic 
  # data structure here (all requests are known up-front).

  # sort scheduled requests by start time
  sorted_schedule = sort_requests(schedule, start)

  prev_end = -1
  total = 0
  for request in sorted_schedule:
    # make sure the request is in the problem statement
    # this also makes sure the request is within the bounds of the problem
    if (request not in requests_set):
      raise Exception("ERROR: Found an request in the proposed schedule that was not in the set of candidate requests!", str(request))
    
    # make sure the request does not overlap with earlier request
    if request.start <= prev_end:
      raise Exception("ERROR: request overlaps earlier request - invalid schedule", str(request))
    prev_end = request.end
    
    # calculate up the utilization of the proposed schedule
    total += len(request)
    
  return total

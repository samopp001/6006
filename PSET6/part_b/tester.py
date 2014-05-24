# Code below is given to you as infrastructure
# You do not need to (nor should yoU) make any changes to the code below
#

from VerifySchedule import verify
from Request import *
from PSET6 import create_schedule
import time
import pickle

# run scheduling algorithm and verify its length is equal to optimal_length
def run_tests(requests, optimal_length, name):
  print "Running test: " + name
  print "Requests: " + str(requests)
  requests_copy = requests
  
  start = time.time()
  schedule = create_schedule(requests)
  end = time.time()
  
  print "Schedule: " + str(schedule)
  print "Time to compute schedule : " + str(end - start) + " seconds"
  
  verify(requests_copy, schedule, optimal_length)
  print ""
  
def run_tests_from_file(filename, name, should_print):
  print "Running test: " + name
  [optimal_length, requests] = pickle.load(open(filename, 'rb'))
  if should_print: print "Requests: " + str(requests)
  requests_copy = requests
  
  start = time.time()
  schedule = create_schedule(requests)
  end = time.time()
  
  if should_print: print "Schedule: " + str(schedule)
  print "Time to compute schedule : " + str(end - start) + " seconds"
  
  verify(requests_copy, schedule, optimal_length)
  print ""

# Tiny tests  
def test_tiny_1():
  requests = []
  requests.append(Request("Stanford", 0,1))
  requests.append(Request("MIT", 2,3))
  requests.append(Request("UC Berkeley", 4,5))
  
  run_tests(requests, 6, "Tiny 1")
  
def test_tiny_2():
  requests = []
  requests.append(Request("Stanford", 0,1))
  requests.append(Request("MIT", 1,2))
  requests.append(Request("UC Berkeley", 2,3))
  
  run_tests(requests, 4, "Tiny 2")

def test_tiny_3():
  requests = []
  requests.append(Request("Stanford", 0,2))
  requests.append(Request("MIT", 1,9))
  requests.append(Request("UC Berkeley", 4,5))
  
  run_tests(requests, 9, "Tiny 3")
  
def test_tiny_4():
  requests = []
  requests.append(Request("Stanford", 1,3))
  requests.append(Request("MIT", 4,9))
  requests.append(Request("UC Berkeley", 0,7))
  
  run_tests(requests, 9, "Tiny 4")

# Small tests
def test_small_1():
  run_tests_from_file("small_1.pickle", "Small 1", False)
  
def test_small_2():
  run_tests_from_file("small_2.pickle", "Small 2", False)

def test_small_3():
  run_tests_from_file("small_3.pickle", "Small 3", False)
  
# Medium tests
def test_medium_1():
  run_tests_from_file("medium_1.pickle", "Medium 1", False)
  
def test_medium_2():
  run_tests_from_file("medium_2.pickle", "Medium 2", False)

def test_medium_3():
  run_tests_from_file("medium_3.pickle", "Medium 3", False)

# Large tests
def test_large_1():
  run_tests_from_file("large_1.pickle", "Large 1", False)
  
def test_large_2():
  run_tests_from_file("large_2.pickle", "Large 2", False)

def test_large_3():
  run_tests_from_file("large_3.pickle", "Large 3", False)
  
# Huge tests
def test_huge_1():
  run_tests_from_file("huge_1.pickle", "Huge 1", False)

# Test definitions
print "Tiny tests!"
test_tiny_1()
test_tiny_2()
test_tiny_3()
test_tiny_4()

print "Small tests!"
test_small_1()
test_small_2()
test_small_3()

print "Medium tests!"
test_medium_1()
test_medium_2()
test_medium_3()

print "Large tests!"
test_large_1()
test_large_2()
test_large_3()

print "Huge tests!"
test_huge_1()

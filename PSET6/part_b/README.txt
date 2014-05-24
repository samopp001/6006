Note: this assignment is relatively open-ended, and is therefore yours to debug. While we attempt to provide a varied set of test cases, ranging from tiny to large, debugging this assignment will likely be more difficult than what you have previously experienced in 6.006. Write your code carefully, keep track of invariants, avoid the temptation to create messy hacks, and test your helper functions (if you write any). Testing pieces of your code separately may save you a lot of debugging time.

- if you are failing a test, your schedule is not optimal. Try your solution with small hand-written test cases.
- Add printout statements generously to your code to visualize what happens
- If your code times out, your implementation is not efficient. Think about your sub-problems for dynamic programming.
- make your own test cases! You are creating a self-contained data structure.
- you may find it useful to use make_requests in your own test cases. This function takes 4 arguments:
  num_requests - number of randomized requests to generate
  max_time - the maximum end time of any request
  max_length - the maximum length of any request
  min_length - minimum length of any request
  
  Note that the function does NOT give you a solution to the scheduling problem, meaning it is not useful for testing the correctness of your code with large cases - only for seeding the input.

- When lost, gather information (printouts, stepping through code, etc.) until you have a good handle on
  where the problem is. Avoid making random changes hoping the problem goes away (even if it does, it
  will probably resurface in a yet more confusing setting).

Expected output is given below (note your run times will vary):

Tiny tests!
Running test: Tiny 1
Requests: [Stanford: [0, 1], MIT: [2, 3], UC Berkeley: [4, 5]]
Schedule: [Stanford: [0, 1], MIT: [2, 3], UC Berkeley: [4, 5]]
Time to compute schedule : 0.000999927520752 seconds

Running test: Tiny 2
Requests: [Stanford: [0, 1], MIT: [1, 2], UC Berkeley: [2, 3]]
Schedule: [Stanford: [0, 1], UC Berkeley: [2, 3]]
Time to compute schedule : 0.0 seconds

Running test: Tiny 3
Requests: [Stanford: [0, 2], MIT: [1, 9], UC Berkeley: [4, 5]]
Schedule: [MIT: [1, 9]]
Time to compute schedule : 0.0 seconds

Running test: Tiny 4
Requests: [Stanford: [1, 3], MIT: [4, 9], UC Berkeley: [0, 7]]
Schedule: [Stanford: [1, 3], MIT: [4, 9]]
Time to compute schedule : 0.00100016593933 seconds

Small tests!
Running test: Small 1
Time to compute schedule : 0.0 seconds

Running test: Small 2
Time to compute schedule : 0.0 seconds

Running test: Small 3
Time to compute schedule : 0.0 seconds

Medium tests!
Running test: Medium 1
Time to compute schedule : 0.0019998550415 seconds

Running test: Medium 2
Time to compute schedule : 0.0019998550415 seconds

Running test: Medium 3
Time to compute schedule : 0.00200009346008 seconds

Large tests!
Running test: Large 1
Time to compute schedule : 0.0680000782013 seconds

Running test: Large 2
Time to compute schedule : 0.066999912262 seconds

Running test: Large 3
Time to compute schedule : 0.0709998607635 seconds

Huge tests!
Running test: Huge 1
Time to compute schedule : 6.03399991989 seconds

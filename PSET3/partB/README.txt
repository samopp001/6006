Note: all tests for all 3 dictionary implementation assume that your insert and search operations work correctly. While the test.py script attempts to find errors soon after they occur to simplify debugging, you may find it useful to use these good strategies for debugging your code:

- if you are failing a test, set printout (last argument to numbersTest) to True in the tester script.
- Add printout statements generously to your code to visualize what happens
- make your own test cases! You are creating a self-contained data structure.
- you may find it useful to use numbersTest in your own test cases. This funciton takes 3 lists:
  a list of insertions to perform, a list of deletions to perform, and a list of searches. The function checks to make sure the dictionary contains all the items it should after each step.
- You may wish to not do this assignment last-minute to avoid delays getting feedback from ALG.
- When lost, gather information (printouts, stepping through code, etc) until you have a good handle on
  where the problem is. Avoid making random changes hoping the problem goes away (even if it does, it
  will probably resurface in a yet more confusing setting).

Expected output is given below (note your run times will vary):

Test 1
OK: dictionary with linear probing seems to work with a light load. The test took 0.000999927520752 seconds.

Test 2
OK: Doubly-hashed dictionary seems to work with a light load. The test took 0.00200009346008 seconds.

Test 3
OK: Cuckoo Dictionary seems to work with a light load. The test took 0.0 seconds.

Test 4
OK: dictionary with linear probing seems to work with a larger load. The test took 2.28999996185 seconds.

Test 5
OK: Doubly-hashed dictionary seems to work with a larger load. The test took 4.67200016975 seconds.

Test 6
OK: Cuckoo Dictionary seems to work with a larger load. The test took 0.0519998073578 seconds.

Test 7
There are 6905 film entries
There are 16588 actor entries
OK: Career change to James Caan due to The Godfather : -1.41333333333
OK: Career change to Marlon Brando due to The Godfather : -0.661428571429


OK: Career change to Matt Damon due to Good Will Hunting : -0.027380952381
OK: Career change to Robin Williams due to Good Will Hunting : -0.160428571429


OK: Career change to Brad Pitt due to Fight Club : -0.345684210526
OK: Career change to Edward Norton due to Fight Club : -0.997857142857


OK: Career change to Pierce Brosnan due to GoldenEye : -0.319130434783
OK: Career change to Michelle Arthur due to GoldenEye : -0.388888888889


OK: Career change to Halle Berry due to Die Another Day : -0.50303030303
OK: Career change to Rosamund Pike due to Die Another Day : 0.607692307692


OK: Career change to Kate Winslet due to Titanic : -0.736842105263
OK: Career change to Leonardo DiCaprio due to Titanic : 1.13857142857


OK: Career change to Tom Hanks due to Big : 1.16578947368
OK: Career change to Elizabeth Perkins due to Big : -0.411538461538


OK: Career change to Robin Wright due to Forrest Gump : -0.708695652174
OK: Career change to Tom Hanks due to Forrest Gump : 0.916430020284


OK: Career change to Mike Myers due to The Love Guru : 1.22333333333
OK: Career change to Jessica Alba due to The Love Guru : -0.314583333333


OK: Career change to Carmen Electra due to Disaster Movie : 0
OK: Career change to Christopher Born due to Disaster Movie : 1.425


OK: Career change to James DeBello due to The Hillz : 0.4
OK: Career change to Paris Hilton due to The Hillz : -0.804166666667


OK: Career change to Bruce Willis due to Die Hard : -0.892424242424
OK: Career change to Bonnie Bedelia due to Die Hard : -1.05333333333


OK: Career change to Tom Hanks due to The Bonfire of the Vanities : 1.35931372549
OK: Career change to Melanie Griffith due to The Bonfire of the Vanities : -0.0663461538462


OK: Career change to Michael Cera due to Superbad : -1.38214285714
OK: Career change to Jonah Hill due to Superbad : 0.292613636364


OK: Career change to Daniel Craig due to Casino Royale : -0.272222222222
OK: Career change to Eva Green due to Casino Royale : -0.941666666667
OK: Career change to Judi Dench due to Casino Royale : 0.0969696969697
Ok, imdb queries seem to be correct. Great job!. The test took 2.4470000267 seconds.


# Test:
# 
# test N inserts and 1 lookup
# 
# test capacity:
# - H can hold up to n elements
# - H fails to hold n+1 elements
# 
# - H can function with a small loading factor
# - H can function with a large loading factor
# - H can function after being trashed
# 
# H is initialized to (None, None) in every location

from OpenAddressedHashArray import *
from AuxHashFunctions import *
from numbers import *
from PSET3 import *
import time

# Test helpers
def insertNumber(D, i):
    if not D.insert("one", 1): raise Exception("Failed to insert "+ i + " into dictionary!")

def numbersTest(D, insertions, deletions, searches, printout):
    # Assumes a dictionary D,
    #  integer arrays {insertions, deletions, searches}
    #  boolean printout
    #
    # attempts to insert each element in insertions into D
    # then attempts to delete each element in deletions from D
    # then attempts to find each element in searches in D
    # all the while checking that valid operations succeed, and
    # invalid operations fail
    #
    # Duplicates are allowed and are correctly resolved
    # Operations will be performed in order given
    #
    # prints a log if printout is True
    
    insertions_seen = []
    deletions_seen = []
    
    # Insert a bunch of elements
    for k in insertions:
        key = str(k)
        should_succeed = (k not in insertions_seen)
        v = num2str(k) if should_succeed else "INVALID"
        result = D.insert(key, v)
        
        if printout: print("Insert (" + str(k) + " --> " + str(v) + ") : " + ("True" if result else "False"))
        
        if should_succeed != result:
            raise Exception(("Succeeded" if result else "Failed") + " to insert " + str(k) + " into D, but should not have!")
        insertions_seen.append(k)
        
        # Check to make sure nothing was overridden
        for k in insertions_seen:
            key = str(k)
            result = D.search(key)
            if result is None:
                raise Exception("Failed to find key=" + str(k) + " in dictionary after it was inserted. This is not correct.")
            elif result == "INVALID":
                raise Exception("A redundant insertions into key=" + str(k) + " appears to have modified the table. This is not correct.")
    
    # Perform a bunch of deletions
    for k in deletions:
        key = str(k)
        should_succeed = (k in insertions) and (k not in deletions_seen)
        result = D.delete(key)
        
        if printout: print("Delete (" + str(k) + ") : " + ("True" if result else "False"))
        
        if should_succeed != result:
            raise Exception(("Succeeded" if result else "Failed") + " to delete " + str(k) + " from the dictionary, but should not have!")
        deletions_seen.append(k)
        
        # Now make sure that deletions removed exactly the keys they were supposed to remove
        for k in insertions:
            key = str(k)
            should_be_in = (k not in deletions_seen)
            result = D.search(key)
            
            if should_be_in and (result is None):
                raise Exception("Failed to find key=" + str(k) + " in dictionary after it was inserted, and other items were deleted. This is not correct.")
            elif (not should_be_in) and (result is not None):
                raise Exception("Failed to remote key=" + str(k) + " from the dictionary after it was deleted. This is not correct.")
    
    # Perform a bunch of searches
    for k in searches:
        key = str(k)
        correct_value = num2str(k);
        should_succeed = (k in insertions) and (k not in deletions)
        result = D.search(key)
        
        if printout: print("Search (" + str(k) + ") --> " + str(result))
        
        if should_succeed and (result is None):
            raise Exception("Failed to find an entry for k=" + str(k) + ", but it should be in the dictionary! This is wrong")
        elif should_succeed and (result != correct_value):
            raise Exception("Found a mapping (k=" + str(k) + " -> v=" + str(result) +") in the dictionary, but should have found (k=" + str(k) + " -> v=" + str(correct_value) +"). This is wrong.")
        elif (not should_succeed) and (result is not None):
            raise Exception("Found a mapping (k=" + str(k) + " -> v=" + str(result) +") in the dictionary, but key should not be mapped! This is wrong.")
        
        deletions_seen.append(k)
        
    # Now make sure that searches did not change dictionary membership
    for k in insertions:
        key = str(k)
        should_be_in = (k not in deletions)
        result = D.search(key)
        
        if should_be_in and (result is None):
            raise Exception("Failed to find key=" + str(k) + " in dictionary after some searches. This is not correct: searches should not modify the dictionary!")
        elif (not should_be_in) and (result is not None):
            raise Exception("Erroneously found deleted key=" + str(k) + " in the dictionary after some searches. This is not correct: searches should not modify the dictionary!")

def imdb_career_impact(db, film, actor, career_impact):
    change = db.career_impact(film, actor)
    epsilon = 0.001
    
    if (abs(career_impact-change)>epsilon):
        raise Exception("FAIL: Career change to " + actor + " due to " + film + " is calculated to be " + str(change) + ", but should be closer to " + str(career_impact))
    
    print ("OK: Career change to " + actor + " due to " + film + " : " + str(change))

# Tests

#
# Run a series of tests
#

#test 1:
aux_hash_functions = AuxHashFunctions()
Array = OpenAddressedHashArray(10)
hash_functions = HashFunctions(aux_hash_functions)

D = OpenAddressedDictionary(Array, hash_functions.linear_probing_hash)

file_start = time.time()

print("\nTest 1")
try:
    start = time.time()
    numbersTest(D, range(0,10), range(0,5), range(0,10), False)
    end = time.time()
    print("OK: dictionary with linear probing seems to work with a light load. The test took " + str(end - start) + " seconds.")
except Exception as e:
    print("FAIL!: dictionary with linear probing failed with a light load.")
    print("  re-run the test with True as the last argument to print a trace.")
    print(e)

#test 2:
aux_hash_functions = AuxHashFunctions()
Array = OpenAddressedHashArray(10)
hash_functions = HashFunctions(aux_hash_functions)

D = OpenAddressedDictionary(Array, hash_functions.double_hashing_hash)

print("\nTest 2")
try:
    start = time.time()
    numbersTest(D, range(0,10), range(0,5), range(0,10), False)
    end = time.time()
    print("OK: Doubly-hashed dictionary seems to work with a light load. The test took " + str(end - start) + " seconds.")
except Exception as e:
    print("FAIL!: Doubly-hashed dictionary failed with a light load.")
    print("  re-run the test with True as the last argument to print a trace.")
    print(e)
    
#test 3:
aux_hash_functions = AuxHashFunctions()
Array = OpenAddressedHashArray(10)
hash_functions = HashFunctions(aux_hash_functions)

D = CuckooDictionary(Array, aux_hash_functions)

print("\nTest 3")
try:
    start = time.time()
    numbersTest(D, range(0,5), range(0,3), range(0,5), False)
    end = time.time()
    print("OK: Cuckoo Dictionary seems to work with a light load. The test took " + str(end - start) + " seconds.")
except Exception as e:
    print("FAIL!: Cuckoo Dictionary failed with a light load.")
    print("  re-run the test with True as the last argument to print a trace.")
    print(e)

#test 4:
aux_hash_functions = AuxHashFunctions()
Array = OpenAddressedHashArray(1000)
hash_functions = HashFunctions(aux_hash_functions)

D = OpenAddressedDictionary(Array, hash_functions.linear_probing_hash)

print("\nTest 4")
try:
    start = time.time()
    numbersTest(D, range(0,700), range(0,200), range(0,700), False)
    end = time.time()
    print("OK: dictionary with linear probing seems to work with a larger load. The test took " + str(end - start) + " seconds.")
except Exception as e:
    print("FAIL!: dictionary with linear probing failed with a larger load.")
    print("  re-run the test with True as the last argument to print a trace.")
    print(e)

#test 5:
aux_hash_functions = AuxHashFunctions()
Array = OpenAddressedHashArray(1000)
hash_functions = HashFunctions(aux_hash_functions)

D = OpenAddressedDictionary(Array, hash_functions.double_hashing_hash)

print("\nTest 5")
try:
    start = time.time()
    numbersTest(D, range(0,700), range(0,200), range(0,700), False)
    end = time.time()
    print("OK: Doubly-hashed dictionary seems to work with a larger load. The test took " + str(end - start) + " seconds.")
except Exception as e:
    print("FAIL!: Doubly-hashed dictionary failed with a larger load.")
    print("  re-run the test with True as the last argument to print a trace.")
    print(e)
    
#test 6:
aux_hash_functions = AuxHashFunctions()
Array = OpenAddressedHashArray(500)
#Array = OpenAddressedHashArray(1000)
hash_functions = HashFunctions(aux_hash_functions)

D = CuckooDictionary(Array, aux_hash_functions)

print("\nTest 6")
try:
    start = time.time()
    numbersTest(D, range(0,100), range(0,50), range(0,100), False)
    #numbersTest(D, range(0,300), range(0,200), range(0,300), True)
    end = time.time()
    print("OK: Cuckoo Dictionary seems to work with a larger load. The test took " + str(end - start) + " seconds.")
except Exception as e:
    print("FAIL!: Cuckoo Dictionary failed with a larger load.")
    print("  re-run the test with True as the last argument to print a trace.")
    print(e)
    
#test 7:
print("\nTest 7")
try:
    aux_hash_functions = AuxHashFunctions()
    hash_functions = HashFunctions(aux_hash_functions)
    array_large = OpenAddressedHashArray(30000)
    array_small = OpenAddressedHashArray(10000)

    start = time.time()
    imdb = IMDB(array_large, array_small, hash_functions.linear_probing_hash, hash_functions.double_hashing_hash)

    imdb_career_impact(imdb, "The Godfather", "James Caan", -1.41333333333)
    imdb_career_impact(imdb, "The Godfather", "Marlon Brando", -0.661428571429)
    print "\n"
    imdb_career_impact(imdb, "Good Will Hunting", "Matt Damon", -0.027380952381)
    imdb_career_impact(imdb, "Good Will Hunting", "Robin Williams", -0.160428571429)
    print "\n"
    imdb_career_impact(imdb, "Fight Club", "Brad Pitt", -0.345684210526)
    imdb_career_impact(imdb, "Fight Club", "Edward Norton", -0.997857142857)
    print "\n"
    imdb_career_impact(imdb, "GoldenEye", "Pierce Brosnan", -0.319130434783)
    imdb_career_impact(imdb, "GoldenEye", "Michelle Arthur", -0.388888888889)
    print "\n"
    imdb_career_impact(imdb, "Die Another Day", "Halle Berry", -0.50303030303)
    imdb_career_impact(imdb, "Die Another Day", "Rosamund Pike", 0.607692307692)
    print "\n"
    imdb_career_impact(imdb, "Titanic", "Kate Winslet", -0.736842105263)
    imdb_career_impact(imdb, "Titanic", "Leonardo DiCaprio", 1.13857142857)
    print "\n"
    imdb_career_impact(imdb, "Big", "Tom Hanks", 1.16578947368)
    imdb_career_impact(imdb, "Big", "Elizabeth Perkins", -0.411538461538)
    print "\n"
    imdb_career_impact(imdb, "Forrest Gump", "Robin Wright", -0.708695652174)
    imdb_career_impact(imdb, "Forrest Gump", "Tom Hanks", 0.916430020284)
    print "\n"
    imdb_career_impact(imdb, "The Love Guru", "Mike Myers", 1.22333333333)
    imdb_career_impact(imdb, "The Love Guru", "Jessica Alba", -0.314583333333)
    print "\n"
    imdb_career_impact(imdb, "Disaster Movie", "Carmen Electra", 0)
    imdb_career_impact(imdb, "Disaster Movie", "Christopher Born", 1.425)
    print "\n"
    imdb_career_impact(imdb, "The Hillz", "James DeBello", 0.4)
    imdb_career_impact(imdb, "The Hillz", "Paris Hilton", -0.804166666667)
    print "\n"
    imdb_career_impact(imdb, "Die Hard", "Bruce Willis", -0.892424242424)
    imdb_career_impact(imdb, "Die Hard", "Bonnie Bedelia", -1.05333333333)
    print "\n"
    imdb_career_impact(imdb, "The Bonfire of the Vanities", "Tom Hanks", 1.35931372549)
    imdb_career_impact(imdb, "The Bonfire of the Vanities", "Melanie Griffith", -0.0663461538462)
    print "\n"
    imdb_career_impact(imdb, "Superbad", "Michael Cera", -1.38214285714)
    imdb_career_impact(imdb, "Superbad", "Jonah Hill", 0.292613636364)
    print "\n"
    imdb_career_impact(imdb, "Casino Royale", "Daniel Craig", -0.272222222222)
    imdb_career_impact(imdb, "Casino Royale", "Eva Green", -0.941666666667)
    imdb_career_impact(imdb, "Casino Royale", "Judi Dench", 0.0969696969697)
    print "\n"
    print("OK: IMDb queries seem to be correct. Great job! The IMDb test took " + str(end - start) + " seconds.")
except:
    print("FAIL: IMDB code threw an exception.")
    print(e)
 
end = time.time()
print "\n"
print(" tester.py finished in " + str(end - file_start) + " seconds")


from AuxHashFunctions import *
import pickle

class HashFunctions:
    def __init__(self, hash_functions):
        
        # Auxiliary hash functions
        self.aux_h1 = hash_functions.hash_1
        self.aux_h2 = hash_functions.hash_2
        
    def linear_probing_hash(self, key, i, m):
        # Use auxiliary hash function self.h1(k) to
        # implement linear probing - a hash function of the form h(k, i) in range [0 ... m-1]
        # See CLRS pp272 for details
        
	# hash = hashfunction1(key) + i mod m
        return ((self.aux_h1(key, m) + i) % m)
        
    def double_hashing_hash(self, key, i, m):
        # Use auxiliary hash functions self.h1(k) and self.h2(k)
        # to implement double hashing - a hash function of the form h(k, i) in range [0 ... m-1]
        # See CLRS pp272-274 for details
        
        # hash = (hashfunction1(key) + hashfunction2(key) * 1) mod m
	return ((self.aux_h1(key, m) + self.aux_h2(key, m)* i) % m)
		

class OpenAddressedDictionary:
    def __init__(self, array, hash_function):
        # use self.array to store your key-value pairs. The array is pre-allocated, and has capacity m.
        # Initially, all elements of self.array are set to (None, None)
        # 
        self.array = array;
        
        # the fixed, static capacity of self.array is exactly m
        self.m = len(array)
        
        # this hash function h(k, i, m) can be used to map a key k to an index in range [0 .. m-1]
        self.hash_function = hash_function;

    def insert(self, key, value):
        # insert
        # - associate a key ("key") with a value ("value")
        #   in a dictionary ("self.array"), provided the key 
        #   is not already in the dictionary, and return True.
        #   If the key is in the dictionary already, return False, and
        #   do not modify the dictionary. Also return False if the dictionary is full.
        #
        # Return Value:
        # - True if "insert" succeeds (i.e. key not already mapped, dictionary not full)
        # - False otherwise (i.e. key already mapped to a value, or dictionary is full).
        #  Do not modify the dictionary in if insertion fails!
        #
        # TODO: Use open addressing (the hhash_function provided specifies the exact strategy among linear probing and double hashing)
        # to implement insert. Feel free to create helper methods.
        
        i = 0
        # While loop will run through the table
        while (i != self.m):
            # Defines hash function once 
            j = self.hash_function(key, i , self.m)
            # If spot is empty of deleted value
            if (self.array[j] == (None, None) or self.array[j] == 'delete'):
                # Place key in table at the location
                self.array[j] = (key, value)
                return True
            # Iterate through table until no more spaces
            i += 1
        return False

    def delete(self, key):
        # delete
        # - remove from the dictionary ("self.array" the key-value mapping
        #   given by a key ("key"), provided the mapping exists.
        #
        # Return Value:
        # - True if "delete" succeeds (key was present in the dictionary)
        # - False otherwise (key was not present in the dictionary)
        
        i = 0
        # While loop will run through the table
        while (i != self.m): 
            # Define hash function once
            j = self.hash_function(key, i, self.m)
            # Pop key when found and replace with string
            if self.array[j][0] == key:
                self.array[j] = 'delete'
                return True
            # Not in the table value
            if self.array[j] == (None, None):
                return False
            # Iterate through table until no more spaces
            i += 1
        return False
		

    def search(self, key):
        # search
        # - find and return the value associated with "key" in the dictionary (self.array).
        #   Return None if the key is not in the dictionary.
        #
        # Return Value:
        # - the value associated with "key" if the key is in the dictionary.
        # - None if the key is not in the dictionary.
        
	i = 0
        # While loop will run through the table
        while (i != self.m):
            # Define hash function once
            j = self.hash_function(key, i, self.m)
            # If not in the table return none
            if self.array[j] == (None, None):
                return None
            elif self.array[j][0] == key:
                # If in the table return value
                return self.array[j][1]
            # Iterate through table until no more spaces
            i += 1
        return None
		
		
class CuckooDictionary:
    def __init__(self, array, aux_hash_functions):
        # use self.array to store your key-value pairs. The array is pre-allocated, and has capacity m.
        # Initially, all elements of self.array are set to (None, None)
        # 
        self.array = array;
        
        # the fixed, static capacity of self.array is exactly m
        self.m = len(array)
        
        # self.h1 and self.h2 are two hash functions h(k, m) that map a key to an index in range [0 .. m-1]
        self.aux_hash_functions = aux_hash_functions
        self.h1 = aux_hash_functions.hash_1
        self.h2 = aux_hash_functions.hash_2
        
        # This is used to limit. You should not need to use this variable in your code.
        self.max_evicts = 10
    
    def insert(self, key, value):
        # insert
        # - associate a key ("key") with a value ("value")
        #   in a dictionary ("self.array"), provided the key 
        #   is not already in the dictionary, and return True.
        #   If the key is in the dictionary already, return False, and
        #   do not modify the dictionary. Also return False if the dictionary is full.
        #
        # Return Value:
        # - True if "insert" succeeds (i.e. key not already mapped, dictionary not full)
        # - False otherwise (i.e. key already mapped to a value, or dictionary is full).
        #  Do not modify the dictionary in if insertion fails!
        #
        # TODO: Use cuckoo hashing to implement insert. Feel free to create helper methods.

        
        if (self.search(key) is not None):
            return False
        else:
            j1 = self.h1(key, self.m)
             # If space available (empty or deleted)
            if self.array[j1] == (None, None) or self.array[j1] == 'delete':
                self.array[j1] = (key, value)
                return True
            else:
                temp = self.array[j1]
                self.array[j1] = (key, value) 
                (tempkey, tempvalue) = temp
                
            i = 0
            while i< self.max_evicts:
                j2 = self.h2(tempkey, self.m)
                # If not swap pointer and j in array 
                if self.array[j2] == (None, None) or self.array[j2] == 'delete':
                    self.array[j2] = (tempkey, value)
                    return True
                else:
                    temp = self.array[j1]
                    self.array[j1] = (tempkey, value) 
                    (tempkey, tempvalue) = temp
                    i += 1
                    
        # At this point, we've performed O(self.max_evicts evictions), and failed to complete the insertion.
        # We would normally rehash with new hash functions. You are not responsible for this in your Pset 3
        # because we designed our test cases to not require rehashing by keeping the load factor small.
        # If you design your own test cases, you may see failed insertions due to eviction loops.
        # This is to be expected, since, again you aren't responsible for rehash()
        
        #if not self.rehash(key, value):
        #    return False
        
        # re-insert the last evicted item (on next iteration).
        # The (key, value) pair is exactly the last evicted item that is currently not in the dictionary
        
        # Looks like we've failed to insert into the hash.
        # The reason is a high loading factor (the dictionary is more or less full), up to hash function quality.
        # It is appropriate to give up in this case
        #return True
        
        raise Exception("failed to insert a key into a Cuckoo dictionary. Our test cases are designed not to do this if you use h1 and h2 correctly.")
    
    def delete(self, key):
        # delete
        # - remove from the dictionary ("self.array" the key-value mapping
        #   given by a key ("key"), provided the mapping exists.
        #
        # Return Value:
        # - True if "delete" succeeds (key was present in the dictionary)
        # - False otherwise (key was not present in the dictionary)
        
        #raise NotImplementedError()
        
        # Define hash functions
        j1 = self.h1(key, self.m)
        j2 = self.h2(key, self.m)

        # Find key and replace with delete
        if self.array[j1][0] == key:
            self.array[j1] = 'delete'
            return True
        elif self.array[j2][0] == key:
            self.array[j2] = 'delete'
            return True
        return False

    def search(self, key):
        # search
        # - find and return the value associated with "key" in the dictionary (self.array).
        #   Return None if the key is not in the dictionary.
        #
        # Return Value:
        # - the value associated with "key" if the key is in the dictionary.
        # - None if the key is not in the dictionary.
        
        #raise NotImplementedError()
        
        # Define hash functions
	j1 = self.h1(key, self.m)
        j2 = self.h2(key, self.m)

        # Find and return value associate to key
        if self.array[j1][0] == key:
            return self.array[j1][1]
        elif self.array[j2][0] == key:
            return self.array[j2][1]
        return None
    
    def rehash(self, last_key, last_value):
        # enumarate all items in the array, and add the last-evicted key-value pair
        items = []
        for (key, value) in self.array:
            if key is not None:
                items.append((key, value))
        items.append((last_key, last_value))
        
        # clear the array!
        for i in range (0, self.m):
            self.array[i] = (None, None)
        
        # mutate to new hash functions
        self.aux_hash_functions.change_hash_functions()
        
        # re-insert all elements
        for (key, value) in items:
            self.insert(key, value)
        
        return True

# You may find this helpful when averaging ratings of multiple films
def mean(L):
    s = float(sum(L))
    l = len(L)
    
    if l != 0:
        return s/l
    else:
        raise Exception("mean of zero numbers is not defined! You tried to take a mean of an empty list.")

class IMDB:
    #
    # Arguments:
    # array_large - a pre-allocated array of 30000 elements (initially all (None, None) )
    # array_small - a pre-allocated array of 10000 elements (initially all (None, None) )
    #
    def __init__(self, array_large, array_small, linear_probing_hash, double_hashing_hash):
        
        # self.films_list is a list of film entries, where
        # each film entry is of the form [film, rating, year, [actors]], where
        #    film is a string film movie "Godfather"
        #    rating is a number (float)
        #    year is an integer
        #    [actors] is a list of strings of actors' names such as "Matt Daemon"
        #
        # There approximately 20000 film entries in self.actors_list.
        self.films_list = pickle.load(open('films_list.pickle', 'rb'))
        print ("There are " + str(len(self.films_list)) + " film entries")
        
        # self.actors_list is a list of actor entries, where
        # each actor entry is of the form [name, [films]], where
        #    name is a string name of the actor, such as "Matt Daemon"
        #    [films] is a list of string film titles such as ["Godfather", "Quantum of Solace", "Oldboy"]
        #
        # There approximately 8000 actor entries in self.actors_list.
        self.actors_list = pickle.load(open('actors_list.pickle', 'rb'))
        print ("There are " + str(len(self.actors_list)) + " actor entries")
        
        # Initialize the data structure you will use to implement career_impact queris below.
        # Use the two arrays as storage with caution - 20,000 films cannot fit in array_small
        
        # Initialize new list of actors 
        self.actors = OpenAddressedDictionary(array_large, linear_probing_hash)
        actorlistlen = len(self.actors_list)-1

        # Adds actors to new list
        for i in range(0, actorlistlen):
            self.actors.insert(self.actors_list[i][0], self.actors_list[i][1])

        # Initialize new list of films
        self.films = OpenAddressedDictionary(array_small, linear_probing_hash)
        filmslistlen = len(self.films_list)-1

        # Adds films to list with tuple of tuple (film, (rating, year))
        for i in range(0, filmslistlen):
            self.films.insert(self.films_list[i][0], (float(self.films_list[i][1]), int(self.films_list[i][2])))
    
    def career_impact(self, film, actor):
        # return a career impact metric for a given actor and a given film, as specified in the problem set  PDF
        
        # Initialize impact metric
        prevImpact = [float(0),0]
        newImpact = [float(0),0]
        
        for i in self.actors.search(actor):
            if self.films.search(i)[1] <= self.films.search(film)[1]:
                prevImpact[0] = float(prevImpact[0]) + float(self.films.search(i)[0])
                prevImpact[1] += 1
            else:
                newImpact[0] = float(newImpact[0]) + float(self.films.search(i)[0])
                newImpact[1] +=  1
        if newImpact[1] == 0:
            return 0
        

        oldAvg = float(prevImpact[0])/float(prevImpact[1])
        newAvg = float(newImpact[0])/float(newImpact[1])
        return (newAvg - oldAvg)
		

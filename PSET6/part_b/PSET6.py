from Request import *
import math
import operator

# BEGIN STUDENT CODE
####################

# Trial 1

# create_memoize
# input: requests := unordered list of Request objects
# output: memoize := unordered list of Request objects, a sub-set of requests
#     such that the requests inn the memoize are non-overlapping
#     and the total time slots are maximized

# def create_list(requests):
# 	templist = [requests[0]]
# 	i=0
# 	j=0
# 	boole = True
# 	while boole == True:
# 		while is_overlapping(requests[j],requests[i]) == True:
# 			if i <= len(requests):
# 				i += 1
# 		templist.append(requests[i])
# 		j = i
		
# 	return templist


# Trial 2

# def create_memoize(requests):
	# memoize = []
	# sortRequests = sort_requests(requests,start)
	# i = 0
	# sumList = []
	# q = 0
	# while i != math.ceil(len(requests)/2):
	# 	p = 0
	# 	tempList = create_list(sortRequests[i:])
	# 	for i in tempList:
	# 		p += len(i)
	# 	if p > q:
	# 		q = p
	# 		sumList = tempList
	# 	i += 1
	# return sumList


# Trial 3

# def create_memoize(requests):
# 	lenSorted = sort_requests(requests,len)
# 	endSorted = sort_requests((lenSorted[::-1]),end)
# 	memoize = [endSorted[0]]

# 	for i in endSorted[1:]:
# 		j = 1
# 		while j<=len(memoize):
# 			if is_overlapping(i,memoize[-1]) == False:
# 				memoize.append(i)
# 				break
# 			if (len(i)<len(memoize[-j])) and (is_overlapping(i,memoize[-(j+1)])):
# 				j +=1
# 			else:
# 				memoize = memoize[:(j)]
# 				memoize.append(i)
# 				break
# 	return memoize
  

# Trial 4

# def create_memoize(requests):
# 	memoize = []
# 	endSorted = sort_requests(requests,end)
# 	memoize = {}
# 	index = []
# 	time = {}
# 	for k in range(len(endSorted)):
# 		memoize[endSorted[k].start] = ([],'NONE')
# 		memoize[endSorted[k].end] = ([],'NONE')
# 		index.append((endSorted[k].start, 'start'))
# 		time[endSorted[k].start] = (len(index))
# 		index.append((endSorted[k].end, 'end'))
# 		time[endSorted[k].end] = (len(index), 'end')
# 	index = sorted(index)
# 	for i in endSorted:
# 		if memoize[i.start][1] == 'NONE':
# 			memoize[i.end] = ([i],i.len)
# 			indice = time[i.end] + 1
# 			while index[indice][1] != 'end':
# 				memoize[indice] = ([i],i.len)
# 	for i in range(len(endSorted)):
# 		print 'test'
# 		memoize[i] = max(memoize[p[i]],memoize[i-1])
# 	return memoize


# Trial 5

# def create_memoize(requests):
# 	endSorted = sort_requests(requests,end)
# 	memoize = {}
# 	index = set()
# 	time = {}
# 	for k in range(len(endSorted)):
# 		memoize[endSorted[k].start] = ([],0)
# 		memoize[endSorted[k].end] = ([],0)
# 		index.add(endSorted[k].start)
# 		index.add(endSorted[k].end)
# 	index = sorted(list(index))	
# 	for i in range(len(index)):
# 		request_time = index[i]
# 		time[request_time] = i
# 	for i in endSorted:
# 		if i.start > 0:
# 			path = memoize[index[time[i.start]-1]][0]
# 			path.append(i)
# 			cost = (memoize[index[time[i.start]-1]][1] + len(i))
# 			print i
# 		else:
# 			path = [i]
# 			cost = len(i)
# 		indices = time[i.end] 
# 		while memoize[index[indices]][1] < cost:
# 			memoize[index[indices]] = (path,cost)
# 			indices +=1
# 			if indices == len(index):
# 				break
# 			print memoize[index[indices]]
# 	return memoize[index[-1]][0]


def create_schedule(requests):
	memoize = []
	endRequests = sort_requests(requests, end)
	ending = endRequests[-1].end

	for i in range(ending + 1):
		memoize.append((0, []))

	for i in range(len(endRequests)):
		requestTime = endRequests[i].start
		prev_built_finish = endRequests[i-1].end
		newList = memoize[prev_built_finish][0]
		tempList = memoize[requestTime - 1][0]
		curtTime = requestTime - 1

		if curtTime != 0 and tempList == 0:
			for k in range(requestTime-1, 0, -1):
				tempList = memoize[k][0]

				if (tempList != 0 and not(is_overlapping(memoize[k][1][-1],endRequests[i]))):
					curtTime = k
					break
		tempList += len(endRequests[i])
	
		if newList >= tempList:
			memoize[endRequests[i].end] = memoize[prev_built_finish]
			
		else:
			memoize[endRequests[i].end] = (0, None)
			order = memoize[curtTime][1] + [endRequests[i]]
			length = memoize[curtTime][0]
			length += len(endRequests[i])
			memoize[endRequests[i].end] = (length, order)

		ending = endRequests[i].end

	schedule = memoize[ending][1]

	return schedule 



####################
# END STUDENT CODE

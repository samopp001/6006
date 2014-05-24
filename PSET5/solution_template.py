import argparse, math, sys, ast, time

# PART A: Fill in below the code for part a
def dijkstra(N, adjacency_list, source):
    res = [(float('infinity'),None)]*N
    res[0] = (0,-1)
    pq = PriorityQ()
    for i in xrange(N):
        pq.insert(i,'infinity')
    pq.decrease_priority(source,0)
    n=0
    while n < N:
        current = pq.extract_min()
        for i in adjacency_list[current]:
            new_distance = res[current][0] + i[1]
            if new_distance < res[i[0]][0]:
                res[i[0]] = (new_distance, current)
                pq.decrease_priority(i[0],new_distance)
        n +=1
    return res

# PART B: Fill in below the code for part b
def shortest_path(N, coords, roads, plant_index, dump_index):
    # coord = (x,y) of vertices
    # roads = (a,b) of edges (vertex,vertex)
    adjacency_list = []
    for i in range(N):
        adjacency_list.append([])
    for i in roads:
        startNode = i[0]
        startCo = coords[startNode]
        endNode = i[1]
        endCo = coords[endNode]
        xDiff = abs(startCo[0] - endCo[0])
        yDiff = abs(startCo[1] - endCo[1])
        distance = (xDiff**2 + yDiff**2)**0.5
        adjacency_list[startNode].append((endNode,distance))
    res = dijkstra(N, adjacency_list, plant_index)
    parent = res[dump_index][1]
    path = []
    path.insert(0,dump_index)
    while parent != plant_index:
        path.insert(0,parent)
        parent = res[parent][1]
    path.insert(0,plant_index)
    return path


# PART C: Fill in below the code for part c
def closest(N, coords, roads, plant_index, dump_indices, k):
    adjacency_list = []
    for i in range(N):
        adjacency_list.append([])
    for i in roads:
        startNode = i[0]
        startCo = coords[startNode]
        endNode = i[1]
        endCo = coords[endNode]
        xDiff = abs(startCo[0] - endCo[0])
        yDiff = abs(startCo[1] - endCo[1])
        distance = (xDiff**2 + yDiff**2)**0.5
        adjacency_list[startNode].append((endNode,distance))

    dumpster = []

    res = [(float('infinity'),None)]*N
    res[0] = (0,-1)
    pq = PriorityQ()
    for i in xrange(N):
        pq.insert(i,'infinity')
    pq.decrease_priority(plant_index,0)
    n=0
    while n < N and len(dumpster) < k:
        current = pq.extract_min()
        if current in dump_indices:
            dumpster.append(current)
        for i in adjacency_list[current]:
            new_distance = res[current][0] + i[1]
            if new_distance < res[i[0]][0]:
                res[i[0]] = (new_distance, current)
                pq.decrease_priority(i[0],new_distance)
        n +=1
    dumpster = sorted(dumpster)
    return dumpster

# PART D: Fill in below the code for part d
def least_spillage(N, adjacency_list, plant_index, dump_index):
    res = [(0,None)]*N
    res[0] = (1.0,-1)
    pq = PriorityQ()
    for i in xrange(N):
        pq.insert(i,float('infinity'))
    pq.decrease_priority(plant_index,0)
    n=0
    current = plant_index
    while current != dump_index:
        current = pq.extract_min()
        for i in adjacency_list[current]:
            new_distance = res[current][0]*i[1]
            if new_distance > res[i[0]][0]:
                res[i[0]] = (new_distance, current)
                pq.decrease_priority(i[0],1-new_distance)
    parent = res[dump_index][1]
    path = []
    path.insert(0,dump_index)
    while parent != plant_index:
        path.insert(0,parent)
        parent = res[parent][1]
    path.insert(0,plant_index)
    return path

######################################
# DO NOT CHANGE CODE BELOW THIS LINE #
######################################

class PriorityQ:
    def __init__(self):
        self.N = 0
        self.heap = [(0,0)]
        self.pos = {}

    def size(self):
        return self.N
    def val_at(self, i):
        return self.heap[i][0]
    def element_at(self, i):
        return self.heap[i][1]
    def where_is(self, element):
        if not element in self.pos:
            sys.stderr.write("ERROR: accessing an element that is not in the priorityQ\n")
            sys.exit()

        return self.pos[element]
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.element_at(i)] = i
        self.pos[self.element_at(j)] = j

    def heapify_down(self, i):
        if i > self.N:
            return None

        f1 = 2 * i
        f2 = 2 * i + 1

        lowest = i

        if f1 <= self.N and self.val_at(f1) < self.val_at(lowest):
            lowest = f1
        if f2 <= self.N and self.val_at(f2) < self.val_at(lowest):
            lowest = f2

        if lowest != i:
            self.swap(i, lowest)
            self.heapify_down(lowest)

    def heapify_up(self, i):
        if i <= 1:
            return None

        if self.val_at(i) < self.val_at(i // 2):
            self.swap(i, i // 2)
            self.heapify_up(i // 2)

    def decrease_priority(self, element, new_priority):
        i = self.where_is(element)
        if new_priority < self.val_at(i):
            self.heap[i] = (new_priority, self.heap[i][1])
            self.heapify_up(i)

    def extract_min(self):
        """
        Extracts the key with the minimum value in the heap and returns the key.
        """
        if self.N < 1:
            sys.stderr.write("ERROR: You are trying to extract the min from an empty queue\n")
            sys.exit()
        element = self.heap[1][1]
        self.pos.pop(element, None)

        self.heap[1] = self.heap[self.N]
        self.pos[self.heap[1][1]] = 1
        self.N -= 1
        self.heapify_down(1)

        return element

    def insert(self, element, priority):
        if element in self.pos:
            return None

        self.N += 1
        if len(self.heap) <= self.N:
            self.heap.append((priority, element))
        else:
            self.heap[self.N] = (priority, element)
        self.pos[element] = self.N
        self.heapify_up(self.N)

def read_input_file(input_file, part):
    f = open(input_file)
    lines = f.readlines()
    f.close()

    N = int(lines[0].rstrip().split(" ")[0])
    M = int(lines[0].rstrip().split(" ")[1])
    source = int(lines[0].rstrip().split(" ")[2])

    if part != "A":
        dest = ast.literal_eval(lines[0].rstrip().split(" ")[3])

    if part == "A" or part == "D":
        neighbors = [[] for i in range(N)]
        for i in range(1, M + 1):
            s = lines[i].rstrip().split(" ")
            neighbors[int(s[0])].append((int(s[1]), float(s[2])))
    else:
        roads = []
        for i in range(1, M + 1):
            s = lines[i].rstrip().split(" ")
            roads.append( (int(s[0]), int(s[1])) )

    if part == "B" or part == "C":
        coords = [0] * N
        for i in range(M + 1, M + N + 1):
            s = lines[i].rstrip().split(" ")
            coords[i - M - 1] = ( float(s[0]), float(s[1]) )

    if part == "A":
        return (N, neighbors, source)
    if part == "B":
        return (N, coords, roads, source, dest)
    if part == "C":
        return (N, coords, roads, source, dest[0], dest[1])
    if part == "D":
        return (N, neighbors, source, dest)

def run_from_file(input_file, part):
    args = read_input_file(input_file, part)

    if part == "A":
        res = dijkstra(args[0], args[1], args[2])
    if part == "B":
        res = shortest_path(args[0], args[1], args[2], args[3], args[4])
    if part == "C":
        res = closest(args[0], args[1], args[2], args[3], args[4], args[5])
    if part == "D":
        res = least_spillage(args[0], args[1], args[2], args[3])

    return res

if __name__ == '__main__':
    parts = ["A", "B", "C", "D"]

    res = {}

    res[("A", 1)] = ast.literal_eval("[(0, -1), (15.0, 0), (17.0, 1), (31.0, 2), (33.0, 8), (3.0, 0), (19.0, 1), (25.0, 1), (20.0, 1), (25.0, 7)]")
    res[("A", 2)] = ast.literal_eval("[(0, -1), (75.0, 0), (88.0, 1), (156.0, 2), (200.0, 3), (17.0, 0), (95.0, 1), (127.0, 1), (100.0, 1), (137.0, 16), (136.0, 1), (56.0, 5), (101.0, 2), (205.0, 3), (118.0, 6), (124.0, 12), (133.0, 17), (37.0, 0), (190.0, 14), (140.0, 15)]")
    res[("B", 1)] = ast.literal_eval("[0, 1, 2, 19]")
    res[("B", 2)] = ast.literal_eval("[0, 17, 20, 26, 3687, 753, 906, 998, 3726, 3999]")
    res[("C", 1)] = ast.literal_eval("[0, 6, 14]")
    res[("C", 2)] = ast.literal_eval("[0, 1, 35, 56, 103, 113, 140, 147, 197, 218, 285, 310, 312, 346, 373, 384, 434, 438, 454, 557, 572, 573, 690, 728, 795, 985, 1047, 1068, 1110, 1175, 1187, 1273, 1276, 1289, 1336, 1345, 1367, 1430, 1489, 1490, 1558, 1644, 1862, 1866, 1874, 1890, 1949, 1955, 2083, 2084, 2085, 2105, 2497, 2500, 2504, 2511, 2585, 2633, 2656, 2797, 2848, 2910, 2981, 3000, 3015, 3077, 3226, 3243, 3257, 3298, 3391, 3494, 3497, 3772, 3838, 3871, 4043, 4126, 4151, 4327, 4371, 4376, 4453, 4507, 4514, 4532, 4551, 4570, 4604, 4615, 4633, 4667, 4711, 4766, 4789, 4815, 4897, 4948, 4977, 4992]")
    res[("D", 1)] = ast.literal_eval("[0, 17, 7, 2, 19]")
    res[("D", 2)] = ast.literal_eval("[0, 393, 438, 5156, 4638, 2008, 1257, 1093, 3384, 2754, 5999]")


    sys.stderr.write("RUNNING TESTS\n")

    all_good = True

    for part in parts:
        for test in range(1, 3):
            sys.stderr.write("\n")
            sys.stderr.write("Running test " + str(test) + " for part " + part + ":\n")

            input_file = "test_part_" + part + "_" + str(test) + ".in"

            start_time = time.time()
            student_res = run_from_file(input_file, part)
            end_time = time.time()

            sys.stderr.write("Your solution took " + str(end_time - start_time) + " seconds\n")

            if student_res == res[(part, test)]:
                sys.stderr.write("CORRECT ANSWER\n")
            else:
                sys.stderr.write("WRONG ANSWER\n")
                sys.stderr.write("You got : " + str(student_res) + "\n")
                sys.stderr.write("But the answer is : " + str(res[(part, test)]) + "\n")
                all_good = False

    if all_good:
        sys.stderr.write("\nEVERTHING CORRECT\n")
    else:
        sys.stderr.write("\nYOU HAVE INCORRECT ANSWERS\n")

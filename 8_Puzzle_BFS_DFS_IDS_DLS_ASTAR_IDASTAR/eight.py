#Author : Ankit Gupta
#UIN: 621009649
#Date: 09/30/2013
#CSCE 625 AI Assignment 2
#Texas A&M University, College Station

from collections import defaultdict,deque
import math,copy,operator,sys
from Queue import PriorityQueue
from heapq import heapify
import shlex

#*************************************
#   SAMPLE STATES
#*************************************
GOAL_STATE  =  [1, 2, 3,
	        8, 0, 4,
	        7, 6, 5]

EASY_STATE  = [1, 3, 4,
		8, 6, 2,
		7, 0, 5]

MEDIUM_STATE  = [2, 8, 1,	
                0, 4, 3,
                7, 6, 5]

HARD_STATE  = [5, 6, 7,
	        4, 0, 8,
	        3, 2, 1]


#*************************************
#   HEURISTIC : MISPLACE TILES
#*************************************
def h1(state, goal):
	state_list = state.value
	goal_list = goal.value
	displace_count = 0
	# check if number are not same as in goal state and increment count if not
	for i in state_list:
		if state_list[i] != goal_list[i]:
			displace_count = displace_count + 1
	return displace_count



#*************************************
#   HEURISTIC : MANHATTAN DISTANCE
#*************************************
def h2(state, goal):
	state_list = state.value
        diff = 0
	#find out the row and col of each number and corresponding entry in goal state and take difference
        for number in state_list:
            if number == 0:
               continue
            row, col = state.getPosition(number)
            row_goal, col_goal = goal.getPosition(number)
            diff = diff + abs(row_goal - row) + abs(col_goal - col)
        return diff
		 

#*************************************
#	GOAL
#*************************************
def goal(current_list):
	global GOAL_STATE
	#Check for each value in list to equal to other
	if current_list == GOAL_STATE:
		print "Goal Reached !!"
		return True
	else:
		return False
	return False


#*************************************
#	DFS
#*************************************
def dfs(state):
        current_state = state.value
        isFound = (goal(current_state))
	dfs_explored = dict() # to keep the explored nodes values
	stack = deque() # stack to store unvisited ndoes
	maxNode = 1
        if (isFound):
		print "Time Complexity: 1"
		print "Space Complexity:1 "
		print "Maximum Depth: 1"
		print "Number of Nodes Visited: 1"
                return state.getPath()
        else:
                stack.appendleft(state)

        while stack:
                popItem = stack.popleft()
		#print popItem.value, popItem.depth
                isFound = (goal(popItem.value))
                if (isFound):
			print "Time Complexity: ", len(dfs_explored)
			print "Space Complexity: ",maxNode
			print "Maximum Depth: ",popItem.depth
			print "Number of Nodes Visited:", len(dfs_explored) + len(stack)
                        return popItem.getPath()

                dfs_explored[str(popItem.value)] = None
                childList = popItem.getMoves(0) # get all the possible moves and add them in stack for next state
                for child in childList:
			#print "chiild", child
                        if (str(child.value) not in dfs_explored):
                                stack.appendleft(child)
		if maxNode < len(stack):
			maxNode = len(stack)
	return None


#*************************************
#	BFS
#*************************************
def bfs(state):
	bfs_explored = dict()
        if (goal(state.value)):
		print "Time Complexity: 1"
		print "Space Complexity:1 "
		print "Maximum Depth: 1"
		print "Number of Nodes Visited: 1"
                return state.getPath()
	queue = deque()
	queue.append(state)
	maxNode = 1
        while queue:
		popItem = queue.popleft()
		#print popItem.depth, #popItem.depth
        	isFound = (goal(popItem.value))
        	if (isFound):
			print "Time Complexity: ", len(bfs_explored)
			print "Space Complexity: ",maxNode
			print "Maximum Depth: ",popItem.depth
			print "Numbers of Nodes Visited:", len(bfs_explored) + len(queue)			
        	        return popItem.getPath()
		bfs_explored[str(popItem.value)] = None
                childList = popItem.getMoves(0)
                for child in childList:
			if (str(child.value) not in bfs_explored):
	                        queue.append(child)
		if maxNode < len(queue):
			maxNode = len(queue)
	return None


#*************************************
#	DLS
#*************************************
def dls(state, gdepth):
	current_state = state.value
	dls_explored = dict()
        #print "Input for dls: ",current_state
	isFound = (goal(current_state))
	dls_stack = deque()
	maxNode = 1
        if (isFound):
		print "Time Complexity: 1"
		print "Space Complexity:1 "
		print "Maximum Depth: 1"
		print "Number of Nodes Visited: 1"
                return state.getPath()
        else:
		tup = (state, 0)
		dls_stack.appendleft(tup)
	while(dls_stack):
		popItem = dls_stack.popleft()
		#print popItem[0].value, popItem[1]
		dls_explored[(str(popItem[0].value))] = None
		isFound = (goal(popItem[0].value))
        	if (isFound):
			print "Time Complexity: ", len(dls_explored)
			print "Space Complexity: ",maxNode
			print "Maximum Depth: ", popItem[1]
			print "Numbers of Node Visited: ", len(dls_explored) + len(dls_stack)

                	return popItem[0].getPath()
                childList = popItem[0].getMoves(0)
                for child in childList:
			if ((str(child.value)) not in dls_explored):
				t = (child, popItem[1] + 1)
				if (t[1] <= gdepth):
	                        	dls_stack.appendleft(t)
		if maxNode < len(dls_stack):
			maxNode = len(dls_stack)
	return None


#*************************************
#	IDS
#*************************************
def ids(state, gdepth):
	isBreak = False
	rev_depth = 1
	while  rev_depth < gdepth: # iterate for all the depths starting from 1 to gdepth till we find solution 
        	result = dls(start_state, rev_depth)
		if result:
			#print "Found at Depth : ",rev_depth
			return result
                rev_depth = rev_depth + 1
	return None
	

#*************************************
#	GREEDY
#*************************************
def greedy(istate, gstate, f):
	current_state = istate.value
	istate.cost = f(istate, gstate)
	maxNode = 1
	isFound = (goal(current_state))
        if (isFound):
		print "Time Complexity: 1"
		print "Space Complexity:1 "
		print "Maximum Depth: 1"
		print "Number of Nodes Visited: 1"
                return istate.getPath()
               
	unexplored = [] 
	explored   = []
	unexplored.append(istate)
	while unexplored:
		node = unexplored[0]
		unexplored.remove(node)
		#print node.value
		if (goal(node.value)):
			print "Time Complexity: ", len(explored)
			print "Space Complexity:", maxNode
			print "Maximum Depth: ",node.depth
			print "Numbers of Node visited: ",len(explored) + len(unexplored)
                	return node.getPath()
        	      
		explored.append(node.value)
		#print "Explored   : ",explored
		childlist = []
		childList = node.getMoves(0)
		#print "ChildList  : ",childList,"\n\n"
		for child in childList:
			if child.value not in explored and child not in unexplored:
				child.cost = f(child, gstate) # calculate the cost of child till goal state
				unexplored.append(child)
		unexplored.sort(key=operator.attrgetter('cost')) #sort the queue so that next element popup will be minimum f value
		if maxNode < len(unexplored):
			maxNode = len(unexplored)
	return None


#*************************************
#	ASTAR
#*************************************
def astar(istate, gstate, f):
        current_state = istate.value
        istate.cost = f(istate, istate)
	istate.totalcost = f(istate, gstate) + f(istate, istate)
        isFound = (goal(current_state))
        if (isFound):
		print "Time Complexity: 1"
		print "Space Complexity:1 "
		print "Maximum Depth: 1"
		print "Number of Nodes Visited: 1"
                return istate.getPath()

        unexplored = dict() 
	explored   = dict() 
	maxNode = 1
        unexplored[str(istate.value)] = istate
        while unexplored:
		templist = sorted(unexplored.values(), key=lambda x: (x.totalcost), reverse=False) # sort the nodes basis of their total cost
                node = templist[0]								   # and take the fist element for expand
		#print node.value, node.cost, node.direction

                if (goal(node.value)):
			print "Time Complexity: ", len(explored)
			print "Space Complexity:", maxNode
			print "Maximum Depth: ", node.depth
			print "Numbers of Node Visited ", len(explored) + len(unexplored)
                        return node.getPath()
		del unexplored[str(node.value)]
                explored[str(node.value)] = node
                childlist = []
                childList = node.getMoves(0)
                for child in childList:
			#totalcost is childs cost to reach goal + child cost from its parent + parent cost to reach goal
			child.totalcost = f(child, child.parent) + f(child, gstate) + child.parent.cost 
			if ((str(child.value) not in explored) and (str(child.value) not in unexplored)):
				unexplored[str(child.value)] = child
			
			elif (str(child.value) in unexplored):
				existNode = unexplored[str(child.value)]
				if existNode.totalcost > child.totalcost:
					del unexplored[str(existNode.value)]
					unexplored[str(child.value)] = child
		if maxNode < len(unexplored):
			maxNode = len(unexplored)
			
        return None

#*************************************
#	IDASTAR
#*************************************
maxSpace = 0 # to keep track of the maximum amount of space used for any iteration
def idastar(istate, gstate, f):
	current_state = istate.value
	istate.cost = f(istate, gstate)
	istate.totalcost = f(istate, gstate) + f(istate, istate)
    	isFound = (goal(current_state))
    	infinity = sys.maxint # take the maximum value as maximum value of system infinity
        fvalue = istate.totalcost
    	if (isFound):
		print "Time Complexity: 1"
		print "Space Complexity:1 "
		print "Maximum Depth: 1"
		print "Number of Nodes Visited: 1"
        	return fvalue,state.getPath(), 1
        while fvalue < infinity:
		fvalue,result = helping_idastar(istate, gstate, f, fvalue) # returns the new fvalue and result
		#if result is not none then result is found and exit else if None continue with new fvalue
		if result:
			return result


#*************************************
#	HELPING_IDASTAR
#*************************************
def helping_idastar(state, gstate, f, fvalue):
	global maxSpace
        current_state = state.value
        isFound = (goal(current_state))
	dfs_explored = dict()
	stack = deque()
	heap = []
	maxNode = 1
        if (isFound):
		print "Time Complexity: 1"
		print "Space Complexity:1 "
		print "Maximum Depth: 1"
		print "Number of Nodes Visited: 1"
                return state.getPath()
        else:
                stack.appendleft(state)

        while stack:
                popItem = stack.popleft()
		#print popItem.value, popItem.depth
                isFound = (goal(popItem.value))
		if maxSpace < maxNode:  #if maximum amount of space used so far in previous iteration is less than current, update the maximum space used.
			maxSpace = maxNode
                if (isFound):
			print "Time Complexity: ", len(dfs_explored)
			print "Space Complexity:", maxSpace
			print "Maximim Depth :", popItem.depth
			print "Numbers of Node Visited: ", len(dfs_explored) + len(stack)
                        return fvalue, popItem.getPath()
	
                dfs_explored[str(popItem.value)] = None
                childList = popItem.getMoves(0)
                for child in childList:
			#totalcost is childs cost to reach goal + child cost from its parent + parent cost to reach goal
			child.totalcost = f(child, gstate) +  f(child, child.parent)  + child.parent.cost
			if child.totalcost > fvalue:          # Donot add child with fvalue greater to the stack and append them to separate
				heap.append(child.totalcost)  # heap to find out the minimum fvalue for next iteration
				continue
			else:
                        	if (str(child.value) not in dfs_explored):
                                	stack.appendleft(child)
		if maxNode < len(stack): 
			maxNode = len(stack)
	
	# Sort the Heap and return the lowest fvalue from it
	heapify(heap)
	if heap:
		return heap[0], None


#*************************************
#	STATE OBJECT CLASS
#*************************************
class State (object):
	def __init__(self,value):
		self.value = value    # Contains the List of Numbers
		self.parent = None    # Contains Object from Which it Derived
		self.direction = None # Direction from its Parent which it get Derived
		self.cost = 0         # Cost from Object to Goal
		self.totalcost = 0    # Cost from Object to Goal + Object to Parent + Parent to Root
		self.maxRows = 3      # max rows in 8 Puzzle
		self.maxCols = 3      # max cols in 8 Puzzle
		self.depth = 0	      # depth in graph object is present
		
        # return index and columber of given number from caling state
	def getPosition(self, number): 
		row = (self.value).index(number) / self.maxRows 
		col = (self.value).index(number) % self.maxCols
		return row,col

	# return path from original state to goal state
	def getPath(self):
		cparent = self
		pathlist = []
		while cparent.direction:
			pathlist.append(cparent.direction)
			cparent = cparent.parent
		return pathlist
		
	
	#getMoves call these functions. They return object with their parents, their direction from parent, cost,
	#depth updated and return to calling object for expansion

	# return new State Object with Left moved from calling object
	def moveLeft(self, number,valuelist):
		#print "In moveLeft: ", valuelist
		c_row,c_col = self.getPosition(number)
		if c_col != 0:
			new_state = State(valuelist) 
			old_index = c_row * self.maxRows + c_col
			new_index = c_row * self.maxRows + (c_col - 1)
			new_value = self.value[new_index]
			old_value = self.value[old_index]
			new_state.value[new_index] = old_value
			new_state.value[old_index] = new_value
			new_state.parent = self
			new_state.direction = "Left"
			new_state.depth = self.depth + 1
			new_state.cost  = self.cost + 1
			return new_state
			
			
	# return new State Object with Right moved from calling object
	def moveRight(self, number,valuelist):
		#print "In moveRight: ",self.value
		c_row,c_col = self.getPosition(number)
		if c_col != (self.maxCols - 1):
			new_state = State(valuelist) 
			old_index = c_row * self.maxRows + c_col
			old_index = c_row * self.maxRows + c_col
			new_index = c_row * self.maxRows + (c_col + 1)
			new_value = self.value[new_index]
			old_value = self.value[old_index]
			new_state.value[new_index] = old_value
			new_state.value[old_index] = new_value
			new_state.parent = self
			new_state.direction = "Right"
			new_state.depth = self.depth + 1
			new_state.cost  = self.cost + 1
			return new_state
			
	
			
	# return new State Object with Up moved from calling object
	def moveUp(self, number,valuelist):
		#print "In moveUp: ",self.value
		c_row,c_col = self.getPosition(number)
		if c_row != 0:
			new_state = State(valuelist)
			old_index = c_row * self.maxRows + c_col
			new_index = (c_row - 1) * self.maxRows + c_col
			new_value = self.value[new_index]
			old_value = self.value[old_index]
			new_state.value[new_index] = old_value
			new_state.value[old_index] = new_value
			new_state.parent = self
			new_state.direction = "Up"
			new_state.depth = self.depth + 1
			new_state.cost  = self.cost + 1
			return new_state
			
	# return new State Object with Down moved from calling object
	def moveDown(self, number,valuelist):
		#print "In moveDown: ",self.value
		c_row,c_col = self.getPosition(number)
		if c_row != (self.maxRows - 1):
			new_state = State(valuelist) 
			old_index = c_row * self.maxRows + c_col
			new_index = (c_row + 1) * self.maxRows + c_col
			new_value = self.value[new_index]
			old_value = self.value[old_index]
			new_state.value[new_index] = old_value
			new_state.value[old_index] = new_value
			new_state.parent = self
			new_state.direction = "Down"
			new_state.depth = self.depth + 1
			new_state.cost  = self.cost + 1
			return new_state
			
	# return possible moves Object for calling state for number
	def getMoves(self, number):
		parentDir = self.direction
		moveList = []
		returnList = []
		leftlist =  self.value[:]
		rightlist = self.value[:]
		uplist = self.value[:]
		downlist = self.value[:]
		moveList.append(self.moveLeft(number,leftlist))
		moveList.append(self.moveUp(number,rightlist))
		moveList.append(self.moveRight(number,uplist))
		moveList.append(self.moveDown(number,downlist))
		for item in moveList:
			if item:
				returnList.append(item)
		return returnList




#*************************************
#	MAIN FUNCTION
#*************************************
if __name__ == "__main__":

	while(1):
		print "\n\nEnter Algorithm: ",
		algo = raw_input().lower()
		print "\nDifficulty Level: Easy, Medium, Hard or different for own input: ",
		level = raw_input().lower()
	
		if level.lower() == "easy":
			start = EASY_STATE
		elif level.lower() == 'medium':
			start = MEDIUM_STATE
		elif level.lower() == 'hard':
			start = HARD_STATE
		else:
			start = list(eval(','.join(shlex.split(level))))
			if len(start) < 9:
				print "Error in Input,All the numbers are not given. Try Again"
				continue

		start_state = State(start)   #object with input given else with level type
		goal_state = State(GOAL_STATE) # goal object to be used for comparison and finding cost
	
		if algo.lower() == 'dfs':
			result = dfs(start_state)

		elif algo.lower() == 'bfs':
			result = bfs(start_state)

		elif algo.lower() == 'dls':
			print "\nEnter Depth :",
			depth =  int(raw_input())
			result = dls(start_state, depth)

		elif algo.lower() == 'ids':
			print "\nEnter Depth :",
			depth =  int(raw_input())
			result = ids(start_state, depth)
	
		elif algo.lower() == 'greedy':
			print "\nEnter Heuristic h1(misplaced tiles) or h2(Manhattan distance): ",
			func = raw_input()
			if func == 'h1':
				result = greedy(start_state, goal_state,h1)
			else:	
				result = greedy(start_state, goal_state,h2)

		elif algo.lower() == 'astar':
			print "\nEnter Heuristic h1(misplaced tiles) or h2(Manhattan distance): ",
			func = raw_input()
			if func == 'h1':
				result = astar(start_state, goal_state,h1)
			else:	
				result = astar(start_state, goal_state,h2)

		elif algo.lower() == 'idastar':
			print "Enter Heuristic h1(misplaced tiles) or h2(Manhattan distance): ",
			func = raw_input()
			if func == 'h1':
				result = idastar(start_state, goal_state,h1)
			else:	
				result = idastar(start_state, goal_state,h2)
		else:
			print "Unknown Algorithm. Try Again"
			continue
		if result:
			count  = 0
			for item in result:
				if count > 200:
					print "Still Going on ........................"
					break;
				print "->",item,
				count =  count + 1
		else:
			print "No Result found :("
#Author : Ankit Gupta
#UIN: 621009649
#Date: 09/30/2013
#CSCE 625 AI Assignment 2
#Texas A&M University, College Station

													Readme
									CSEC 625 Artifical Intelligence: Program 2



How to Run:
-------------
 
>> python eight.py

It will prompt for the Algorithm you want to run e.g. dfs, bfs, dls, ids, greedy, astar and idastar

Then it will ask for difficulty level: hard, easy or medium or you can enter your own input: e.g hard, easy, medium , (1 2 3 8 4 0 7 6 5)

For IDS, DLS: it will ask for Depth you want your Recursion. e.g. 100, 200

For Greedy, Astar, Idastar it will ask for Heuristic function input: h1 for misplaced tiles or h2 for Manhattan distance. e.g h1, h2

Each run will give you the time complexity, space complexity, maximum depth of recursion it reached inside tree and the number of nodes it visited

To end the execution:
Ctrl + C

File Results.txt contains all the values of time, space complexity and number of nodes visited and depth of recursion for each case for easy, medium and hard
and for h1(mispalace tiles) and h2(manhattan distance) heuristic.

=================================================================================
For each method, comment on the strengths and weaknesses?

Comparisons between different Search Algorithms
--------------------------------------------------------------------------------

DFS:

Strength:
Space is better than BFS for huge graph

Weakness:
may be incomplete
Bad for shallow goal nodes
--------------------------------------------------------------------------------

BFS

Strength:
Complete, it will find the solution

Weakness:
space and time both are issue

--------------------------------------------------------------------------------
DLS

Strength:
Space and time complexity will be better than DFS for shallow nodes
Solution is good if given in limited depth

Weakness:
Not Optimal Solution
Complete only when given depth contains the solution

--------------------------------------------------------------------------------
IDS

Strength:
Optimal Solution
Complete Solution
Good for Searching of Goal when possibilities are huge and depth is not known

Weakness:
Revisits already explored nodes at successive depth
Time complexity is exponential

--------------------------------------------------------------------------------
Greedy:

Strength:
Less time
Single path towards goal Only
Space is same as time complexity.

Weakness:
Incomplete Solution
Not Optimal Solution

--------------------------------------------------------------------------------
Astar

Strength:
Complete Solution
Optimal Solution


Weakness:
Heuristic function should be admissable and should not overestimate the acutal cost
Space Complexity can be exponential if heuristic is not good
--------------------------------------------------------------------------------

Idastar

Strength:
Complete Solution
Optimal Solution
Space required is better than Astar 

Weakness:
Heuristic function should be admissable and should not overestimate the acutal cost

=========================================================================================================================================

Q .Some search methods may fail to produce an answer. Analyze why it failed and report your ﬁndings ?

For Astar: hard Example failed to produce result for heuristic h1 (misplace tiles) and it continuously running for like more than 10 minutes

Issue:  Astar algorithm is keeping all the generated nodes in memory and it explores all of them and thus after some time it either run out of space and
	if you have enough memory it will keep running until it find a solution.
	H1 heuristic (mispace tile) is overestimating the size of problem by just calculating the misplaced tiles from its position without matter they are close
	to their position in goal state. H2 gives result for this problem as it correctly as it doesnt overestimate the cost and actually calculate the cost to
	reach the particular value in problem to its positon in goal state.
	Thus sometime H1 failed to produce result for Astar hard example while H2 does.

=========================================================================================================================================

Q. Test and compare the effect of different heuristic functions

Clearly heuristic given by h2 is much better in finding solution as explained above and can be seen in results.


Greedy(Hard)
Time and Space complexity for greedy for h1 is 1924 and 1295 respectively whereas,
Time and Space complexity for greedy for h2 is  292 and  200 respectively.

Astar(Hard)
Time and Space complexity for Astar for h1 is unknown and gives no result in time limit
Time and Space complexity for Astar for h2 is  2166 and  1171 respectively.

Idastar(Hard)
Time and Space complexity for Idastar for h1 is 4172 and   22 respectively whereas,
Time and Space complexity for Idastar for h2 is  190 and   22 respectively.
Time Complexity is much better for h1 than h2 in all the cases and thus a better heuristic function to search for goal
===========================================================================
Greedy(Medium)
Time and Space complexity for greedy for h1 is 164 and 110 respectively whereas,
Time and Space complexity for greedy for h2 is  9 and  9 respectively.

Astar(Medium)
Time and Space complexity for Astar for h1 is 33 and 31 respectively whereas,
Time and Space complexity for Astar for h2 is 15 and 13 respectively.

Idastar(Medium)
Time and Space complexity for Idastar for h1 is 33 and 15 respectively whereas,
Time and Space complexity for Idastar for h2 is  15 and 15 respectively.
Time Complexity is much better for h1 than h2 in all the cases and thus a better heuristic function to search for goal
===========================================================================

Greedy(Easy)
Time and Space complexity for greedy for h1 is 6 and 8 respectively whereas,
Time and Space complexity for greedy for h2 is  5 and  7 respectively.

Astar(Easy)
Time and Space complexity for Astar for h1 is 6 and 8 respectively whereas,
Time and Space complexity for Astar for h2 is 5 and 7 respectively.

Idastar(Easy)
Time and Space complexity for Idastar for h1 is 5 and 15 respectively whereas,
Time and Space complexity for Idastar for h2 is 5 and 15 respectively.
Time Complexity is much better for h1 than h2 in all the cases and thus a better heuristic function to search for goal
-----------------------------------------------------------------------------------------------------------------------------

From the above results it can also be referenced for the idstar to be more space efficient than astar as it takes minimum space keeping the almost same time or less for solutions.
=============================================================================================================================






















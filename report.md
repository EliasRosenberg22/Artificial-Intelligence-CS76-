# PA1: Chickens and Foxes
Elias Rosenberg
CS76
21F
Professor Quattrini Li

# Introduction: 
In this lab we were tasked with solving the chicken and fox problem. Three foxes and three chickens are on one side of a river with one boat. The boat can hold up to two animals, and there cannot be more foxes on either side of the river at any point or they will eat the chickens. This problem can be solved with graph search algorithms (BFS, DFS, and IDS in this case) where each node of the graph is a representation of the next legal state in an order of actions to get all the animals to the other side of the river. The relationship between the chickens, foxes, and boat was represented by a triple (number of chickens, number of foxes, boat present/not) with the left side of the river being the reference position for all other states. 
# 
# Description: 
Each algorithm functions in a unique way, differing in how they choose the next node to propogate to, and how they store their search trees. Breadth-First Search keeps track of visited nodes in a set, and has a queue to hold the frontier nodes that need to be visited. When a new node is instantiated from either the start state or the child of another node further down the tree, it is popped from the queue. This means that the BFS algorithm checks every path from left to right, and always arrives at the optimal solution because all the nodes are visited. BFS returns a path with the help of a backchaining() which recursively goes from the current node to that node's parent, adding states to the list until the start state is reached. 

Depth-First Search utilizes a stack instead of a queue to get the next node to visit, and doesn't keep track of all the nodes visited. The next node to visit is removed from the top of the stack, meaning DFS will travel down the path it is on before checking all the nodes on a given depth. This DFS implementation is recursive, meaning it will run paths as far down as they go into the tree until it finds any solution (often not the optimal one). Since there is not a set like in BFS to check for loops, I wrote a helper function pathchecking() to see whether or not the current path would end up in a loop. 

Increment-Depth Search is the same as DFS, except it rebuilds the search tree at every depth. For instance, when the depth_limit is 0, it checks all the nodes at depth 0 in the tree for a goal. If no node is found it increases the depth limit by one, and then checks all the nodes at that limit. Since DFS takes depth_limit as a paremeter, IDS was implemented with a for-loop that checks every depth until the depth limit is reached, recursively increasing the depth by one at each failed layer until a goal state node was found. 

Implementing these algorithms did not require much creativity in terms of 'design decisions.' Apart from writing the helper methods for BFS and DFS, the pseudocode in the class slides was closely followed. FoxProblem.py, where the legality of states was determined, required more creativity. I am proud of the get_next() function I wrote to get the possible child states of any give node. I knew what the calculations were, but it was tricky to create the right numerical values in the (Chicken, Fox, Boat) setup because the calculations changed depending on which side of the river you are on. To get around this, I first checked which side of the river the boat was on, and then changed a variable called 'stateSign' to see what the difference value should be multiplied by to get the correct output. This way, I didn't have to write a seperate set of actions for each side of the river. The instructions were very clear about what states were legal and which ones weren't. All those caveats are written in is_legal(). I did spend about a day writing down possible paths with pen and paper to see what my options were, until I realized that I was wasting my time, and that that was the whole point of using tree search! 

# Evaluation: 

The implemented algorithms work as well as expected, with BFS being the most optimal, followed by IDS, and then DFS. I can tell that BFS worked well because the number of nodes explored is always just above the size of the path. The path returned also matched what I had written down manually. DFS had to explore more nodes. The more nodes explored, the further down a path the algorithm had to go to find a solution. DFS was the worst of the three, exploring many of the same nodes multiple times. IDS was alright, having slightly lower numbers to DFS in terms of explored nodes (I didn't keep track of every single node explored in every rebuilt tree). It had a longer path than BFS becuase it returned the first path found, not the best one. 

The only problem I have had with the code is a very specific case that only happens when you run multiple tests in foxes.py. Because my backchaining method is recursive, I couldn't hold the path of nodes within the method, so I instantiated it outside of BFS. Because of this, when you run multiple tests in foxes.py, whatever nodes are left in path (approx line 19, uninformed_search.py) from a previous search are added to the SearchSolution's path. This returns a path that is wrong, and I am still trying to figure out a workaround. If each search problem is ran seperately, they all yield the correct results, which tells me my actual implementation of the algorithms is fine. I'm skeptical that this hiccup would have even been caught by whoever is grading the lab, but I want to be transparent. (I fixed it! Don't have enough time to edit this paragraph).

BFS runtime: O(b^d) where 'b' is the branching factor and 'd' is the depth

DFS runtime: O(b^m) where 'm' is the max depth

IDS runtime: O(b^l) where 'l' is the incremented depth

# Responses:
Upper bound of possible states is 32. 

I got this number by multiplying the number of possible values in each slot of the (chickens, foxes, boat) representation. Since there could be 3 chickens, 2, 1, or none, there are 4 options for the number of chickens. There are also 4 options for the number of foxes. The boat only has two: starting side or opposite side. 4 * 4 * 2 = 32 possible states. 

Image of first two layers with legal/illegal actions

![](https://i.imgur.com/Uz9AKya.png)


Discussion points
- In theory pathchecking DFS should save much more memory than BFS because it doesn't visit all the nodes in the search tree. In this case, however, I don't think the memory we are saving is that big of a deal, especially when the returned paths are less optimal. The memory saved is not 'significant' for this problem in particular. If there were more nodes, thousands or tens of thousands, it would make a big difference in space efficiency. A situation where path-checking DFS would have a longer runtime would be where the solution on the tree is shallow, but is on the far right of the tree. DFS would go through all the deep, leftward paths first, but BFS would find the shallow solution immediately because it checks the nodes at every depth. 
![](https://i.imgur.com/P80TeQk.png)

- I imagine memoizing in DFS saves much more memory than path-checking does because the algorithm won't dive down a deep path on the tree if it has seen one of its nodes before. DFS with pathchecking will check paths that are nearly the same multiple times because it has no way of keeping track of previously-visited nodes, which wastes time. Memoizing seems good for DFS, especially on larger trees where going down a huge path can waste a ton of time. Also, storing a set of states does not take up the same amount of space as actually storing a search tree. I know that was not the case for this lab, but it could be for other coding problems. 
- I would prefer to use BFS, as long as the memory is there (which it likely is in the real world) for smaller graphs, and memoizing IDS for larger ones. I don't understand how a memoizing DFS in conjunction with IDS is much different than BFS. What good is memoizing if you rebuild the tree at every new depth? That would just be BFS with extra steps, with the path going to the next unexplored node at that depth checking from left to right. You would save space, because the only nodes left that are stored would be the optimal path, but it sounds like it would take much longer. Whether or not I would want to use DFS is entirely contextual. Do I need ANY path or THE BEST path? 

Lossy Chickens and Foxes: 
The state for this problem could be represented the same (number of chickens, number of foxes, boat present/not), but we can change the legality of certain child states. If the state is (2, 2, 0) and either a fox or chicken can return, a possible legal state could now be (2, 3, 1). We would need a chicken counter that can't go down below E for the solution to be valid. We would also need to go into the original rules for testing legal states and allow for the loss of E chickens. Upper bound for states could now be 4+E * 4 * 2 = 32 + 8E where E is the number of chickens that can be lost. 

# Artificial-Intelligence-CS76-
Repo for storing all my work for Artificial Intelligence (CS76).
This class covered a wide bredth (no pun intended) of algorithms used to solve common problems under the banner of "Artificial Intelligence." I will label all the projects in the Repo here, describing what was implemented and learned for each project. Some assignments were strictly conceptual, or written tests, so the numbering is not consistent. 

##Lab 1: Chickens and Foxes
In this lab we implemented specialized BFS, DFS, and Iterative Depth Search (IDS) algorithms to navigate a path of steps needed to solve the classic Chicken and Foxes problem. 

""Three chickens and three foxes come to the bank of a river as shown in the figure above. They would like to cross to the other side of the river. However, there is one boat. The boat can carry up to two animals at one time, but doesn't row itself -- at least one animal must be in the boat for the boat to move. If at any time there are more foxes than chickens on either side of the river, then those chickens get eaten.

Constants are not part of the state.  The size of the boat (it holds two), or the total number of chickens and foxes (three each), are not part of the state, since these are constants that don't change.  They are part of the rules of the game.  That doesn't mean that the rules can't be changed -- but they are changed in the problem definition, rather than in state elements.     

Minimal state representations are often best.  If one fox, one chicken, and one boat are on the starting bank, where are the other chickens and foxes?  Wait wait, don't tell me!  They had better be on the other bank of the river, assuming nothing...untoward...has happened.  Since I can compute where the others are, I don't have to keep track of their locations as part of the state.  I would describe this state using the tuple (1, 1, 1):  one chicken, one fox, and one boat, on the starting side.  If I need to know how many of each are on the other side, I can use subtraction.  Using this representation, the initial state is (3, 3, 1).  

Actions link states.  Given a state of (3, 3, 1), the action of moving one chicken, one fox, and one boat to the other side changes the state to (2, 2, 0).  Given a particular state, we'll need to consider which actions are legal:  actions that can be carried out from that state, and don't lead to a state where someone is eaten.    

States are nodes in a graph; actions are edges.  There is an underlying graph of all possible legal states, and there are edges between them.  The algorithms you write will implicitly search this graph.  However, you will not generate the graph ahead of time, but rather write methods that, given a state, generate legal actions and possible successor states, based on the current state and the rules of the game.""

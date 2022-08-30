#Author: Elias Rosenberg
#Date: September 23, 2021
#Purpose: Lays out the functions needed to see if a certain graph state in the chicken fox problem is legal.

class FoxProblem:
    def __init__(self, start_state): #three chickens, three foxes, boat is on the left. When index(2) = 0 boat is on the right of the river, when it is 1 the boat is on the left
        self.start_state = start_state
        self.goal_state = (0, 0, 0)

        self.successor_list = [] #list to hold possible sucessors

        self.chicken_number = start_state[0] #total number of chickens
        self.fox_number = start_state[1] #total number of foxes
        self.boat_size = start_state[2] #boat size

        self.signSignal = None

    # get successor states for the given state



    def calc_other_side(self, state): #calculates the number of animals on the other side of the river
        opposite_side = (abs(state[0] - self.chicken_number), abs(state[1] - self.fox_number), abs(state[2] - 1))
        return opposite_side

    def get_successors(self, state): #returns a list of possible sucessor states from the given state
        successors = []
        for n_state in self.get_next(state): #for the list of possible successor states from this state
            if self.is_legal(n_state) and n_state != self.start_state: #if the state is legal
                successors.append(n_state) #add it to the list of next states
        return successors #return the list

    def is_legal(self, state):
        left = state
        right = self.calc_other_side(state)

        leftChickens = left[0]
        leftFoxes = left[1]
        leftBoat = left[2]

        rightChickens = right[0]
        rightFoxes = right[1]
        rightBoat = right[2]

        if leftChickens < 0 or leftChickens > self.start_state[0]: #checks to see if there are the proper amount of animals on the left side
            return False
        if leftFoxes < 0 or leftFoxes > self.start_state[1]:
            return False

        if rightChickens < 0 or rightChickens > self.start_state[0]: #proper amount of animagles on the right side
            return False
        if rightFoxes < 0 or rightFoxes > self.start_state[1]:
            return False

        if leftFoxes > leftChickens and leftChickens != 0: #if there are more foxes than chickens AND there are still chickens on this side
            return False
        if rightFoxes > rightChickens and rightChickens != 0: #same thing, but for the right side
            return False
        if rightFoxes + rightChickens < 1 and state != self.start_state: #if there are no animals left to row on the right side, the path fails
            return False
        return True

    def get_next(self, state): #returns a list of possible legal actions from this state to the next

        if state[2] == 1:
            self.signSignal = 1
        if state[2] == 0:
            self.signSignal = -1

        one_chicken_one_fox = (state[0] - 1*self.signSignal, state[1] - 1*self.signSignal, state[2]-1*self.signSignal)
        one_chicken = (state[0] - 1*self.signSignal, state[1], state[2]-1*self.signSignal)
        one_fox = (state[0], state[1] - 1*self.signSignal, state[2]-1*self.signSignal)
        two_chickens = (state[0] - 2*self.signSignal, state[1], state[2]-1*self.signSignal)
        two_foxes = (state[0], state[1] - 2*self.signSignal, state[2]-1*self.signSignal)

        nextStates = [one_chicken_one_fox, one_chicken, one_fox, two_chickens, two_foxes]
        return nextStates

    def goal_test(self, state): #goal test method
        if state == self.goal_state:
            return ("goal state has been reached!")

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string

if __name__ == "__main__":
    test_cp = FoxProblem((3, 3, 1))
    #print(test_cp.get_successors((5, 5, 1)))
    #print(test_cp)
    #print(test_cp.calc_other_side((3, 3, 1)))
    print(test_cp.get_successors((3, 0, 0)))
    #print(test_cp.is_legal((3,3,1)))

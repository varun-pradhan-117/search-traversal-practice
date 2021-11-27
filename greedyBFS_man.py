from copy import deepcopy
class Board:
    def __init__(self,startstate,goalstate):
        self.currState=startstate
        self.goalstate=goalstate
        self.bestHeur=100
        self.goals=dict((j,(x, y)) for x, i in enumerate(self.goalstate) for y, j in enumerate(i))

    @staticmethod
    def index_2d(l, v):
        for i, x in enumerate(l):
            if v in x:
                return (i, x.index(v))

    def calcHeuristic(self,newState):
        score=0
        for i in range(0,3):
            for j in range(0,3):
                if (val:=newState[i][j])!=0:
                    score+=abs(i-self.goals[val][0])+abs(j-self.goals[val][1])
        return score

    def up(self):
        r0,c0=Board.index_2d(self.currState,0)
        newState=deepcopy(self.currState)
        if r0==0:
            return None
        else:
            newState[r0][c0],newState[r0-1][c0]=newState[r0-1][c0],newState[r0][c0]
        return newState

    def down(self):
        r0,c0=Board.index_2d(self.currState,0)
        newState=deepcopy(self.currState)
        if r0==2:
            return None
        else:
            newState[r0][c0],newState[r0+1][c0]=newState[r0+1][c0],newState[r0][c0]
        return newState
    
    def left(self):
        r0,c0=Board.index_2d(self.currState,0)
        newState=deepcopy(self.currState)

        if c0==0:
            return None
        else:
            newState[r0][c0],newState[r0][c0-1]=newState[r0][c0-1],newState[r0][c0]
        return newState
    
    def right(self):
        r0,c0=Board.index_2d(self.currState,0)
        newState=deepcopy(self.currState)
        if c0==2:
            return None
        else:
            newState[r0][c0],newState[r0][c0+1]=newState[r0][c0+1],newState[r0][c0]
        return newState

    def greedyBFS(self):
        stack=[self.currState]
        path=[]
        order=['up','down','left','right']
        ct=0
        while self.bestHeur!=0:
            removeDupe=[]
            for i in order:
                newState=eval("self."+i+"()")
                if newState!=None:     
                    stack.append(eval("self."+i+"()"))
                    if (newHeur:=self.calcHeuristic(newState))<self.bestHeur:
                        self.bestHeur=newHeur
            
            removeDupe=[i for i in stack if i not in removeDupe]
            stack=deepcopy(removeDupe)
            print("Possible states:")
            self.printStates(stack)
            stack=[i for i in stack if self.calcHeuristic(i)<=self.bestHeur]
            print("Superior states:")
            self.printStates(stack)
            print("Current best heuristic value")
            print(self.bestHeur)
            result=self.currState=stack.pop()
            print('-'*30)

    def printStates(self,stack):
        for i in range(0,3):
            for j in range(0,len(stack)):
                print("|",end=" ")
                for k in range(0,3):
                    print(stack[j][i][k], end=" ")
                print("|",end="\t")
            print()

if __name__=='__main__':
    board=Board([[2,8,3],
                [1,6,4],
                [7,0,5]],
                [[1,2,3],
                [8,0,4],
                [7,6,5]])
    print("Initial Sate:")
    board.printStates([board.currState])
    print("Goal State:")
    board.printStates([board.goalstate])
    print("\nPerform greedy BFS:")
    print("-"*20)
    board.greedyBFS()
    print("Final state after Greedy BFS:")
    board.printStates([board.currState])
    print("Final heuristic value=",board.bestHeur,sep="")
            

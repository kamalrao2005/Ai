import heapq
import copy

def read_puzzle():
    puzzle=[]
    for i in range(3):
        puzzle.append(list(map(int,input(f"Row {i+1}: ").split())))
    return puzzle

def h1_misplaced_tiles(state,goal):
    misplaced=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0 and state[i][j]!=goal[i][j]:
                misplaced+=1
    return misplaced

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j

def generate_next_states(state):
    x,y=find_blank(state)
    moves=[]
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new_state=copy.deepcopy(state)
            new_state[x][y],new_state[nx][ny]=new_state[nx][ny],new_state[x][y]
            moves.append(new_state)
    return moves

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def a_star(initial,goal):
    pq=[]
    visited=set()
    heapq.heappush(pq,(h1_misplaced_tiles(initial,goal),0,initial,[]))
    while pq:
        f,g,current,path=heapq.heappop(pq)
        if current==goal:
            return path+[current]
        visited.add(state_to_tuple(current))
        for next_state in generate_next_states(current):
            if state_to_tuple(next_state) not in visited:
                new_g=g+1
                new_h=h1_misplaced_tiles(next_state,goal)
                heapq.heappush(pq,(new_g+new_h,new_g,next_state,path+[current]))
    return None

def print_state(state):
    for row in state:
        print(row)
    print()

def main():
    print("Enter Initial State:")
    initial=read_puzzle()
    print("\nEnter Goal State:")
    goal=read_puzzle()
    solution=a_star(initial,goal)
    if solution:
        print("\nSolution Steps:\n")
        for step,state in enumerate(solution):
            print(f"Step {step} | h1 = {h1_misplaced_tiles(state,goal)}")
            print_state(state)
        print(f"Total number of moves = {len(solution)-1}")
    else:
        print("No solution found!")

if __name__=="__main__":
    main()

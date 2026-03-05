from collections import deque

class State:
    def __init__(self, m, c, b, path=[]):
        self.m = m  
        self.c = c  
        self.b = b  
        self.path = path + [(m, c, b)]

    def is_valid(self):
        
        if self.m < 0 or self.m > 3 or self.c < 0 or self.c > 3:
            return False
        
        if self.m > 0 and self.m < self.c:
            return False
        
        if (3 - self.m) > 0 and (3 - self.m) < (3 - self.c):
            return False
        return True

    def is_goal(self):
        return self.m == 0 and self.c == 0 and self.b == 0

    def __repr__(self):
        return f"M:{self.m} C:{self.c} B:{'Left' if self.b == 1 else 'Right'}"

def solve():
    initial_state = State(3, 3, 1)
    queue = deque([initial_state])
    visited = set([(3, 3, 1)])

    
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        current = queue.popleft()

        if current.is_goal():
            return current.path

        for dm, dc in moves:
            if current.b == 1: 
                new_state = State(current.m - dm, current.c - dc, 0, current.path)
            else: 
                new_state = State(current.m + dm, current.c + dc, 1, current.path)

            state_tuple = (new_state.m, new_state.c, new_state.b)
            if new_state.is_valid() and state_tuple not in visited:
                visited.add(state_tuple)
                queue.append(new_state)

    return None


solution = solve()
if solution:
    print("Success! Path to solution:")
    for step in solution:
        m, c, b = step
        print(f"Left Bank -> Missionaries: {m}, Cannibals: {c}, Boat: {'Left' if b==1 else 'Right'}")
else:
    print("No solution found.")

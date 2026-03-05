from collections import deque

capacities = (8, 5, 3)
start = (8, 0, 0)

def get_next_states(state):
    x, y, z = state
    amounts = [x, y, z]
    next_states = []

    for i in range(3):
        for j in range(3):
            if i != j:
                temp = amounts.copy()
                pour = min(temp[i], capacities[j] - temp[j])
                if pour > 0:
                    temp[i] -= pour
                    temp[j] += pour
                    next_states.append(tuple(temp))
    return next_states


def bfs():
    visited = set()
    queue = deque()
    parent = {}

    queue.append(start)

    while queue:
        state = queue.popleft()

        if state in visited:
            continue

        print("Exploring:", state)   # Debug line

        visited.add(state)

        if state[1] == 4:
            print("Goal Reached:", state)
            return

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append(next_state)
                parent[next_state] = state

    print("No solution found")


bfs()

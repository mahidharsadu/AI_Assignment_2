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


def dls(limit):

    def recursive(state, depth, visited):

        if depth > limit:   # 🔴 IMPORTANT
            return False

        if state in visited:
            return False

        print("Exploring:", state, "Depth:", depth)

        visited.add(state)

        if state[1] == 4:
            print("Goal Reached:", state)
            return True

        for next_state in get_next_states(state):
            if recursive(next_state, depth + 1, visited):
                return True

        return False

    visited = set()
    if not recursive(start, 0, visited):
        print("No solution within depth limit")


dls(4)   # try 6, 7, 8 etc

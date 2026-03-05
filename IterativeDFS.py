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


def dls(state, limit, visited):

    if limit < 0:
        return False

    if state in visited:
        return False

    visited.add(state)

    if state[1] == 4:
        print("Goal Reached:", state)
        return True

    for next_state in get_next_states(state):
        if dls(next_state, limit - 1, visited):
            return True

    return False


def iddfs(max_depth):
    for depth in range(max_depth):
        visited = set()
        print("Trying depth:", depth)
        if dls(start, depth, visited):
            return


iddfs(15)

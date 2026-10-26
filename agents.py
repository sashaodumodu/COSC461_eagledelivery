from collections import deque
import heapq
from itertools import count


class SearchResult:
    def __init__(self, path, expanded):
        self.path = path
        self.expanded = expanded


def reconstruct_path(parents, goal):
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parents[state]
    path.reverse()
    return path


def bfs(campus, start, goal):
    frontier = deque([start])
    parents = {start: None}
    expanded = 0
    while frontier:
        state = frontier.popleft()
        if state == goal:
            return SearchResult(reconstruct_path(parents, goal), expanded)
        expanded += 1
        for action, successor in campus.neighbors(state):
            if successor not in parents:
                parents[successor] = state
                frontier.append(successor)
    return SearchResult(None, expanded)


def manhattan(state, goal):
    # """TODO 1: Return Manhattan distance between two (row, column) tuples."""
    # Add the absolute row difference and the absolute column difference.
    # raise NotImplementedError("Complete TODO 1: manhattan")
    r_s, c_s = state
    r_g, c_g = goal
    distance = abs(r_s - r_g) + abs(c_s - c_g)
    return distance 


def astar(campus, start, goal):
    # """TODO 2: Return SearchResult(path, expanded) for A* graph search."""
    # Use heapq as a priority queue and manhattan() as the heuristic.
    # Track best known g-costs and parent states in dictionaries.
    # raise NotImplementedError("Complete TODO 2: astar")
    if start == goal: #immediate edge case check
        return SearchResult(path=[start], expanded=0)

    frontier = []
    counter = 0
    g_cost = {start: 0}
    parents = {start: None}
    expanded = 0

    init_h = manhattan(start, goal)
    init_g = 0
    init_f = init_g + init_h

    heapq.heappush(frontier, (init_f, counter, init_g, start))
    counter += 1

    while frontier: 
        f, _, g, state = heapq.heappop(frontier)

        if g>g_cost.get(state, float('inf')):
            continue
        if state == goal:
            path = reconstruct_path(parents, goal)
            return SearchResult(path, expanded)
        else:
            expanded += 1
            for action, successor in campus.neighbors(state):
                new_g = g + 1

                if new_g < g_cost.get(successor, float('inf')):
                    g_cost[successor] = new_g
                    parents[successor] = state

                    new_h = manhattan(successor, goal)
                    new_f = new_g + new_h
                    heapq.heappush(frontier, (new_f, counter, new_g, successor))
                    counter += 1

    return SearchResult(path=None, expanded=expanded)


def epsilon_greedy(q_values, state, actions, epsilon, rng):
    # """TODO 3: Choose an action with epsilon-greedy exploration."""
    # q_values is a dictionary. Its keys are (state, action) pairs.
    # Example key: ((1, 1), "RIGHT"). Unseen entries have value 0.0.
    # raise NotImplementedError("Complete TODO 3: epsilon_greedy")
    if rng.random() < epsilon:
        return rng.choice(actions)

    best_actions = [] #store a list of best possible actions
    q_max = float('-inf') #start tracking best q values, use -inf because values can range from any space

    for action in actions:
        q = q_values.get((state, actions), 0.0) #use 0.0 as default, remember to use .get
        if q > q_max: #compare
            q_max = q
            best_actions = [action]
        elif q == q_max: #add anyway since it's on the last level
            best_actions.append(action)
    return rng.choice(best_actions)
#need to remember when to use action/actions/best_actions vs. q


def q_learning_update(q_values, state, action, reward, next_state,
                      actions, alpha, gamma, terminal):
    """TODO 4: Update exactly one Q-table entry in place; return nothing."""
    # Get Q(state, action), defaulting to 0.0.
    # If terminal is True, the target is reward with no continuation term.
    # Otherwise target = reward + gamma * max Q(next_state, next_action).
    # Consider every action, including unseen entries with value 0.0.
    # Apply Q <- Q + alpha * (target - Q).
    raise NotImplementedError("Complete TODO 4: q_learning_update")

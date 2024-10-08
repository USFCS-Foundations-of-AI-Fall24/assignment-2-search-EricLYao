from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    num_states = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        if goal_test(next_state[0]):
            # print("Goal found")
            # print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                # print(ptr)
            print("Total States: ", num_states)
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            num_states += len(successors)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)
    print("Total States: ", num_states)

### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True,limit=0) :
    search_queue = deque()
    closed_list = {}
    num_states = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()

        if limit > 0 and next_state[0].depth > limit:
            # go next, can still find answer at a better depth
            continue

        if goal_test(next_state[0]):
            # print("Goal found")
            # print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                # print(ptr)
            print("Total States: ", num_states)
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            num_states += len(successors)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            for s in successors :
                s[0].depth = next_state[0].depth + 1
            search_queue.extend(successors)
    print("Total States: ", num_states)
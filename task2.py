def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    # TODO
    reachable = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        reachable.add(node)
        for i in adj_list[node]:
            if i not in reachable:
                stack.append(i)
    return reachable
adj_list = [[1, 3], [2], [0], [4], [3], []]
print(reachable(adj_list,0))

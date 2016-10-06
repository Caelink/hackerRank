import Queue

def traverse(edge, curr, handled):
    if not (edge[0] == curr) and not(edge[0] in handled):
        return edge[0]
    elif not (edge[1]  == curr) and not(edge[1] in handled):
        return edge[1]
    else:
        return 0

def address_adjacent(steps, edges, initial, length):
    handled = []
    nodes_to_visit = Queue.Queue()
    nodes_to_visit.put(initial)
    while not nodes_to_visit.empty():
        curr = nodes_to_visit.get()
        adjacent_edges = [edge for edge in edges if (edge[0] == curr or edge[1] == curr)]
        adjacent_nodes = filter(None, [traverse(edge, curr, handled) for edge in adjacent_edges])
        for node in adjacent_nodes:
            steps[node-1] = length
            nodes_to_visit.put(node)
        for edge in adjacent_edges:
            edges.remove(edge)
        handled.append(curr)
        length += 6

def print_nodes(n, m, edges, s):
    steps = [-1] * n
    address_adjacent(steps, edges, s, 6)
    steps.pop(s-1)
    print ' '.join(map(str, steps))

def perform_query():
    n, m = map(int, raw_input().split(' '))
    edges = []
    for m_i in range(0, m):
        edge = map(int, raw_input().split(' '))
        if not (sorted(edge) in edges):
            edges.append(sorted(edge))
    s = int(raw_input())
    print_nodes(n, m, edges, s)
    
q = int(raw_input())

for q_i in range(0, q):
    perform_query()

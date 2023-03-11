# Adjacency List

# graph = dict()
# graph['A'] = ['B', 'C']
# graph['B'] = ['E', 'C', 'A']
# graph['C'] = ['A', 'B', 'E', 'F']
# graph['E'] = ['B', 'C']
# graph['F'] = ['C']


# Adjacency Matrix Using Adjacency List

# matrix_elements = sorted(graph.keys())
# cols = rows = len(matrix_elements)

# adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
# edges_list = []

# for key in matrix_elements:
#     for neighbor in graph[key]:
#         edges_list.append((key, neighbor))

# print(adjacency_matrix)
# print(edges_list)

# for edge in edges_list:
#     indx_first_vertex = matrix_elements.index(edge[0])
#     indx_second_vertex = matrix_elements.index(edge[1])
#     adjacency_matrix[indx_first_vertex][indx_second_vertex] = 1

# print(adjacency_matrix)

################ BFS ##################################################

from collections import deque
# graph = dict()
# graph['A'] = ['B', 'G', 'D']
# graph['B'] = ['A', 'F', 'E']
# graph['C'] = ['F', 'H']
# graph['D'] = ['F', 'A']
# graph['E'] = ['B', 'G']
# graph['F'] = ['B', 'D', 'C']
# graph['G'] = ['A', 'E']
# graph['H'] = ['C']


def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while (len(graph_queue) > 0):

        node = graph_queue.popleft()
        adj_node = graph[node]

        remaining_elements = set(adj_node).difference(set(visited_vertices))

        if (len(remaining_elements) > 0):

            for ele in sorted(remaining_elements):
                visited_vertices.append(ele)
                graph_queue.append(ele)

    return visited_vertices


# print(breadth_first_search(graph, 'A'))

##################### DFS ###################################
graph = dict()
graph['A'] = ['B', 'S']
graph['B'] = ['A']
graph['S'] = ['A', 'G', 'C']
graph['D'] = ['C']
graph['G'] = ['S', 'F', 'H']
graph['H'] = ['G', 'E']
graph['E'] = ['C', 'H']
graph['F'] = ['C', 'G']
graph['C'] = ['D', 'S', 'E', 'F']


def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = list()
    graph_stack.append(root)
    node = root

    while graph_stack:
        if node not in visited_vertices:
            visited_vertices.append(node)

        adj_nodes = graph[node]

        # All Adjacent Nodes Visited -> pop() from stack and set node to last element
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()

            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue

        # Not All Adjacent Nodes Have been Visited

        else:
            remaining_elements = set(adj_nodes).difference(
                set(visited_vertices))
            first_adj_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adj_node)
            node = first_adj_node

    return visited_vertices

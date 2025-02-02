import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys
import heapq
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

def build_tree(heap):
    if not heap:
        return None
    nodes = [Node(val) for val in heap]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0]

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def generate_colors(n):
    return ["#{:02x}{:02x}{:02x}".format(int(c[0]*255), int(c[1]*255), int(c[2]*255))
            for c in [colorsys.hsv_to_rgb(i/n, 1, 1) for i in range(n)]]

def visualize_traversal(root, order='bfs'):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    traversal_order = []
    
    if order == 'bfs':
        queue = deque([root])
        while queue:
            node = queue.popleft()
            traversal_order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    else:
        stack = [root]
        while stack:
            node = stack.pop()
            traversal_order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    colors = generate_colors(len(traversal_order))
    node_colors = {node.id: colors[i] for i, node in enumerate(traversal_order)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels={n: tree.nodes[n]['label'] for n in tree.nodes},
            arrows=False, node_size=2500,
            node_color=[node_colors.get(n, '#FFFFFF') for n in tree.nodes])
    plt.show()

heap = [3, 1, 6, 5, 2, 4]
heapq.heapify(heap)
tree_root = build_tree(heap)
visualize_traversal(tree_root, order='bfs')
visualize_traversal(tree_root, order='dfs')

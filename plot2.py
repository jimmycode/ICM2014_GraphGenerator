__author__ = 'jimmy'
import re
import networkx as nx
import matplotlib.pyplot as plt

f = open('adjacent.txt','r')

graph = {}
count = 0

while True:
    line = f.readline()
    if not line: break
    num = int(re.findall(r'\d+', line)[0])
    graph[num] = []
    num2 = int(re.findall(r'\d+', f.readline())[0])
    for i in xrange(num2):
        num3 = int(re.findall(r'\d+', f.readline())[0])
        graph[num].append(num3)

f.close()

G = nx.DiGraph()
for nodes in graph:
    G.add_node(nodes)
    if len(graph[nodes]) > 0:
        for item in graph[nodes]:
            G.add_edge(nodes, item)

pos = nx.circular_layout(G)
nx.draw(G, pos, arrows=True, node_color='w', linewidth=0.5 )
plt.savefig("graph02.png")

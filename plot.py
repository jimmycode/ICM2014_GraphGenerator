__author__ = 'jimmy'
import re
import networkx as nx
import matplotlib.pyplot as plt

f = open('Erdos1.txt','r')
flines = f.readlines()
namefile = open('authorNameList.txt','r')
namelist = namefile.readlines()
for i in xrange(len(namelist)):
    namelist[i] = namelist[i].strip()

graph = {}
count = -1
hit = 0

for l in flines:
    pattern = re.compile(r'.+\s+\d+')
    match = pattern.match(l)
    if match:
        # matchline = match.group()
        # print matchline
        # name = re.findall(r'(\w+,\s\w+\*?) | (\w+,\s\w+\s\w+\*?)', matchline)
        # print name
        # graph[m]=[]
        # cur = m
        count += 1
        graph[count] = []

    else:
        name = l.strip().upper()
        # print name
        if name in namelist:
            hit += 1
            graph[count].append(namelist.index(name))

print hit
f.close()
namefile.close()

G = nx.Graph()
G.add_nodes_from(xrange(511))
for keys in graph:
    if len(graph[keys]) > 0:
        for item in graph[keys]:
            G.add_edge(keys, item)
pos = nx.spring_layout(G, k = 0.06, iterations = 20, scale = 5.0)
nx.draw(G, pos, node_size=80, with_labels=False, node_color='r' , linewidth=0.5 )
plt.savefig("graph.png")

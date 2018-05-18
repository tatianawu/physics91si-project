import print
import networkx as nx
import matplotlib.pyplot as plt

# Number of people playing Assassins
count = 45

print.welcome()

# Create a network (MultiDiGraph)
# Each node represents a player
# Each edge {u, v} represents player v as the target of player u
G = nx.MultiDiGraph()
for i in range(count):
    G.add_edge(i%count, (i+1)%count)

# Draw the graph
nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color='b', edge_color='b')

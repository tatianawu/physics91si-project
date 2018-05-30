"""

    *** Previous version ***
*** See vis.py for current version ***

"""

import print
import data
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pylab
pylab.ion

# Number of people playing Assassins
nplayers = len(data.players)
nelim = 0

# Create a network (MultiDiGraph)
# Each node represents a player
# Each edge {u, v} represents player v as the target of player u
G = nx.DiGraph()
for i in range(nplayers):
    G.add_edge(data.players[i], data.players[(i+1)%nplayers])


# def draw_network(G):
#     nx.draw(G, pos=nx.kamada_kawai_layout(G), arrows=True, with_labels=True)
#     anim = animation.FuncAnimation(G, update_network, len(data.eliminated), fargs=(G), interval=50, blit=False)

def init_network():
    nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color='b', arrows=True, with_labels=True)

def find_assassin(victim):
    for n in G:
        for nbr in G[n]:
            if nbr == victim: return n

def find_new_target(victim):
    for nbr in G[victim]:
        return nbr

def update_network():
    global nelim
    victim = data.eliminated[nelim]
    assassin = find_assassin(victim)
    new_target = find_new_target(victim)
    G.remove_edge(assassin, victim)
    G.remove_edge(victim, new_target)
    G.remove_node(victim)
    G.add_edge(assassin, new_target)
    nelim += 1
    nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color='b', arrows=True, with_labels=True)

def final_network():
    nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color='b', arrows=True, with_labels=True)

def draw_network():
    pylab.show()
    init_network()
    pylab.draw()
    for i in range(len(data.eliminated)):
        pylab.cla()
        update_network()
        pylab.draw()
        plt.pause(0.5)

    final_network()
    pylab.draw()
    plt.pause(30)


print.welcome()
print.start()
draw_network()

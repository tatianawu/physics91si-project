"""
File: vis.py
=============
Visualizes Otero Assassins.

"""

import print
import data
import networkx as nx
import matplotlib.pyplot as plt
import pylab
pylab.ion

# Number of people playing Assassins
nplayers = len(data.players)
# Number of players eliminated thus far
nelim = 0

# Create a network:
# Each node represents a player
# Each edge {u, v} represents player v as the target of player u
G = nx.DiGraph()
for i in range(nplayers):
    G.add_edge(data.players[i], data.players[(i+1)%nplayers])


"""
Function: init_network
=======================
Draws the initial network of players.

"""
def init_network():
    nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color=data.colors, arrows=True, with_labels=True)


"""
Function: find_target_idx
==========================
Takes the node representing the current target and returns its index in the nodelist.

"""
def find_target_idx(target):
    for i in range(len(G)):
        if list(G.nodes)[i] == target: return i;


"""
Function: find_assassin
========================
Takes the node representing the current target and returns the node preceding it -- the assassin.

"""
def find_assassin(target):
    for n in G:
        for nbr in G[n]:
            if nbr == target: return n


"""
Function: find_new_target
==========================
Takes the node representing the current target and returns the node to which it points -- the new target of the assassin.

"""
def find_new_target(target):
    for nbr in G[target]:
        return nbr


"""
Function: show_target
======================
Takes the index of the target in the nodelist. Changes the color of the target to red and the color of the assassin to green
and draws the network.

"""
def show_target(target_idx):
    data.colors[target_idx] = '#ff0000' # indicate target by red
    data.colors[(target_idx-1)%len(G)] = '#00ff7f' # indicate assassin by green
    nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color=data.colors, arrows=True, with_labels=True, font_size=8)


"""
Function: kill_target
======================
Takes the node and index of the current target. Removes the target from the game and assigns the assassin their new target.
Redraws the network without the target.

"""
def kill_target(target, target_idx):
    assassin = find_assassin(target)
    new_target = find_new_target(target)
    G.remove_edge(assassin, target)
    G.remove_edge(target, new_target)
    G.remove_node(target)
    G.add_edge(assassin, new_target)
    del data.colors[target_idx]
    nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color=data.colors, arrows=True, with_labels=True, font_size=8)


"""
Function: update_network
=========================
Resets the color of the previous assassin and draws the network again.

"""
def update_network(assassin_idx):
    data.colors[assassin_idx] = '#b2b2ff'
    nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color=data.colors, arrows=True, with_labels=True, font_size=8)


"""
Function: final_network
========================
Draws the outcome of the game -- shows just the winner.

"""
def final_network():
    nx.draw(G, pos=nx.kamada_kawai_layout(G), node_color='#ffa500', arrows=True, with_labels=True, font_size=8)


"""
Function: draw_network
=======================
Repeatedly draws the network -- in a pseudo-animation -- of Assassins.

"""
def draw_network():
    global nelim
    pylab.show()
    init_network()
    pylab.draw()
    for i in range(len(data.eliminated)):
        target = data.eliminated[nelim]
        target_idx = find_target_idx(target)
        pylab.cla()
        show_target(target_idx)
        pylab.draw()
        plt.pause(0.3)
        pylab.cla()
        kill_target(target, target_idx)
        pylab.draw()
        plt.pause(0.3)
        pylab.cla()
        update_network((target_idx-1)%len(G))
        pylab.draw()
        pylab.cla()
        nelim += 1

    final_network()
    pylab.draw()
    plt.pause(30)


"""
Function: __main__
====================
Runs the program.

"""
if __name__ == '__main__':
    print.welcome()
    print.start()
    draw_network()

# cecullar_automata

This is a Python library which can create cecullar automata either given only the dimenssions of a board and set your rule or use ours either input you array

Example

from cecullar_automata.cecullar_automata import cecullar_automata as ca
d=ca(width=100,height=100,generations=100) 
d.game_of_life()

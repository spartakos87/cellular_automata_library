# Cellular Automata

We present you a new Python library , the **cellular_automata**.

## How to install

Clone the current repository and then,

```bash
> cd cellular_automata
> python3 setup.py install
```

That's it you already you have install it.

## What can I do?

Let's start with a simple and famous example - cellular automata, the [game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) .  Show go to favorite Python IDE or directly to Python repl and copy the follow piece of code,

 ```python
from cecullar_automata.cecullar_automata import cecullar_automata as ca
game_of_life = ca(width=100,height=100,generations=100)
game_of_life.game_of_life()

 ```

At the end , a GIF will be pop up to our desktop , like this,


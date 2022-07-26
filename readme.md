<div align=center>
  <br>
  <img width=55% src='./lilly.svg'></img>
  <br>
</div>


# Lilly

Lilly is a minimal library for composing [pure functions](https://en.wikipedia.org/wiki/Pure_function) using pipe notation. If `f` and `g` are functions then `f | g` is a function such that `(f | g)(x) = g(f(x))`. 


## Composables

Lilly exports a function decorator called `Composable`. Any two composable functions can be composed using the `|` operator. For example,

```py
from lilly import Composable
```

Create two composable functions...

```py
f = Composable(lambda x: x + 1)

g = Composable(lambda x: x * 2)
```

Compose them...

```py
h = f | g 
```

Apply the composite...

```py
h(2)  # returns 6 
```

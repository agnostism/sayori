<div align=center>
  <br>
  <img width=50% src='./images/lamb.svg'></img>
  <br>
</div>

# Lilly

Lilly is a minimal library for composing [pure functions](https://en.wikipedia.org/wiki/Pure_function) using pipe notation. If `f` and `g` are functions, then `h = f | g` is a function such  
that `h(x) = g(f(x))`. 


## Usage

Lilly exports a decorator called `Composable` which allows a function to support piping. Any two composable functions can be combined using the `|` operator. For example,

```py
from lilly import Composable
```

Create two composables...

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


## API

* `Composable(callable: Callable)` - creates a composable from a callable. 

* `(left: Composable) | (right: Composable)` - combines two composables, such that `(f | g)(x) = g(f(x))`.

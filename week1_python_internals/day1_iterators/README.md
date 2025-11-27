# EvenRange Iterator

A simple Python class that implements a custom iterator to yield even numbers between a given start and end.
https://realpython.com/python-iterators-iterables/#understanding-iteration-in-python

## Features

* Returns all even numbers in the specified range (inclusive).
* Easy to use with Python `for` loops.
* Can be extended with additional features like reverse iteration.

## Installation

No installation required. Just include the `EvenRange` class in your project.

```python
from even_range import EvenRange  # if saved in a separate file
```

## Usage

```python
# Create an iterator for even numbers between 1 and 10
evens = EvenRange(1, 10)

for num in evens:
    print(num)
```

**Output:**

```
2
4
6
8
10
```

## How It Works

* The iterator starts at the first even number greater than or equal to the `start`.
* Each call to `__next__()` increments by 2 until reaching the `end`.
* Raises `StopIteration` when the range is exhausted.

## Extending

* You can add a `reverse` flag to iterate backward.
* Can be adapted to support custom step sizes.

## Author

Ruchita Gelani

## License

MIT License

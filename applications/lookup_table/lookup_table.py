# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

fact_cache = {}

def recur_factorial(n):
  if n not in fact_cache:
    if n == 1:
      return n
    else:
      fact_cache[n] = n*recur_factorial(n-1)
      return fact_cache[n]
  else:
    return fact_cache[n]

def facti(n):
    if n not in fact_cache:
        if n == 1:
            return n
        else:
            fact_cache[n] = math.factorial(n)
            return fact_cache[n]
    else:
        return fact_cache[n]

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    key = (x,y)
    cache = {}
    if key not in cache:
        v = math.pow(x,y)
        v = facti(v)
        v //= (x + y)
        v %= 982451653
        cache[key] = v
        return cache[key]
    else:
        return cache[key]
    



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

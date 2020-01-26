# Collections module

# === List as Stack (LIFO) ===
# Just use append and pop (this operations are fast)
stack = []
stack.append(1)
stack.append(2)
stack.pop() # 2
stack.pop() # 1


# === Deque as Queue (FIFO) ===
# Add or rem elements to the beginning of the list is slow because the others have to shift one place.
# Better use `Deque`

from collection import deque
queue = deque([0, 1, 2])
queue.append(3)
queue.append(4)
queue.popleft() # 0
queue.popleft() # 1


# === Counter ===
# dictionary to keep a counter of the occurrence of the keys
from collections import Counter
counterA = Counter(['a','b','b','c'])
print(counterA) # Counter({'b': 2, 'a': 1, 'c': 1})

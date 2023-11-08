import numpy as np

data = input().strip()

moves = { "^": np.array([0, 1]), "v": np.array([0, -1]), "<": np.array([-1, 0]), ">": np.array([1, 0]),}
pos = np.array([0, 0])

def to_tuple(a):
    return tuple(a.tolist())
visited = dict()
visited[to_tuple(pos)] = 1


for c in data:
    assert c in moves
    pos += moves[c]
    if to_tuple(pos) not in visited:
        visited[to_tuple(pos)] = 0
    visited[to_tuple(pos)] += 1

print(len(visited))



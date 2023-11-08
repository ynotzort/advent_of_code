import numpy as np

data = input().strip()

moves = { "^": np.array([0, 1]), "v": np.array([0, -1]), "<": np.array([-1, 0]), ">": np.array([1, 0]),}
pos = np.array([0, 0])
pos2 = np.array([0, 0])

def to_tuple(a):
    return tuple(a.tolist())
visited = dict()
visited[to_tuple(pos)] = 1

real_santa = True

for c in data:
    assert c in moves
    if real_santa:
        pos += moves[c]
        posx = pos
    else:
        pos2 += moves[c]
        posx = pos2
    if to_tuple(posx) not in visited:
        visited[to_tuple(posx)] = 0
    visited[to_tuple(posx)] += 1
    real_santa = not real_santa

print(len(visited))



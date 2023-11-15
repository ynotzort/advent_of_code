import fileinput
import itertools
from tqdm import tqdm

graph = dict()
def add_to_graph(graph, f,t,d):
    if f not in graph:
        graph[f] = dict()
    graph[f][t] = d
    return graph

for line in fileinput.input():
    line = line.strip()
    rest, dist = line.split(" = ")
    f, t = rest.split(" to ")
    graph = add_to_graph(graph, f,t,int(dist))
    graph = add_to_graph(graph, t,f,int(dist))
    

print(graph)
print(len(graph))

cities = list(graph.keys())

def compute_path_len(graph, path):
    ax = 0
    pos = path[0]
    for p in path[1:]: 
        assert p!=pos
        ax += graph[pos][p]
        pos = p
    return ax

min_path_len = 0
for perm in itertools.permutations(cities):
    path_len = compute_path_len(graph, perm)
    # print(perm, path_len)
    min_path_len = max(min_path_len, path_len)
    # break

print(min_path_len)

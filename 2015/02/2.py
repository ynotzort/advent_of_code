import fileinput

ax = 0
for line in fileinput.input():
    line = line.strip()
    dims = sorted([int(x) for x in line.split("x")])
    assert len(dims) == 3
    sides = dims[0]*2 + dims[1]*2 + dims[0]*dims[1]*dims[2]
    ax += sides
print(ax)


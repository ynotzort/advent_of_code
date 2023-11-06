import fileinput

ax = 0
for line in fileinput.input():
    line = line.strip()
    dims = [int(x) for x in line.split("x")]
    assert len(dims) == 3
    sides = dims[0]*dims[1], dims[1]*dims[2], dims[0]*dims[2]
    area = sum(sides)*2 + min(sides)
    ax += area
print(ax)


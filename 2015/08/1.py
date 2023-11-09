import fileinput

data = fileinput.input()

ax, bx = 0, 0
for line in data:
    line = line.strip()
    l, le = len(line), len(eval(line))
    print(line)
    print(eval(line))
    print(l, le)
    ax += l
    bx += le

print(ax, bx, ax-bx)

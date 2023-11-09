import fileinput
import codecs

data = fileinput.input()

ax, bx, cx = 0, 0, 0
for line in data:
    line = line.strip()
    l, le = len(line), len(eval(line))
    ext = len(line.encode("unicode-escape").decode('utf-8').replace('"', r'\"'))+2
    print(line.encode("unicode-escape").decode('utf-8').replace('"', r'\"'))
    print(line)
    print(eval(line))
    print(l, le, ext)
    ax += l
    bx += le
    cx += ext
    # break

print(ax, bx, cx, ax-bx, cx-ax)

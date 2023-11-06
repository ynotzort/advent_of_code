
data = input("")

print(data)
movement = {"(": 1, ")": -1}

ax = 0
for i, c in enumerate(data):
    ax += movement[c]
    if ax == -1:
        print(i + 1)
        break



import itertools

def describe(s: str) -> list[tuple[str,int]]:
    res = []
    for k,v in itertools.groupby(s):
        res.append((k, len(list(v))))
    return res

def say(t: tuple[str, int]) -> str:
    return f"{t[1]}{t[0]}"

def say_all(l: list[tuple[str, int]]) -> str:
    return "".join(map(say, l))

# print(say_all(describe("1211")))

next = "1113122113"
print(next)
for i in range(50):
    next = say_all(describe(next))
    # print("-----")
    # print(next)

print(len(next))



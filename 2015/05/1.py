import fileinput

data = fileinput.input()

def is_nice(word: str) -> bool:
    vowels = has_n_vowels(word) 
    conseq = has_conseq_let(word) 
    forb = has_no_forbidden_words(word)
    print(f"{word=} -> {vowels=} {conseq=} {forb=}")
    return vowels and conseq and forb

def has_n_vowels(word: str, num: int = 3) -> bool:
    vowels = set("aeiou")
    return num <= sum(c in vowels for c in word)

def has_conseq_let(word: str) -> bool:
    assert len(word)>1
    return any(True for i in range(len(word)-1) if word[i]==word[i+1])

def has_no_forbidden_words(word: str) -> bool:
    forbidden = {"ab", "cd", "pq", "xy"}
    for f in forbidden:
        if f in word:
            return False
    return True

ax = 0
for line in data:
    line = line.strip()
    ax += is_nice(line)

print(ax)


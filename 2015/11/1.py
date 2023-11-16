import string
from tqdm import tqdm

data = input().strip()

alphabet = string.ascii_lowercase
inv_alph = {v:i for i,v in enumerate(alphabet)}
modulos = len(alphabet)
n_digits = 8
print(alphabet, inv_alph, modulos)

def int2pass(i: int) -> tuple[int, ...]:
    if i == 0:
        return (0, )
    digits = []
    while i:
        digits.append(int(i%modulos))
        i = i // modulos
    if len(digits) < n_digits:
        digits.extend([0] * (n_digits - len(digits)))

    return tuple(digits[::-1])

def pass2int(p: tuple[int, ...]) -> int:
    ax = 0
    f = 1
    for v in p[::-1]:
        ax += v*f
        f *= modulos
    return ax

def pass2str(p: tuple[int, ...]) -> str:
    return "".join(map(lambda r: alphabet[r], p))

def str2pass(s: str) -> tuple[int, ...]:
    return tuple(inv_alph[c] for c in s) 

def p_has_strait(p: tuple[int, ...]) -> bool:
    for i in range(len(p) - 2):
        if p[i] == p[i+1]-1 and p[i+1] == p[i+2]-1:
            return True
    return False

def p_has2pairs(p: tuple[int, ...]) -> bool:
    n = len(p)
    for i in range(n-3):
        if p[i] == p[i+1]:
            for j in range(i+1, n-1):
                if p[i] != p[j]:
                    if p[j] == p[j+1]:
                        return True
    return False



print(data)
ps = str2pass(data)
print(ps, pass2str(ps))
psi = pass2int(ps)
print(psi)
print(int2pass(psi))
print(pass2str(int2pass(psi)))

print("has2pairs", p_has2pairs(ps))
print("has_strait", p_has_strait(ps))

ps_cur = ps
for i in tqdm(range(26**8)):
    psi_c = pass2int(ps_cur)
    ps_cur = int2pass(psi_c+1)
    ps_cur_str = pass2str(ps_cur)
    # print(ps_cur, ps_cur_str)
    if 'i' in ps_cur_str or 'o' in ps_cur_str or 'l' in ps_cur_str:
        continue
    if p_has_strait(ps_cur) and p_has2pairs(ps_cur):
        print("** gg **")
        print(ps_cur_str)
        break



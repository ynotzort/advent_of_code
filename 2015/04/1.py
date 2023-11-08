import hashlib

def compute_md5(in_str: bytes) -> str:
    m = hashlib.md5()
    m.update(in_str)
    return m.hexdigest()

def has_leading_zeros(in_str: str, num_zeros: int = 5) -> bool:
    return in_str.startswith("0"*num_zeros)

salt = input().strip().encode()
print(salt)
for i in range(10000000):
    v = salt + str(i).encode()
    hash = compute_md5(v)
    if has_leading_zeros(hash):
        print(hash)
        print(v)
        print(i)
        break


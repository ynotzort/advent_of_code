import fileinput
import functools

data = fileinput.input()

rules = dict()

def AND(a: int, b: int) -> int:
    return a & b

def OR(a: int, b: int) -> int:
    return a | b

def NOT(a: int) -> int:
    return ~a

def LSHIFT(a: int, b: int) -> int:
    return a << b

def RSHIFT(a: int, b: int) -> int:
    return a >> b

ops = dict(AND=AND, OR=OR, NOT=NOT, LSHIFT=LSHIFT, RSHIFT=RSHIFT)


@functools.cache
def eval_r(var_name: str) -> int:
    if var_name.isdecimal():
           return int(var_name)
    assert var_name in rules, var_name
    op, args = rules[var_name]
    if op == "CONST":
        assert len(args) == 1
        val = args[0]
        if val.isdecimal():
           return int(val)
        else:
           return eval_r(val)
    elif op in ops:
        args_evald = [eval_r(a) for a in args]
        return ops[op](*args_evald)
    else:
        raise ValueError()
    
    




for line in data:
    line = line.strip()
    lhs, rhs = line.split(" -> ")
    assert rhs not in rules
    lhs_ops = lhs.split(" ")
    rr = None
    if len(lhs_ops) == 1:
        # assert lhs_ops[0].isdecimal(), lhs_ops[0]
        rr = ("CONST", [lhs_ops[0]])
    if len(lhs_ops) == 2:
        assert lhs_ops[0] == 'NOT'
        rr = ("NOT", [lhs_ops[1]])
    if len(lhs_ops) == 3:
        assert lhs_ops[1] in ops
        assert lhs_ops[1] != 'NOT'
        rr = (lhs_ops[1], [lhs_ops[0], lhs_ops[2]] )
    if len(lhs_ops) > 3:
        raise ValueError()

    assert rr is not None
    rules[rhs] = rr

rules["b"] = ("CONST", ["46065"])
# print(rules)
print( eval_r("a") )


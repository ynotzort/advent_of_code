
data = input("")

print(data)
positive = data.count('(')
negative = data.count(')')
print(f'{positive=} {negative=} {positive-negative=}')

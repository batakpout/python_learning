
"""
join concatenate any number of strings
"""
a = ['A', 'E', 'I', 'O', 'U']
s = ' '.join(a)
print(type(s))
print(s)
x = '.'.join(['ab', 'pq', 'rs'])
print(x)
y = '.'.join(x for x in ['a', 'b'])
print(y)
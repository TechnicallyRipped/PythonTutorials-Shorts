


from types import MappingProxyType

original = {'a': 1, 'b': 2}

proxy = MappingProxyType(original)

original['c'] = 3
print(proxy['c'])

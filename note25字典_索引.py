brand = ['李宁', '耐克', '阿迪达斯', '安踏']
slogan = ['一切皆有可能', 'Just do it'
    , 'Impossible is nothing', '永不止步']
print('安踏:', slogan[brand.index('安踏')])

# dictl = {键 : 值}
dictl = {'李宁': '一切皆有可能'
    , '耐克': 'Just do it'
    , '阿迪达斯': 'Impossible is nothing'
    , '安踏': '永不止步'}
print('安踏:', dictl['安踏'])
dict2 = {1: 'one', 2: 'tow'}
print(dict2[2])
dict3 = {}  # 空字典

dict3 = dict((('F', 70), ('i', 105), ('h', 184)))
print(dict3)

dict4 = dict(安踏='永不止步', 李宁='一切皆有可能')
print(dict4)

# 如果不存在就创建一个，存在就覆盖他的值
dict4['安踏'] = '安踏，永不止步'
print(dict4)
dict4['耐克'] = '耐克耐克耐克耐克'
print(dict4)
help(dict)

# Help on class dict in module builtins:
#
# class dict(object)
#  |  dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs
#  |  dict(iterable) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in iterable:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |
#  |  Methods defined here:
#  |
#  |  __contains__(self, key, /)
#  |      True if D has a key k, else False.
#  |
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __getitem__(...)
#  |      x.__getitem__(y) <==> x[y]
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |
#  |  __len__(self, /)
#  |      Return len(self).
#  |
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |
#  |  __setitem__(self, key, value, /)
#  |      Set self[key] to value.
#  |
#  |  __sizeof__(...)
#  |      D.__sizeof__() -> size of D in memory, in bytes
#  |
#  |  clear(...)
#  |      D.clear() -> None.  Remove all items from D.
#  |
#  |  copy(...)
#  |      D.copy() -> a shallow copy of D
#  |
#  |  fromkeys(iterable, value=None, /) from builtins.type
#  |      Returns a new dict with keys from iterable and values equal to value.
#  |
#  |  get(...)
#  |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
#  |
#  |  items(...)
#  |      D.items() -> a set-like object providing a view on D's items
#  |
#  |  keys(...)
#  |      D.keys() -> a set-like object providing a view on D's keys
#  |
#  |  pop(...)
#  |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#  |      If key is not found, d is returned if given, otherwise KeyError is raised
#  |
#  |  popitem(...)
#  |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
#  |      2-tuple; but raise KeyError if D is empty.
#  |
#  |  setdefault(...)
#  |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
#  |
#  |  update(...)
#  |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#  |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
#  |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
#  |      In either case, this is followed by: for k in F:  D[k] = F[k]
#  |
#  |  values(...)
#  |      D.values() -> an object providing a view on D's values
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  __hash__ = None

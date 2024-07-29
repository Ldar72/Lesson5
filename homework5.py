immutable_var = 1, 2, False, 'Start'
print(immutable_var)
# immutable_var[1] = 42
# print(immutable_var)
# Если мы попытаемся изменить значение в immutable_var, у нас ничего не получится.
# Пример выше выдаст ошибку 'TypeError: 'tuple' object does not support item assignment'.
# Это произошло потому, что immutable_var относится к типу "кортеж" (tuple), в чем мы можем легко убедиться:
# print (type(immutable_var))
mutable_list = [1, 2, False, 'Start']
mutable_list = mutable_list[0:4] + ['Modified Final']
print(mutable_list)

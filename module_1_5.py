immutable_var = ('Привет', 20, True, 21.7, ['рыба', 'персики', 'черешня'])
print(immutable_var)

#immutable_var[0] = 'Самокат'
#print(immutable_var)
#Кортеж является не изменяемым обьектом. Но он может содержать изменяемые элементы напримерт список:
immutable_var[4][1] = 'кокос'
print(immutable_var)



mutable_list = [1, 2, 5, 4, 8]
print(mutable_list)
mutable_list[4] = 10
print(mutable_list)
mutable_list[4] = mutable_list[4] - 2
print(mutable_list)
my_dict = {'Кот': 'Животное', 'Карась': 'Рыба', 'Орел': 'Птица'}
print(my_dict)
print(my_dict['Орел'])
print(my_dict.get('Кит', 'Еще не внесет'))
my_dict.update({'Кит': 'Млекопитающие',
                'Ворона': 'Птица'})
print(my_dict)
a = my_dict.pop('Кит')
print(a)
print(my_dict)


my_set = {1, 5, 4, 6, 7, 8, 'Кот', 2.5, False, 1, 8, 3.5, 7, 'Кот'}
print(my_set)
my_set.update([3, True, 10])
my_set.discard(8)
print(my_set)


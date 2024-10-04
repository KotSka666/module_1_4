

my_string = str(input('Введите текст: '))
print(f'Количество символов: {len(my_string)}\n{my_string.lower()}\n{my_string.upper()}\n'
      f'{my_string.replace(input('Какой символ вы хотите заменить? '), input("На какой символ произвести замену? "))}\n'
      f'Первый символ строки {my_string[0]}\n'
      f'Последний символ строки {my_string[-1]}')



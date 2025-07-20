def sum_nums(a, b):
  try:
    print(float(a)+float(b))
  except ValueError:
    print('Функция сложения работает только с числами.')


print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление')
choice = input('Введите номер действия: ')
if choice == '1':
  a = input()
  b = input()
  sum_nums(a, b)
else:
  print("Такого действия нет.")


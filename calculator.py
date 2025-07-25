def sum_nums(a, b):
	try:
		print(f'{a} + {b} = {float(a)+float(b)}')
	except ValueError:
		print('Функция сложения работает только с числами.')
		print(f'{a} + {b} = {0}')
    
def dum_nums(a, b):
	try:
		print(f'{a} - {b} = {float(a)-float(b)}')
	except:
		print('Функция вычитания работает только с числами.')
		print(f'{a} - {b} = {0}')
def multy(a, b):
	try:
		print(f'{a} * {b} = {float(a)*float(b)}')
	except:
		print('Функция умножения работает только с числами.')
		print(f'{a} * {b} = {0}')
def del_nums(a, b):
	try:
		print(f'{a} / {b} = {float(a)/float(b)}')
	except ValueError:
		print('Функция деления работает только с числами.')
		print(f'{a} / {b} = {0}')
	except:
		print('Нельзя делить на ноль.')
		print(f'{a} / {b} = {0}')


print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n10. Выход')
while True:
	choice = input('Введите номер действия: ')
	if choice in {'1', '2', '3', '4', '10'}:
		if choice != '10':
			if choice == '1':
				a = input()
				b = input()
				sum_nums(a, b)    
			if choice == '2':
				a = input()
				b = input()
				dum_nums(a, b)
			if choice == '3':
				a = input()
				b = input()
				multy(a, b)
			if choice == '4':
				a = input()
				b = input()
				del_nums(a, b)
		else:
			print('Выход из калькулятора')
			break
	else:
		print('Такого действия нет.')
		

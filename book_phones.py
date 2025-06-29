book_phones = {
  'Квам-Дамн': '-79899899889',
  'Лук Скамворкер': '112',
  'Петард Вейпер': '1',
  'Лия Моргала': '+09998765432',
  'Эдуард Скамворкер': '0'
}
# Напиши код тут
contact = int(input())
if contact == 1:
	one = input()
	if one in book_phones:
		print(book_phones[one])
	else:
		print('Нет в телефонной книге')
elif contact == 2:
	two = input()
	number = input()
	book_phones[two] = number 
	for key in book_phones:
			print(f'{key}: {book_phones[key]}')
elif contact == 3:
	three = input()
	number3 = input()
	book_phones[three] = number3
	for key in book_phones:
			print(f'{key}: {book_phones[key]}')	
elif contact == 4:
	four = input()
	if four in book_phones:
		del book_phones[four]
		for key in book_phones:
				print(f'{key}: {book_phones[key]}')	   
	else:
		print('Нет в телефонной книге')
elif contact == 5:
  for key in book_phones.keys():
    	print(key)
elif contact == 6:
  for val in book_phones.values():
    	print(val)
  	
    
# Этот код используй для вывода обновлённой телефонной книги в формате "{имя}: {телефон}".
#for key in book_phones:
#    print(f'{key}: {book_phones[key]}')

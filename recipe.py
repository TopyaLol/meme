recipe = []
while True:
		ing = input()
		if ing == '':
			break
		elif 'лук' in ing:
			continue
		else:
			recipe.append(ing)

print(*recipe)

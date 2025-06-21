# Код ниже  - подсказка, с чего можно начать.
# Если он тебе не понятен - смело удаляй.
white_list = []
answers = []

while True:
    white_request = input('Разрешенный запрос: ')
    if white_request == '':
      break
    else:  
      white_list.append(white_request)

while True:
    request = input()
    if request == '':
      break
    elif request in white_list:
      answers.append(request)
    else:
      continue
for i in range(len(answers)):
  print(answers[i])
  # Продолжи решение тут

def menu():
    print("1.Добавить запись")
    print("2.Просмотреть все записи")
    print("3.Выход")
    return input("Выберите пункт меню: ")
deal = menu()
while deal != "3":
    if deal == "1":
        f = open("text.txt", "a", encoding = "utf-8")
        writing = input("Введите запись: ")
        f.write(f"{writing}\n")
        f.close()
        deal = menu()
    elif deal == "2":
        f = open("text.txt", "r", encoding = "utf-8")
        print(f.read())
        f.close()
        deal = menu()
    else:
        print("Неверный пункт меню")
        deal = menu()
print("Выход из программы...")

#with open("text.txt", "r", encoding="utf-8") as f:
#    print(f.read())
#food = []

#for line in f:
#    line = line.replace("\n", "")
#    food.append(line)
#print(food)

#with open("check.txt", "r", encoding="utf-8") as f:
#    sum = 0
#    list = []
#    for line in f:
#        line = line.replace("\n", "")
#        line = line.split(" ")
#        sum += int(line[1])
#        list.append(line[0])
        
#    print(list)

f = open("text.txt", "r", encoding="utf-8")
restaurant = {"details": []}
for item in f.read().split("***\n"):
  item_list = item.split("\n")
  restaurant["details"].append({
      "administrator": item_list[0],
      "turnover": int(item_list[1]),
      "profit": int(item_list[2]),
      "employees": int(item_list[3])
  })
print(restaurant)

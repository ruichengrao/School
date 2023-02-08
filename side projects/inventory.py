shoppingList = {}
itemCount = input("How much items?")

itemInt = int(itemCount)

for i in range(itemInt):
    item = input("Items Name")
    amount = input("Number of Items")
    shoppingList[item] = amount

var = 0.0
for (key, value) in shoppingList.items():
    print(key + ": $" + value)
    var += float(value)
    roundVar = round(var, 2)
print("Total: $" + str(var))







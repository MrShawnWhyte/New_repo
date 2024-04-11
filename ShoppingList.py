apple = float(1)
orange = float(1)
watermelon = float(4)
eggs = float(8)
cookies = float(6)
water = float(3)
milk = float(6)
chicken = float(8)
bacon = float(6)

ans_a = ["a", "A"]
ans_b = ["b", "B"]

store = {
    'apple' '':1,
    'orange': 1,
    'watermelon': 4,
    'eggs': 8,
    'cookies': 6,
    'water': 2,
    'milk': 2,
    'chicken': 8,
    'bacon': 6}

print("""
I only brought 1 bag that can atleast store 5 items
What should I buy""")

print("""The store have these items on sale
    """,)

print(store)
#print("""
#apple $1
#orange $1
#watermelon $4
#eggs $8
#cookies $6
#water $3
#milk $6
#chicken $8
#bacon $6
#""")

inventory = []

item1 = input("What should I buy >>")
if item1 not in inventory:
    inventory.append(item1)

item2 = input("What else")
if item2 not in inventory:
    inventory.append(item2)

item3 = input("What else")
if item3 not in inventory:
    inventory.append(item3)
    
item4 = input("What else")
if item4 not in inventory:
    inventory.append(item4)

item5 = input("lastly")
if item5 not in inventory:
    inventory.append(item5)
    
print(len(inventory))
print("""
Items in your bag""")

#FINISH
print(""" a) remove an item  b) cost""")

ans1 = input(">>")

if ans1 in ans_a: 
    print(inventory)

    inv = input("Disposing of an item")
    inventory.remove(inv)

    print(inventory)
    
    cost = item1 + item2 + item3 + item4 + item5
        
    print(cost)

if ans1 in ans_b:
    cost = item1 + item2 + item3 + item4 + item5
        
    print(cost)

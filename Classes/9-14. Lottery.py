import random

lottery = ['5', '6', '2', '4', '9', '11', '33', '88', '0', '44', 'l', 'p', 'e', 's', 'n']
results = []

print("Any ticket matching these four numbers or letters wins a prize:")
lot_1 = random.choice(lottery) 
results.append(lot_1)

lot_2 = random.choice(lottery)
results.append(lot_2)

lot_3 = random.choice(lottery)
results.append(lot_3)

lot_4 = random.choice(lottery)
results.append(lot_4)

lot_5 = random.choice(lottery)
results.append(lot_5)

print(f"Here are the lottery results:\n{results}")

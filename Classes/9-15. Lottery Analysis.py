import random

lottery = ['5', '6', '2', '4', '9', '11', '33', '88', '0', '44', 'l', 'p', 'e', 's', 'n']
results = []
results_temp = []
my_ticket = ['2', 'l', '88', 'p', 's']
active = True
count = 0

print("Any ticket matching these four numbers or letters wins a prize:")
while True: 
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

    results_temp = results[:]
    results.clear()
    print("Here are the lottery results:")
    print(f"{results_temp}")
    count += 1

    if results_temp != my_ticket:
        print("Sorry, you did not win the lottery!\n")
        results_temp.clear()

    if results_temp == my_ticket:
        print("You have won the lottery!")
        print(f"It has taken you {count} attempts to win.")
        active = False
        
               

    


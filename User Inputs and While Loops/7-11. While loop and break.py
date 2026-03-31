prompt = "\nEnter the name of a city you have visited: "
prompt += "\nEnter 'quit' to end the program."

while True: # a loop that starts with While True will run forever
    city = input(prompt)

    if city =='quit':
        break # break stops the code from continously running when city == 'quit'
    else:
        print(f"I'd love to go to {city.title()}!")

    
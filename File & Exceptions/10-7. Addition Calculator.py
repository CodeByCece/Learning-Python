"""program that prompts user for two numbers,
sums them and prints the result."""

print("Give me two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nEnter your first number:")
    if first_number == 'q':
        break
    second_number = input("\nEnter your second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)+ int(second_number)
    except ValueError:
        print("You can only add numbers!")
    else: 
        print(f"The sum of {first_number} and {second_number} is {answer}")

    
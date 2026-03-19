#4-3 Counting to Twenty
for value in range(1, 21):
    print(value)

#4-6 Odd numbers
odd_numbers = [] 
for number in range(1, 20, 2):
    odd_numbers.append(number)
print(odd_numbers)


#4-7. Threes
threes = []
for value in range(3, 31, 3):
    new = value * 3
    threes.append(new)
print(threes)

#4-8 Cubes
cubes = []
for cube in range(1, 11):
    cubed = cube** 3
    cubes.append(cubed)
print(cubes)

#4-9 Cube Comprehension
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)
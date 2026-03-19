#6-5 Rivers exercise

rivers = {
    'nile' : 'egypt',
    'amazon' : 'brazil',
    'Yangtze' : 'china'
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print(f"\n")

for name in rivers.keys():
    print(name.title())

print(f"\n")

for location in rivers.values():
    print(location.title())
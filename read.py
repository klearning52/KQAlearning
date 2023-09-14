fileobjectvar = open("car.csv")

print(type(fileobjectvar))

companies = []

sales = []

with open("car.csv") as file:
    lines = file.readlines()
for line in lines:
    print(line)

for line in fileobjectvar:
    data = line.split
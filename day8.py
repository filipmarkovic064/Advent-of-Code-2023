f = open("8.txt").read().splitlines()

steps = 0
teller = 0

instruksjon = f[0]
node = "AAA"

hash = {}
for line in f[1:]:
    tempList = line.split(" = ")
    hash[tempList[0]] = tempList[1]
while node != "ZZZ":
    if instruksjon[teller] == "L":
        node = hash[node][1:4]
    else:
        node = hash[node][6:9]

    if teller >= len(instruksjon)-1:
        teller = 0
    else:
        teller+= 1
    steps+= 1
print(steps)

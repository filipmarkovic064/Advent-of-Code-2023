sum = 0
sum_p2 = 0
#filnavn = input("Input file: ")
f = open("6.txt").read().splitlines()

times = f[0].strip("Time: ").split()
distances = f[1].strip("Distance: ").split()
hash = {}
time_p2 = ""
distance_p2 = ""

for x in range(len(times)):
    hash[times[x]] = distances[x]
    time_p2+=times[x]
    distance_p2+=distances[x]

for x in hash:
    tempList = []
    tempX = int(x)
    for y in range(tempX):
        if y*(tempX-y) > int(hash[x]):
            tempList.append(y)
    if sum == 0 and len(tempList) != 0:
        sum = 1
        sum = sum*len(tempList)
    else:
        sum = sum*len(tempList)

for z in range(int(time_p2)):
    if z*(int(time_p2)-z) > int(distance_p2):
        sum_p2+=1

print("Part 1: ",sum)
print("Part 2: ",sum_p2)


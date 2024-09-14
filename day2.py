sum = 0
sum_part2 = 0
filnavn = input("Input file: ")
f = open(filnavn)

for line in f:
    msg = line.strip().split(":")
    ok = True
    id = int(msg[0].strip('Game '))
    red, blue, green = 0, 0, 0
    gems = msg[1].strip().split(";")
    for round in gems:
       hand = round.split(",")
       for gem in hand:
            trial = gem.strip().split(" ")
            if trial[1] == "red" and int(trial[0]) > 12 or trial[1] == "green" and int(trial[0]) > 13 or trial[1] == "blue" and int(trial[0]) > 14:
                ok = False
            if trial[1] == "red" and int(trial[0]) > red:
                red = int(trial[0])
            if trial[1] == "green" and int(trial[0]) > green:
                green = int(trial[0])
            if trial[1] == "blue" and int(trial[0]) > blue:
                blue = int(trial[0])
    power = blue*red*green
    sum_part2+= power

    if(ok):
        sum+=id
print("Part 1 sum: ",sum)
print("Part 2 sum: ",sum_part2)

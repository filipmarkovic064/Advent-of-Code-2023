filnavn = input("Input file: ")
f = open(filnavn)
sum = 0
hash = {}

for x in range (len(f.read().splitlines())):
    hash[x+1] = 1

f.seek(0)
for lines in f:
    l = lines.split("|")
    temp = l[0].split(": ")

    id = int(temp[0].strip("Card "))
    winning = temp[1]
    cards = l[1]
    
    listWinning = winning.strip().split()
    listCards = cards.strip().split()

    cardCount = id
    res = 0
    for card in listCards:
        if card in listWinning:
            res+=1
    for y in range(res):
        cardCount+=1
        hash[cardCount] = int(hash[cardCount])+1*int(hash[id]) 
    
for r in range(1,len(hash)+1):
    sum+=hash[r]
print(sum)

''' part1: 
for lines in f:
    l = lines.split("|")
    temp = l[0].split(": ")
    winning = temp[1]
    cards = l[1]

    listWinning = winning.strip().split()
    listCards = cards.strip().split()
    res = 0
    for card in listCards:
        if card in listWinning:
            if res == 0:
                res = 1
            else:
                res = res * 2
    sum+= res

print(sum)
'''

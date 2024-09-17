letter_map = {"T": "A","J":"B","Q":"C","K":"D","A":"E"} #Lager vårt egen letter map som skal fortelle sort algorithmen hvordan den skal sortere
#Vi setter "A" som er sterkest som sist fordi vi skal sortere det motsatt (så 9 blir sortert før 1)

def classify(hand):
    counts = [hand.count(card) for card in hand]
#Her ser vi på hvor sterk en hånd er, så hvis den har 5 in counts det betyr at den har 5 av det samme kort så det er den sterkeste
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts: 
        return 1
    return 0

def strength(hand): #Definerer hvordan sortering algoritmen skal kjøre
    return (classify(hand), [letter_map.get(card, card) for card in hand])


plays = []
f = open("7.txt")
for line in f:
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key = lambda play: strength(play[0]))

total = 0

for rank, (hand, bid) in enumerate(plays, 1):
    total+= rank * bid
print(total)

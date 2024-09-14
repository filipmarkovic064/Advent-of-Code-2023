sum = 0
filnavn = input("Input file: ")
grid = open(filnavn).read().splitlines() #Åpner input som en 2D-grid
k = set() #Lagrer koordinater av første siffer i en tall
listen = []
for r, row in enumerate(grid): #Index: verdi
    for c, ch in enumerate(row): #ch -> char vi ser på, r -> row# , c -> column#
        if ch != "*":
            continue #Betyr at den er ikke en symbol så vi bryr oss ikke
        set_part2 = set()
        temp_list = []
        for cr in [r-1, r, r+1]: #row av den symbol vi ser på
            for cc in [c-1, c, c+1]: #column (Vi sjekker i 3x3 rundt symbol):
                if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit(): #Sjekker om det er out of bounds eller ikke en tall
                    continue
                while cc > 0 and grid[cr][cc-1].isdigit(): #Vi prøver å gå til venstre for å finne først siffer av den tall sånn at vi kan legge det i k
                    cc -= 1
                set_part2.add((cr, cc))
        for rrr,ccc in set_part2:
            a = ""
            while ccc < len(grid[rrr]) and grid[rrr][ccc].isdigit(): #Så lenge vi kan gå til venstre så skal vi det (for å forme den tall)
                a += grid[rrr][ccc]
                ccc += 1
            temp_list.append(int(a)) 
        if len(temp_list) == 2:
            res = 1
            for x in temp_list:
                res= res*x
            listen.append((int(res)))
''' 
            Måtte kaste vekk ting jeg prøvde og ting fra del1 men til slutt funka det fint 
            ignore
            if len(temp_list)!=2:
                res = 0
                for x in temp_list:
                   res += x
                listen.append((int(res)))
        else:
            for cr in [r-1, r, r+1]: #row av den symbol vi ser på
                for cc in [c-1, c, c+1]: #column (Vi sjekker i 3x3 rundt symbol)
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit(): #Sjekker om det er out of bounds eller ikke en tall
                        continue
                    while cc > 0 and grid[cr][cc-1].isdigit(): #Vi prøver å gå til venstre for å finne først siffer av den tall sånn at vi kan legge det i k
                        cc -= 1
                    k.add((cr, cc))
            for rrr,ccc in k:
                a = ""
                while ccc < len(grid[rrr]) and grid[rrr][ccc].isdigit(): #Så lenge vi kan gå til venstre så skal vi det (for å forme den tall)
                    a += grid[rrr][ccc]
                    ccc += 1
                listen.append(int(a))
'''
sum = 0
for x in listen:
    sum += x
print("Sum: ", sum)


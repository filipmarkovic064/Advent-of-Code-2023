sum = 0
pInput = input("Txt fil med puzzle input: ")
f = open(pInput)

for line in f:
    listen = list(line) 
    tall = []
    for x in listen:
        if(x.isdigit()):
            tall.append(x)
    finNum = int(str(tall[0])+str(tall[-1]))
    sum+= finNum
print(sum)

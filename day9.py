f = open("9.txt")
sum = 0

def lines(array):
    if all(x == 0 for x in array):
        return 0
    deltas = [y - x for x, y in zip(array, array[1:])]

    diff = lines(deltas)
    return array[0] - diff

for line in f:
    nums = list(map(int, line.split()))
    sum+= lines(nums)
print(sum)

filnavn = input("Input file: ")

# Read the file, split the contents by two consecutive newlines ('\n\n'),
# and unpack the result into 'seeds' (the first part) and 'blocks' (the rest).
seeds, *blocks = open(filnavn).read().split("\n\n") 

# Extract the numbers from the 'seeds' line, which appears after the first colon (:).
# This creates a list of integers from the seed values.
seeds = list(map(int, seeds.split(":")[1].split()))

# Loop through each 'block' in 'blocks' (each block corresponds to a chunk of rules).
for block in blocks:
    ranges = []

    # Loop through the lines of the block, skipping the first line (header).
    # Each line contains three integers representing the range and transformation values.
    for line in block.splitlines()[1:]:
        # Convert the line into a list of integers and append to the 'ranges' list.
        ranges.append(list(map(int, line.split())))

    # Create a new list to store updated seed values after applying transformations.
    new = []

    # Loop through each seed value to check which transformation applies.
    for x in seeds:
        # For each seed, check it against each range in the current block.
        for a, b, c in ranges:
            # If the seed 'x' falls within the range [b, b+c), apply the transformation.
            # The new seed becomes 'x - b + a', and we add it to the 'new' list.
            if b <= x < b+c:
                new.append(x - b + a)
                break
        # If no range matches, keep the original seed value.
        else:
            new.append(x)

    # After processing all seeds for the current block, update the seeds with the new list.
    seeds = new

# Finally, print the minimum value from the final list of seed values.
print(min(seeds))



with open('ground_truth.txt', 'r') as ground_file:
    lines = ground_file.readlines()

for i in range(len(lines)):
    line = lines[i]
    tokens = line.split()
    tokens[0] += '.txt'
    lines[i] = ' '.join(tokens)

with open('ground_truth.txt', 'w') as ground_file:
    for line in lines:
        ground_file.write(line + '\n')

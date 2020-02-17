'''
Daniel McCrystal
June 2018

Script to convert data in eTOUR dataset into ground truth format
'''

truths = dict()

while True:
    try:
        ln = input()
        tokens = ln.split()
        key = int(tokens[0][2:-4])
        if key not in truths:
            truths[key] = []

        for target in tokens[1:]:
            truths[key].append(str(target)[:-4] + ".java")

    except EOFError:
        break

keys = list(truths.keys())
keys.sort()

for key in keys:
    print("UC" + str(key), end=".TXT ")
    print(' '.join(truths[key]))

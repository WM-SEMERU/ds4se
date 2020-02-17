'''
Daniel McCrystal
June 2018

Script to convert data in EBT dataset into ground truth format
'''

truths = dict()

req_to_code = open('../EBT/AnswerReq2CC.txt', 'r')
req_to_tests = open('../EBT/AnswersRequirements2Testcases.txt', 'r')


for ln in req_to_code.readlines():
    tokens = ln.split()
    key = "RQ" + str(tokens[0])
    if key not in truths:
        truths[key] = []

    for target in tokens[1:]:
        truths[key].append(str(target) + ".java")


for ln in req_to_tests.readlines():
    tokens = ln.split()
    key = "RQ" + str(tokens[0])
    if key not in truths:
        truths[key] = []

    for target in tokens[1:]:
        truths[key].append("UC" + str(target))


keys = list(truths.keys())
keys.sort()

for key in keys:
    print(key, end=" ")
    print(' '.join(truths[key]))

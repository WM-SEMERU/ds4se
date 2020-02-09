'''
Daniel McCrystal
June 2018

Script to convert data in iTrust dataset into ground truth format
'''

import xml.etree.ElementTree

targets_xml = xml.etree.ElementTree.parse('../target_code.xml').getroot()[1]
answers_xml = xml.etree.ElementTree.parse('../answer_req_code.xml').getroot()[1]


targets = dict()
for target in targets_xml.findall('artifact'):
    identifier = target[0].text
    path = target[1].text

    targets[identifier] = path[23:]

truths = dict()

for link in answers_xml.findall('link'):
    key = link[0].text
    target = link[1].text

    if key not in truths:
        truths[key] = []

    truths[key].append(targets[target])

keys = list(truths.keys())
keys.sort()

for key in keys:
    print(key, end=".txt ")
    print(' '.join(truths[key]))

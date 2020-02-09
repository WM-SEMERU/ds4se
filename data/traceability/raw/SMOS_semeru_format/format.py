'''
Daniel McCrystal
July 2018

Script to convert data in iTrust dataset into ground truth format
'''

import xml.etree.ElementTree

answers_xml = xml.etree.ElementTree.parse('answer_req_code.xml').getroot()[1]

truths = dict()

for link in answers_xml.findall('link'):
    key = link[0].text
    target = link[1].text

    if key not in truths:
        truths[key] = []

    truths[key].append(target + ".java")

keys = list(truths.keys())
keys.sort()

for key in keys:
    print(key, end=".txt ")
    print(' '.join(truths[key]))

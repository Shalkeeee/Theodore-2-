import csv
import random

with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    N = [i for i in range(1024)]
    random.shuffle(N)
    for row in reader:
        scientist_name = row['ScientistName']
        hash_indexes = []
        H = 0
        for i in scientist_name:
            H += N[ord(i) % 1024]
        row['hash'] = str(H % 2048)

with open('scientist_with_hash.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, delimiter='#', fieldnames=['hash', 'ScientistName', 'preparation', 'date',
                                                             'components'])
    writer.writeheader()
    writer.writerows(reader)
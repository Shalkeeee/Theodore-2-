import csv
import random

with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    symparol = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for row in reader:
        N = row['ScientistName'].split()
        row['login'] = f'{N[0]}_{N[1][0]}{N[2][0]}'
        parol = ''
        for i in range(10):
            parol += random.choice(symparol)
        row['parol'] = parol

    with open('scientist_password.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, delimiter='#', fieldnames =['ScientistName', 'preparation', 'date', 'components', 'login', 'parol'])
        writer.writeheader()
        writer.writerows(reader)

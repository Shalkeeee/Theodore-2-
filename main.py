import csv

with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    reader.sort(key=lambda x: x['date'])
    prep = []
    create = []
    chel = False
    for row in reader:
        if row['preparation'] not in prep:
            prep.append(row['preparation'])
            create.append(row)


    print('Разработчиками Аллопуринола были такие люди')
    for row in reader:
        if row['preparation'] == 'Аллопуринол':
            if not chel:
                kto = row['ScientistName']
                chel = True
            print(f'{row["ScientistName"]} - {row["date"]}')
    print('Оригинальный рецепт принадлежит:', f'{kto}')

    with open('scientist_origin.txt', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['ScientistName','preparation','date','components'], delimiter='#')
        writer.writeheader()
        writer.writerows(create)

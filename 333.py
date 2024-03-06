import csv
with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    request = input()
    reader.sort(key=lambda x: x['date'])
    while request != 'эксперимент':
        request = request.split('.')
        request = request[::-1]
        request = '-'.join(request)
        left = 0
        right = len(reader) - 1
        while left <= right:
            center = (left + right) // 2
            if request == reader[center]['date']:
                scientist = reader[center]
                scientist_name = scientist['ScientistName'].split()
                print(f'Ученый {scientist_name[0]} {scientist_name[1][0]}.{scientist_name[2][0]}.'
                      f' создал препарат: {scientist["preparation"]} - {scientist["date"]}')
                break
            if request > reader[center]['date']:
                left = center + 1
            else:
                right = center - 1
        request = input()
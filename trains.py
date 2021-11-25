with open('schedule.txt', encoding='utf-8') as routes:
    with open('town_info.txt', mode='w', encoding='utf-8') as out_file:
        train = input().split()
        writing = [line.rstrip().split() for line in routes]
        result = []
        for i in writing:
            if i[0] == train[0]:
                result.append(i)

        c = []
        for i in result:
            c.append(i[1].split(':'))
        train = train[1].split(':')

        diff = []

        for i in c:
            diff.append(abs(int(i[1]) + int(i[0]) * 60 - int(train[1]) - int(train[0]) * 60))

        mini = diff.index(min(diff))
        out_file.write(str(len(result)) + '\n')
        out_file.write(''.join(result[mini][1]) + '\n')
        out_file.write(str(diff[mini]))

# Richmond 09:15

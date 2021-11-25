import sqlite3

big_data = {
    "height": [],
    "weight": [],
    "clothing": [],
    "habit": []
}
height = []
weight = []
clothing = []
habit = []
profession = input()
con = sqlite3.connect('disguise.db')
cur = con.cursor()
result = cur.execute('''SELECT height, weight, clothing, habit
FROM data
WHERE profession = ?''', (profession,)).fetchall()
for i in result:
    if i[0] not in height:
        height.append(i[0])
    if i[1] not in weight:
        weight.append(i[1])
    if i[2] not in clothing:
        clothing.append(i[2])
    if i[3] not in habit:
        habit.append(i[3])

big_data['height'] = sorted(height)
big_data['weight'] = sorted(weight)
big_data['clothing'] = sorted(clothing)
big_data['habit'] = sorted(habit)
print(big_data)

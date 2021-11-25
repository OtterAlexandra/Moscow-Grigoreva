begin = int(input())
end = int(input())
count = int(input())

before = []
after = []
times = []

for i in range(count):
    portal = int(input())
    if portal < end:
        before.append(portal)
    else:
        after.append(portal)

sorted(before)
sorted(after)

time1 = abs(begin - end)
times.append(time1)

if len(before) > 0:
    time2 = abs(begin - before[0]) + 1 + abs(end - before[-1])
    times.append(time2)
if len(before) > 0 and len(after) != 0:
    time3 = abs(begin - before[0]) + 1 + abs(end - after[0])
    times.append(time3)

print(sorted(times)[0])

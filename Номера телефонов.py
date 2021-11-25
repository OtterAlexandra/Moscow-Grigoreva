telephone = input().replace(' ', '')
p = []

if telephone[0] == '+':
    print(1)
    if telephone[1:].isalnum():
        print(1)
        if '--' not in telephone:
            print(1)
            if telephone.count('(') == 1 and telephone.count(')') == 1:
                print(1)
                if telephone.find('(') < telephone.find(')'):
                    print(telephone)

elif telephone[0] == '8':
    telephone = '+7' + telephone[1:]
    if telephone[1:].isalnum():
        if '--' not in telephone:
            if telephone.count('(') == 1 and telephone.count(')') == 1:
                if telephone.find('(') < telephone.find(')'):
                    print(telephone)

with open('input.txt') as file:
    l = [int(x.strip('\n')) for x in file.readlines()]
    
for i in l:
    for j in l:
        if i + j == 2020:
            print(i * j)
            break
    else:
        continue
    break

for i in l:
    for j in l:
        for k in l:
            if i + j + k == 2020:
                print(i * j * k)
                break
        else:
            continue
        break
    else:
        continue
    break

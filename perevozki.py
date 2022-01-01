wight = input()

if not wight.isnumeric():
    print('некорректный вес')
    exit()
else:
    wight = int(wight)

import math
part = wight / 100

if math.ceil(part) <= 5:
    print(math.ceil(part) * 80)
elif math.ceil(part) <= 10:
    print(math.ceil(part) * 70)
elif math.ceil(part) <= 100:
    print(math.ceil(part) * 65)
else:
    print('не возим')

import sys


if len(sys.argv) < 2:
    print('Передайте сторону квадрата')
    exit()


square_side = sys.argv[1]
if not square_side.isnumeric():
    print('Передайте число в качестве стороны квадрата')
    exit()

perumetr = int(square_side) * 4


print(f'Периметр квадрата со стороной {square_side} равен {perumetr}')

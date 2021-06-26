import sys
from math import pi

r = int(sys.stdin.readline().rstrip())

Euclidean = r*r*pi
Texi = r*r*2

print('%.6f' % Euclidean)
print('%.6f' % Texi)

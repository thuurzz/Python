#Arthur Vinicius Santos Silva RA: 1903365
import math

i = 1
meta = 0
c = 0
d = 0

while i <= 7:
    c = int(input())
    d = d + c
    i = i + 1

    if c >= 100:
        meta = meta + 1

media = math.trunc(d / 7)

print(meta)
print(media)

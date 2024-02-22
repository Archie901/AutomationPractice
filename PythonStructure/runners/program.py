import sys
import main

print(sys.path)

import add_data as ad
import processors as pr

print(ad.Something.sizes)

some1 = pr.func_random(ad.Something.templateNames)

some2 = pr.func_random(ad.Something.QRnames)

print(some1 + "///" + some2)

i = pr.func_add(444, 777)

u = pr.funct_multiply(5, 66)

print(i, u)

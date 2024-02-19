import processors
import add_data

#from processors import adder
#from processors import printer

some1 = processors.func_random(add_data.Something.templateNames)

some2 = processors.func_random(add_data.Something.QRnames)

print(some1 + "///" + some2)

i = processors.func_add(some1, some2)

u = processors.funct_multiply(5, 66)

print(i, u)
from src.binary_functions import *

t1 = convert_dec_to_bin(30)
t2 = convert_dec_to_bin(50)

print(t1)
print(t2)
print()

print(t1)
print(Not16(t2))
print()

t3 = Add16(t1, Not16(t2))
print(t3)
print(convert_bin_to_dec(t3) + 1)
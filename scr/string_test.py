import  sys
m = sys.maxsize
c = 0
print(m)
while m > 0:
    m >>= 1
    c += 1

print(c)
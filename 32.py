digits = range(1,10)

prodsum = 0

for i in xrange(1,9999):
    for j in xrange(1, 10000/i):
        prod = i*j
        digits = str(i)+str(j)+str(prod)
        if sorted(digits) == ["1","2","3","4","5","6","7","8","9"]:
           prodsum += prod
           print i, j, prod
            
print prodsum

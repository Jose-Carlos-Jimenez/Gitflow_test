print("Hola mundo desde la rama develop.")

for x in range(10):
    print("Hola ", x, " desde el release.")


def merryChristmas(n):
    for x in range(n):
        print (' '*(n - (x + 1)), '*'*(2*x +1))

merryChristmas(10)

def ackerman(m, n, s="%s"):
    print (s % ("A(%d,%d)" % (m, n)))
    if m == 0:
        return n + 1
    if n == 0:
        return ackerman(m - 1, 1, s)
    n2 = ackerman(m, n - 1, s % ("A(%d,%%s)" % (m - 1)))
    return ackerman(m - 1, n2, s)

print(ackerman(3,2))
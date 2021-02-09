print("Hola mundo desde la rama develop.")

for x in range(10):
    print("Hola ", x, " desde el release.")


def merryChristmas(n):
    for x in range(n):
        print (' '*(n - (x + 1)), '*'*(2*x +1))

merryChristmas(10)
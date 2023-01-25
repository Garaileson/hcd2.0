def hcf(a, b):

    if b == 0:
        return a
    else:
        return hcf(b, a % b)


print("Брой членове на редицата: = ")
n = int(input())
if n <= 1:
    print("Грешка  :( ")
elif n == 2:
    a = int(input())
    b = int(input())
    m = hcf(a, b)
    print("gcd на a и b:", m)
else:
    a = int(input())
    b = int(input())
    for i in range(n-2):
        c = int(input())
    k = hcf(hcf(a, b), c)
    print("gcd на редицата е:", end="")
    print(k)
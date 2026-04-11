n = int(input(""))
z = list(map(int, input("").split()))

expected = n * (n + 1) // 2
actual = sum(z)

print(expected - actual)
#Find d
b10, b1, n = map(int, input("b10 , b1 , n; ").split(","))
print("d", (b10 - b1) / (n - 1) )
#caculate (bn)
b1, n, d = map(int, input(" b1 , n , d: ").split(","))
print("bn", b1 + (n - 1) * d)


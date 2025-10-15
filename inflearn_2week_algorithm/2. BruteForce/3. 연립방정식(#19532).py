A, B, C, D, E, F = map(int, input().split())
det = A * E - B * D
X = (C * E - B * F) // det
Y = (A * F - C * D) // det
print(X, Y)

a, b, c, d, e, f = map(int, input().split())
det = a * e - b * d
detv1 = c * e - b * f
detv2 = a * f - c * d

print(detv1 // det, detv2 // det)

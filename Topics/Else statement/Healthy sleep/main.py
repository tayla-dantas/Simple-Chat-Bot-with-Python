# A, B, H, where A is always less than or equal to B.
# ideal to sleep a minimum of A hours daily but not to exceed B hours.
a = int(input())
b = int(input())
h = int(input())

print("Normal" if (a <= h <= b) else ("Excess" if (h > b) else "Deficiency"))
# if h >= a and h <= b normal
# if h > b excess
# if h < a deficiency
# ("Deficiency," "Excess," "Normal")

initial = int(input())
final = int(input())
half_life = 12
half_life_count = 0


while not initial <= final:
    initial = initial // 2
    half_life_count += 1

print(half_life_count * half_life)
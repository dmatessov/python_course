import sys

shot_count = int(sys.stdin.readline())
i = 0
list_in_float = []
total_score = 0
while i < shot_count:
    in_str = str(sys.stdin.readline())
    list_in_str = in_str.split(" ")
    R = (float(list_in_str[0])**2 + float(list_in_str[1])**2 )**0.5
    if R > 10:
        score = 0
    else:
        score = int(10 - (R // 1))
    total_score = total_score + score
    i += 1
print(total_score)
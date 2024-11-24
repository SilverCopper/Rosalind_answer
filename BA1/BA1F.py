with open("rosalind_ba1f.txt") as fp:
    seq = fp.read().strip()

skew_statistic = [0]

skew_count = 0

for i in seq :
    if i == "C":
        skew_count -= 1
    elif i == "G":
        skew_count += 1
    
    skew_statistic.append(skew_count)

min_index = [i for i, x in enumerate(skew_statistic) if x == min(skew_statistic)]

for index in min_index:
    print(index, end= " ")


    
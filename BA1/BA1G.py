with open("rosalind_ba1g.txt") as fp:
    result = fp.readlines()
    seq1 = result[0].strip()
    seq2 = result[1].strip()

compare_result = [i for i in range(len(seq1)) if seq1[i] != seq2[i]]

print(len(compare_result))
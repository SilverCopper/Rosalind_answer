def find_clumps(genome, k, L, t):
    patterns = set()
    kmer_count = {}
    window = genome[:L]
    
    for i in range(L - k + 1):
        kmer = window[i:i + k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1

    for kmer, count in kmer_count.items():
        if count >= t:
            patterns.add(kmer)
    
    for i in range(1, len(genome) - L + 1):
        prev_kmer = genome[i - 1:i - 1 + k]
        kmer_count[prev_kmer] -= 1
        new_kmer = genome[i + L - k:i + L]
        if new_kmer in kmer_count:
            kmer_count[new_kmer] += 1
        else:
            kmer_count[new_kmer] = 1
        if kmer_count[new_kmer] >= t:
            patterns.add(new_kmer)

    return patterns

with open("rosalind_ba1e.txt") as fp:
    result = fp.readlines()
    seq = result[0].strip()
    k = int(result[1].split(" ")[0])
    L = int(result[1].split(" ")[1])
    t = int(result[1].split(" ")[2])
    result = find_clumps(seq, k, L, t)
    for i in result:
        print(i, end=" ")
    
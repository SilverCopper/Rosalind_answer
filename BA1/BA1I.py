def Hamming_distance(seq1, seq2):
    compare_result = len([i for i in range(len(seq1)) if seq1[i] != seq2[i]])
    return compare_result

def find_all_kmer(seq, k):
    kmer_list = []
    for i in range(len(seq) - k + 1):
        temp = seq[i:i+k]
        if temp not in kmer_list:
            kmer_list.append(temp)
    return kmer_list

def find_pair(pattern ,seq, threshold):
    k = len(pattern)
    count_result = 0
    for i in range(len(seq) - k + 1):
        if Hamming_distance(pattern, seq[i:i+k]) <= threshold:
            count_result += 1
    return count_result

def main():
    with open("rosalind_ba1i.txt") as fp:
        result = fp.readlines() 
        seq = result[0].strip()
        k = int(result[1].split(" ")[0])
        d = int(result[1].split(" ")[1].strip())
    
    patterns_count = []
    patterns = find_all_kmer(seq, k)
    for pattern in patterns:
        patterns_count.append(find_pair(pattern, seq, d))
    
    max_index = [i for i in range(len(patterns_count)) if patterns_count[i] == max(patterns_count)]
    
    for index in max_index:
        print(patterns[index], end=" ")
        
if __name__ == "__main__":
    main()
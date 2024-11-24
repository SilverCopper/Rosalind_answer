def create_kmer(k):
    bases = ["A", "T", "C", "G"]
    if k==2:
        double_mer = []    
        for base1 in bases:
            for base2 in bases:
                double_mer.append(base1 + base2)
        
        return double_mer
    
    result_mer = []
    if k>2:
        temp_mer = create_kmer(k-1)
        for base1 in temp_mer:
            for base2 in bases:
                result_mer.append(base1+base2)
        
        return result_mer
    
def Hamming_distance(seq1, seq2):
    compare_result = len([i for i in range(len(seq1)) if seq1[i] != seq2[i]])
    return compare_result

def main():
    with open("rosalind_ba1n.txt") as fp:
        result = fp.readlines()
        kmer = result[0].strip()
        threshold = int(result[1].strip())
        
    k = len(kmer)
    kmer_list = create_kmer(k)
    kmer_result = []
    for i in kmer_list:
        if Hamming_distance(kmer, i) <= threshold:
            kmer_result.append(i)
    
    for j in kmer_result:
        print(j)
    
if __name__ == "__main__":
    main()
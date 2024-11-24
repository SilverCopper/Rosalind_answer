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
def kmer_count(kmer, seq):
    count = 0
    for i in range(len(seq) - len(kmer) + 1):
        if kmer == seq[i:i+len(kmer)]:
            count += 1
    return count
    
    
def main():
    with open("rosalind_ba1k.txt") as fp:
        result = fp.readlines()
        seq = result[0].strip()
        num = int(result[1].strip())

    kmer_list = create_kmer(num)
    kmer_list.sort()
    kmer_list_count = []
    print(kmer_list)
    for kmer in kmer_list:
        kmer_list_count.append(kmer_count(kmer, seq))
    for i in kmer_list_count:
        print(i, end=" ")
    
if __name__ == "__main__":
    main()
        
        




    

        
        
    
        
    
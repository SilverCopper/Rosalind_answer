def Hamming_distance(seq1, seq2):
    compare_result = len([i for i in range(len(seq1)) if seq1[i] != seq2[i]])
    return compare_result

def count_mismatch(pattern, seq, threshold):
    index_result = []
    for i in range(len(seq) - len(pattern) + 1):
        if Hamming_distance(pattern, seq[i:i+len(pattern)]) <= threshold:
            index_result.append(i)
    
    return index_result

def main():
    with open("rosalind_ba1h.txt") as fp:
        result = fp.readlines() 
        pattern = result[0].strip()
        seq = result[1].strip()
        threshold = int(result[2].strip())
        
    result_list = count_mismatch(pattern, seq, threshold)
    
    for i in result_list:
        print(i, end=" ")
    
if __name__ == "__main__":
    main()
def calculate(seq):
    dict = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }
    trans_seq = seq[::-1]
    sum = 0
    for i in range(len(trans_seq)):
        sum += 4**i * dict[trans_seq[i]]
    
    return sum

def main():
    with open('rosalind_ba1l.txt') as fp:
        seq = fp.read().strip()
    print(calculate(seq))
    
if __name__ == "__main__":
    main()
        
        
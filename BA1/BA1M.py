def trans_num_to_seq(num, seq_length):
    dict = {
        0: "A",
        1: "C",
        2: "G",
        3: "T"
    }
    result = []
    while num // 4 != 0:
        temp = num % 4
        result.append(temp)
        num = num // 4
    
    result.append(num)
    result.reverse()
    
    seq = "".join([dict[i] for i in result])
    
    seq = "A" * (seq_length - len(result)) + seq
    
    return seq

def main():
    with open("rosalind_ba1m.txt") as fp:
        result = fp.readlines()
        num = int(result[0].strip())
        seq_length = int(result[1].strip())
    print(trans_num_to_seq(num, seq_length))
    
if __name__ == "__main__":
    main()


        
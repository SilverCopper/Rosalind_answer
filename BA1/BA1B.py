text = input("text:")
k = int(input("number of k:"))
kmer_list = []
kmer_list_count = []

for i in range(len(text) - k + 1):
    pattern_temp = text[i:i+k]
    if pattern_temp not in kmer_list:
        kmer_list.append(pattern_temp)

for pattern in kmer_list:
    kmer_list_count.append(text.count(pattern))

index = [i for i in range(len(kmer_list_count)) if kmer_list_count[i] == max(kmer_list_count)]

for i in index:
    print(kmer_list[i])
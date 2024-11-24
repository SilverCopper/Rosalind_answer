with open("rosalind_ba1d.txt") as fp:
    result = fp.readlines()

pattern = result[0].strip()
text = result[1].strip()

index_list = []
for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        index_list.append(i)

for index in index_list:
    print(index,end=" ")
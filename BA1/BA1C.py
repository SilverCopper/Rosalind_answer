trans_dict = {
    "A":"T",
    "C":"G",
    "T":"A",
    "G":"C"
}

with open("rosalind_ba1c.txt") as fp:
    text = fp.read().strip()

trans_text = text[::-1]

trans_text_list = []

for i in trans_text:
    trans_text_list.append(trans_dict[i])
    
trans_text_result = "".join(trans_text_list)

print(trans_text_result)
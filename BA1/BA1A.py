pattern = input("pattern:")
text = input("text:")

count = 0
for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        count += 1

print(f"pattern appears {count} times")
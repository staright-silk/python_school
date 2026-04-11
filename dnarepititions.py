s = input()

max_len = 1   
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        count = 1
    if count > max_len:
        max_len = count

print(max_len)

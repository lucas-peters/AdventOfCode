import os
print(os.getcwd())
left = []
right = []

#reading in input text into separate arrays
with open('input.txt', 'r') as f:
    while True:
        line = f.readline()
        if not len(line):                      # readline returns an empty string with no newline for EOF
            break
        
        line = line.rstrip().split()
        left.append(int(line[0]))
        right.append(int(line[1]))
        
# sort strings
left.sort()
right.sort()
# take absolute value of difference and add to sum
sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)

hash_map = {}
for num in right:
    if num not in hash_map:
        hash_map[num] = 1
    else:
        hash_map[num] += 1

total_score = 0
for num in left:
    if num in hash_map:
        total_score += num * hash_map[num]

print(total_score)
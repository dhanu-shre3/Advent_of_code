with open("Day1/Day1_input.txt", "r") as file:
    input_data = file.readlines()

#attribute error because readlines returns a list of strings (lines in a file). And a list doesnt have a strip() method

left = []
right = []

for line in input_data:
    line = line.strip() #removes leading or traling whitspace
    l, r = map(int, line.split())
    left.append(l)
    right.append(r)

#print("left:", left)
#print("right:", right)    

sorted_left = sorted(left)
sorted_right = sorted(right)

total_distance = 0

for i in range(len(sorted_left)):
    difference = abs(sorted_left[i] - sorted_right[i])

    total_distance += difference

print(f"total distance: {total_distance}")    

#part2

from collections import Counter

right_counts = Counter(right)

similarity_score = 0

for i in left:
    count_in_right = right_counts.get(i,0)
    similarity_score += i * count_in_right


print(similarity_score)    


l2 = [1, "Jay", 0.6, [4,56,8,9],[56,89,1,2]]
numbers1 = l2[3]
numbers2 = l2[4]
# numbers1.sort()
# numbers2.sort()
numbers3 = []
count = 0

for number in numbers1:
  numbers3.append(numbers2[count] * numbers1[count])
  count = count+1
   
print(numbers3)
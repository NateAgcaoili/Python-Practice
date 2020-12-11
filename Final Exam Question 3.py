### CODE FOR STAT EXAM NUMBER 3 ###

### Initalizing Lists ###
nums = [37,39,32,20,22,30,25,37,21,24,29,29,26,23,22]
nums = sorted(nums)
mean_nums = []
square = []

### A ###
print("A: " + str(round(sum(nums) / 15,2)))

### B ###
for num in nums:
    mean_nums.append(round(num-27.73, 2))
print("B: " + str(mean_nums))

### C ###
for num in mean_nums:
    square.append(round(num**2, 3))
print("C: " + str(square))

### D ###
summy = sum(square)
print("D: " + str(summy))

### E ###
summy_divided = summy / 14
print("E: " + str(summy_divided))

### F ###
sqrt = summy_divided ** 0.5
print("F: " + str(sqrt))

### G ###
print("G: " + str(nums[len(nums)//2]))
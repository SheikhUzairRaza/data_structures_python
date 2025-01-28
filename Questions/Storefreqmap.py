nums = [5,6,7,7,9,1]
freq_map = dict()
for i in nums:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1
print(freq_map)

# OR 
nums = [5,6,7,7,9,1]
freq_map = dict()
for i in range(len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(freq_map)
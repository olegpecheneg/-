def max_min_sum(nums):      
    for i in range(len(nums)):
        minimum = i        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimum]:
                minimum = j
        nums[minimum], nums[i] = nums[i], nums[minimum]
        
    half = len(nums) // 2
    a = nums[:half]
    b = nums[half:]
    l = []
    
    for i in range(0, half):
        l.append(a[i] + b[- 1 - i])
        
    return l[0]
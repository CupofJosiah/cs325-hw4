def max_independent_set(nums):
    if all(num < 0 for num in nums):
        return []
    incl, excl = [], []
    for num in nums:
        new_incl = excl + [num]
        excl = max(incl, excl, key=sum)
        incl = new_incl
    return incl if sum(incl) >= sum(excl) else excl


print(max_independent_set([7, 2, 5, 12, 6]))

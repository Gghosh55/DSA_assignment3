def findMissingRanges(nums, lower, upper):
    result = []

    def addRange(start, end):
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + '->' + str(end))

    prev = lower - 1

    for num in nums + [upper + 1]:
        if num - prev >= 2:
            addRange(prev + 1, num - 1)
        prev = num

    return result
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))

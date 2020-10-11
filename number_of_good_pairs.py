def goodPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count


if __name__ == "__main__":
    nums = list(map(int, input().split()))

    print(goodPairs(nums))

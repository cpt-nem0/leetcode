def runningSum(nums):
        r_sum = [nums[0]]
        for i in range(1, len(nums)):
            r_sum.append(nums[i]+r_sum[i-1])
        return r_sum

if __name__ == "__main__":
    nums = list(map(int,input().split()))
    print(runningSum(nums))
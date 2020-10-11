def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result


if __name__ == "__main__":
    nums = list(map(int, input('> ').split()))
    n = int(input('> '))

    print(shuffle(nums, n))

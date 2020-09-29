def kidsWithCandies(candies, extraCandies):
    maxCandies = max(candies)
    result = []
    for c in candies:
        if c + extraCandies >= maxCandies:
            result.append(True)
        else:
            result.append(False)
    return result


if __name__ == "__main__":
    candies = list(map(int, input('> ').split()))
    extraCandies = int(input('> '))

    print(kidsWithCandies(candies, extraCandies))
def Add(numbers: str) -> int:

    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")
    nums = numbers.split(",")
    result = 0

    for n in nums:

        if int(n) < 0:
            raise ValueError()
        else:
            result += int(n)

    return result
def one(file_path):
        count = 0
        max1 = 0
        with open(file_path) as f:
            nums = f.read().splitlines()
        for num in nums:
            if num == '':
                if count > max1:
                    max1 = count
                count = 0
            else:
                count += int(num)
        return max1


def two(file_path):
    count = 0
    calories = []
    with open(file_path) as f:
        nums = f.read().splitlines()
    for num in nums:
        if num == '':
            calories.append(int(count))
            count = 0
        else:
            count += int(num)
    return sorted(calories)[-3:]


if __name__ == '__main__':
    print(one("in.txt"))
    print(two("in.txt"))

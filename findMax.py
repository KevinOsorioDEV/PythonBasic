def find_max(nums):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


if __name__ == "__main__":
    print(find_max([1,2,3,40,5]))
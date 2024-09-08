

def calculate_average(nums):
    sum = 0
    for num in nums:
        sum += num
    average = sum  / len(nums)
    return average

numbers  = [4,7,2,9,3]

result = calculate_average(numbers)
print(f"the average for {numbers} is: {result}")


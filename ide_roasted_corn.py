import random

#1
numbers = []
for num in range(10):
    numbers.append(random.randrange(1,51))
print(numbers)

#2
def length(nums : list):
    count = 0
    for num in nums:
        count += 1
    return count
print(length([1,2,3,4,5,6]))

#3
def sum_even_positions(nums : list):
        sum = 0
        for count in range(length(nums)):
            if count % 2 == 0:
                sum += nums[count]
        return sum
print(sum_even_positions([1,2,3,4,5,6]))

#4
def sum_odd_positions(nums : list):
        sum = 0
        for count in range(length(nums)):
            if count % 2 != 0:
                sum += nums[count]
        return sum
print(sum_odd_positions([1,2,3,4,5,6]))

#5
def multiply_every_third(nums: list):
    answer = 1
    for count in range(0,length(nums),3):
            answer *= nums[count]
    return answer
print(multiply_every_third([1, 2, 3, 4, 5, 6]))

#6
def average(nums : list):
    sum = 0
    for count in range(length(nums)):
        sum += nums[count]
    average = sum / length(nums)
    return average
print(average([1, 2, 3, 4, 5, 6]))

#7
def largest(nums : list):
    biggest = nums[0]
    for num in nums:
        if num > biggest:
            biggest = num
    return biggest
print(largest([1, 2, 3, 4, 5, 6]))

#8
def smallest(nums : list):
    least = nums[0]
    for num in nums:
        if num < least:
            least = num
    return least
print(smallest([1, 2, 3, 4, 5, 6]))

#9
def strings_count(words : list):
        for word in words:
            if length(word) >= 2 and word[0] == word[-1]:
                    print(word)
strings_count(["hi", "apple", "eba", "eniife"])

#10
num_list = [number for number in range(1,16)]
print(num_list)

#11
duplicate = [number for number in range(1,16)]
for num in num_list:
    duplicate.append(num)
duplicate.sort()
print(duplicate)

#12
def remove_duplicate(nums : list):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique
print(remove_duplicate(duplicate))

#13
def sum_every_third_element(nums : list):
    sum = 0
    for count in range(length(nums)):
        if (count + 1) % 3 == 0:
            sum += nums[count]
    return sum
print(sum_every_third_element([1, 2, 3, 4, 5, 6]))

#14
def sum_specific_element(nums : list):
    sum = nums[0] + nums[-1]
    if length(nums) % 2 != 0:
        middle = nums[Math.ceil(length(nums) / 2)]
        sum += middle
    else:
        middle = (nums[length(nums) // 2] + nums[(length(nums) // 2)-1]) / 2
        sum += middle
    return sum
print(sum_specific_element([1, 2, 3, 4, 5, 6]))

#15
numbers = set()
for _ in range(10):
    num = input("Enter a number: ")
    numbers.add(num)
print(numbers)

#16
def sum_collection(nums : set):
        sum = 0
        for num in nums:
            sum += num
        return sum
print(sum_collection({1, 2, 3, 4, 5, 6}))

#17
def remove_item(nums : set, number):
    if number in nums:
        nums.remove(number)
        return nums
print(remove_item({1, 2, 3, 4, 5, 6},7))

#18
def find_intersection(nums : set, numbers : set):
        output = set()
        for num in nums:
            if num in numbers:
                output.add(num)
        return output
print(find_intersection({1, 2, 3, 4, 5, 6}, {1, 2, 3}))

#19
def join_sets(nums : set, numbers : set):
    output = nums.union(numbers)
    return output
print(join_sets({1, 2, 3, 4, 5, 6}, {7, 2, 3}))

#20
def check(nums : set, numbers : set):
    output = []
    for nums in numbers:
        if nums in numbers:
            output.append(True)
        else:
            output.append(False)
    if output.count(False) >= 1:
        return False
    else:
        return True
print(check({1, 2, 3}, {1, 2, 3, 4, 5, 6}))

#21
def remove_elements(nums : set, numbers : set):
    nums.clear()

nums = {1,2,3}
remove_elements(nums, {1, 2, 3, 4, 5, 6})
print(nums)

#22
def max_and_min(nums : set, numbers : set):
    return max(numbers), min(numbers)
print(max_and_min({1,2,3},{1, 2, 3, 4, 5, 6}))

#23
def length_of_set(nums : set):
    count = 0
    for num in nums:
        count += 1
    return count
print(length_of_set({1, 2, 3}))

#24
empty_tuple = ()

#25
empty_tuple+=tuple(num for num in range(1,21))
print(empty_tuple)

#26
def sum_odd_positions(numbers : tuple):
    sum = 0
    for count in range(len(numbers)):
        if count % 2 != 0:
            sum += numbers[count]
    return sum
print(sum_odd_positions((1, 2, 3)))

#27
def sum_even_positions(numbers : tuple):
    sum = 0
    for count in range(len(numbers)):
        if count % 2 == 0:
            sum += numbers[count]
    return sum
print(sum_even_positions((1, 2, 3)))

#28
def sum_max_and_min(numbers : tuple):
    return max(numbers) + min(numbers)
numbers = (1,2,3)
print(sum_max_and_min(numbers))

#29
numbers = (1,2,3,4,5,6,7,8,9)
first,second,third,fourth,fifth,*others = numbers
print(first,second,third,fourth,fifth)

#30
empty_dictionary = {}

#31
for _ in range(10):
    name = input("Enter a name: ")
    age = input("Enter age: ")
    if age.isdigit():
        if int(age) > 0:
            empty_dictionary[name] = int(age)
print(empty_dictionary)

#32
keys = [key for key in empty_dictionary]
keys.sort()
print(keys)

#33
values = [value for key,value in empty_dictionary.items()]
values.sort()
print(values)

#34
ages = []
for key,value in empty_dictionary.items():
    ages.append(value)
print(sum(ages))


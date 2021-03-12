nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Example 1
# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# how the above list looks in List Comprehension
my_list = [n for n in nums]
print(my_list)


# Example 2
# I want 'n*n' for each n in the nums

list2 = []
for n in nums:
    list2.append(n*n)
print(list2)

# how the above list looks in List Comprehension
list2 = [n*n for n in nums]
print(list2)

# Example 3
list3 = []
for n in nums:
    if n % 2 == 0:
        list3.append(n)
print(list3)

list3 = [n for n in nums if n % 2 == 0]
print(list3)
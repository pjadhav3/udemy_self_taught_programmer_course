'''
Assignment 11: Algorithm challenge

Given a non-empty list of integers, every element appears twice except for one. Find that single one.
'''

import time


#approach 1: using dictinaries

def find_single_element_dict(nums):

    dict_nums = {}

   

    for num in nums:

        if num in dict_nums:

            dict_nums[num] += 1

        else:

            dict_nums[num] = 1

       

    for key,value in dict_nums.items():

        if value==1:

            return key

       


start = time.time()

print(find_single_element_dict([1,1,2,3,3,4,5,5,4]))

end= time.time()

print("time : {}".format(end-start))


#approach 2: using list

def find_single_element_list(nums):

    items = []

   

    for num in nums:

        if num in items:

            items.remove(num)

        else:

            items.append(num)

       

    return items[0]


start = time.time()

print(find_single_element_list([1,1,2,3,3,4,5,5,4]))

end= time.time()

print("time : {}".format(end-start))
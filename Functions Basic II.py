# # 1. Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element). Example: countdown(5) should return [5,4,3,2,1,0]
# def countdown(num):
#     newOutput=[]
#     while num >=0:
#         newOutput.append(num)
#         num-=1
#     return newOutput
# print(countdown(5))


# # 2. Create a function that will recieve a list with two numbers. Print the first value and return the second. Example: print_and_return ([1,2]) should print 1 and return 2
# def print_and_return(arr):
#     print (arr[0])
#     return arr[1]
# print_and_return([1,2])


# # 3. Create a function that accepts a list and returns the sum of the first list plus the list's length. Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1+length: 5)
# def first_plus_length(arr):
#     a=arr[0]
#     b=len(arr)
#     return a+b
# print(first_plus_length([1,2,3,4,5]))


# # 4. Write a function that accepts a list and createsa  new list containting only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False. Example: values_greater_than_second ([5,2,3,2,1,4]) should print 3 and return [5,3,4]. and _seconds[3] should return False
# def values_greater_than_second(arr):
#     for i in range(len(arr)):
#         if arr[i] >= i[2]:
#             arr.pop(i)
#             arr[i]+=1
#         print(len(arr))
#         if len(arr)<2:
#             return False
# values_greater_than_second([5,2,3,2,1,4])
# COME BACK TO DEEES


# # 5. Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value. Example: length_and_value(6,2) should return [2,2,2,2,2,2]
# def length_and_value(set):
#     size= set[1]
#     repeat = set[0]
#     print(f"{size},"*repeat)
# length_and_value((6,2))

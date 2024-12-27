# import numpy as num
#
my_list = [1, 2, 3, 4, 5, 6]

#
# # temp_list = []
# # for i in list:
# #     temp_list.append(i*2)
# # print(temp_list)
# #
# def double_item(num):
#     return num ** 2


#
#  # Map() function
# double_list = list(map(def_double_item, list))

# 1. Takes each item from the list
# execute th function on it
# return same number of elements(list)

double_list = list(map(lambda num: num ** 2,my_list))
print(double_list)



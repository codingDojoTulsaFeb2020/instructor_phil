#1

# python
# var my_number = 42;
# print(my_number)










#2

# my_list = [41, 23]
# my_second_list = [
#   42,
#   24
# ]
# print(my_list[1] + my_second_list[2])









#3

# my_list = [41, 23]
# my_second_list = [
#   42,
#   24
# ]

# try:
#   print(my_list[1] + my_second_list[2])
# except IndexError:
#   print(my_list[0] + my_second_list[1])
# except KeyError:
#   print('dictonary')










#4

# i,j = (1,2), [3,4]
# print(i)
# print(j)
# i[1] = 42
# j[0] = 42
# print(i[1] + j[1])














#5

# num = 1,2,3
# print(num)
# num1, num2, num3 = 1,3,5
# print(num2)
# print(type(num2))











#6

# i,j = 1,2,3
# print(j)
# (i,j) = (1,2,3)
# print(j)











#7

# our_list = ['Martin', 'Michael']
# for val in enumerate(our_list):
#   print(val)














#8

# our_list = ['Martin', 'Michael']
# for idx,value in enumerate(our_list):
#   print(value, idx)













#9

# name = {"sw":"Sara Wong", "mp":"Martin Puryear"}
# print(name['sw'])
# for key in name:
#   print(key)
#   print(name[key])











#10

name = {"sw":"Sara Wong", "mp":"Martin Puryear"}
for key, value in name.items():
  print(key, value)

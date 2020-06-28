"""
27. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""
num=[1,2,3,4,5,6,7]
num1=[2,3,8,9,0,10]
num[-1:]=num1
print(num)
#32.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
import random as r
nums=[r.randint(1,15)for y in range  (20)]
print(nums)
print(set(nums))
nums1=[]
#=======================================================
for y in range (len(nums)):
    for d in range(len(nums)-1,y,-1):
        if nums[y]==nums[d]:
            nums1.append(nums[y])
print(nums1)
for y in nums1:
    for d in nums:
        if y==d:
            nums.remove(y)
print(nums)
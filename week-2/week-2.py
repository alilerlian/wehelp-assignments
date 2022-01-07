#要求1
def calculate(min,max):
  x=0
  for i in range(min,max+1):
    x+=i
  print(x)

calculate(1,3)
calculate(4,8)

#要求2
def avg(data):
  data_list=data["employees"]
  x=0
  for i in range(0,data["count"]):
    x+=data_list[i]["salary"]
    average=x/data["count"]
  print(average)

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) 

#要求3
def maxProduct(nums):
  n=len(nums)
  nlist=[]
  for i in range(0,n):
    for j in range(i,n-1):
      x=nums[i]*nums[j+1]
      nlist.append(x)
  print(max(nlist))

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

#要求4
def twoSum(nums, target):
  result=[]
  n=len(nums)
  for i in range(0,n):
    if target-nums[i] in nums:
      result.append(nums.index(nums[i]))
  return result

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#要求5
def maxZeros(nums):
  not_zero=[]
  n=len(nums)
  if nums[0]==0:
    not_zero.append(-1)
  for i in range(0,n):
    if nums[i]!=0:
      not_zero.append(i)
  if nums[n-1]==0:
    not_zero.append(n)
  gap=[]
  for j in range(1,len(not_zero)):
    gap.append(not_zero[j]-not_zero[j-1])
  print(max(gap)-1)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
#while循环
condition = 0
while condition <10:
	print(condition)
	condition = condition + 1

print("*************************************")
#for循环
examplelist = [1,2,3,4,5,6,44,22,56,88,22]
for i in examplelist:
	print(i)
	print("inner of for")
print("out of for")

print("******************************************")
#Range函数
for i in range(10,101,10):
	print(i)

print("******************************************")
#
dic = {}
dic['lan'] = "python"
dic['version'] = 3.6
dic['platform'] = 64
for key in dic:
	print(key,dic[key])
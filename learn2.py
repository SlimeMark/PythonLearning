#for循环
flightsim=['FSX','P3D','MFS2020','X-Plane']
for sim in flightsim:
	print(sim)
	#for循环格式：for 变量名 in 列表名
	print(sim+" "+"is great")
print("Now choose yours!")
for value in range(1,6):
	print(value)#显示数字1~5，格式：for 变量名 in range(起始值,末尾值+1)
print(list(range(1,6)))#使用list()将for循环的数字直接转为列表
squares=[]
for sqvalue in range(1,11):#时刻记得冒号
	sqvalue1=sqvalue**2
	squares.append(sqvalue1)
print(squares)
#简化↓
squares2=[]
for sqvalue2 in range(1,11):
	squares2.append(sqvalue2**2)
print(squares2)
#找出数字列表中的各种值
print(min(squares2))
print(max(squares2))
print(sum(squares2))
#进一步简化
squares3=[sqvalue3**2 for sqvalue3 in range(1,11)]#格式：列表名=[表达式 for 变量名 in range()]
print (squares3)
#切片
print(flightsim[0:2])#显示该列表中第一个至第二个元素
print(flightsim[:2])#从头至第二个元素
print(flightsim[1:])#从第二至最后一个元素
print(flightsim[-2:])#最后两个元素
#按顺序输出切片
for simulator in flightsim[0:2]:
	print (simulator)
#复制列表
flightsimfamous=flightsim[:]#必须使用切片
print(flightsim)
print(flightsimfamous)
#元组
#元组是元素不可变的列表
siminstalled=('X-Plane','DCS')
print(siminstalled[0])#输出该元组中第一个数据
print(siminstalled[1])#输出该元组中第二个数据
#同样的，元组也可以使用和列表相同的for循环来依次输出所有数据
#元组无法修改，但可以赋值
print(siminstalled)
siminstalled=('X-Plane','FSX')
print(siminstalled)
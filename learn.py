#pre
message="hello world"
note="!"
message2='hello world '
num=114514

print (message)
print(message.title())#title
print(message.upper())#caps
print(message.lower())#lower
print(message+note)#合并字符串
print(message2+note)#与下一条的对比
print(message2.rstrip()+note)#删除空格，避免字符串开头或末尾的空格造成问题
#lstrip()删除开头空格,strip()删除两端空格
#出现撇号（'）时字符串仅可使用双引号
print(str(num))#str()可将数作为字符串

#列表
flightsim=['FSX','P3D','MFS2020','X-Plane']
#使用print(列表名称[第几项(从零起)])输出列表元素
print(flightsim[2])
#将索引指定为-1可直接输出最后一个元素
print(flightsim[-1])
#列表内的元素也可与其它字符串相加
print(flightsim[-1]+" "+"11")
#使用“列表名称[第几项(从零起)]=内容”可修改元素
flightsim[0]="FS9"
print(flightsim)
print(flightsim[0])
#使用“列表名称.append()”在该列表末尾添加一个元素
flightsim.append("FlightGear")
print(flightsim)
print(flightsim[-1])
#使用“列表名称.insert(位置，内容)”在该列表中的指定位置添加一个元素
flightsim.insert(0,"IF")
print(flightsim)
print(flightsim[0])
#使用“del 列表名称[第几项]”删除一个元素
del flightsim[0]
print(flightsim)
#pop()可以删除末尾或指定位置的值并弹出它
popsim=flightsim.pop(-1)
print(flightsim)
print(popsim)
#.remove()同理，只是括号内不是元素位置而是其内容，也可以弹出该元素
removed="MFS2020"
flightsim.remove(removed)
print(flightsim)
print(removed+" "+"is too expensive")

#OK LET'S PRACTICE!
sim=[]
while 1:
	sim.append(input())
	print(sim)


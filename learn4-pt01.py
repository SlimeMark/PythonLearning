aircraft_0={'MTOW':'114514','LW':'1919','FUEL':'810'}
#访问字典中的值
print(aircraft_0['MTOW']+"kg")
fob=aircraft_0['FUEL']
print("FOB"+"="+fob+"kg")
print(aircraft_0)
aircraft_0['ZFW']="1919810"
print(aircraft_0)
print("FOB"+"="+aircraft_0['FUEL']+"kg")
aircraft_0['FUEL']="800"
print("FOB"+"="+aircraft_0['FUEL']+"kg")
print(aircraft_0)
del aircraft_0['LW']
print(aircraft_0)
for key,value in aircraft_0.items():
	print(key)
	print(value)
for key in aircraft_0.keys():
	print(key)
if 'LW' not in aircraft_0.keys():
	print("NO LW DATA")
for key in sorted(aircraft_0.keys()):
	print(key)
for value in aircraft_0.values():
	print(value)
for value in sorted(aircraft_0.values()):
	print(value)

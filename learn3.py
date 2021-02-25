sims=['fsx','P3D','msfs']
for sim in sims:
	if sim=='fsx':
		print(sim.upper())
	else:
		print(sim.title())

installed_sims=['X-Plane','P3D']

installed_sim = 'X-Plane'
if installed_sim != 'FSX':
	print("Not Found")



data=3
if data != 27:
	print("ERROR")


if data !=27 and data<=2:
	print("ERROR")
elif data !=27 and data>2:
	print("FAULT")


if installed_sim not in sims:
	print("WTF")
else:
	print("installed")


if 1>2:
	print("That's impossible.")
else:
	print("true")


for sim in sims:
	if sim!='fsx':
		print("Not FSX")
	else:
		print("FSX")


simslist=['fsx','P3D','msfs','X-Plane']
installed_sims=['P3D','X-Plane']

for installedsim in installed_sims:
	if installed_sims in simslist:
		print("installed")
	else:
		print("1")
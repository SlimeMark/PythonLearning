sims=['fsx','P3D','msfs']
for sim in sims:
	if sim=='fsx':
		print(sim.upper())
	else:
		print(sim.title())

#installed_sims=['X-Plane','P3D']

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


installion=['auto','man','other']
used_ins=['auto','other','force']
for used_inst in used_ins:
	if used_inst in installion:
		print('install ')
	else:
		print('install a ')
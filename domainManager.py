from os import fdopen, remove
from tempfile import mkstemp
from shutil import move
import subprocess
import re




def inhabilitar(path,pattern,subst):
	fh, abs_path = mkstemp()
	with fdopen(fh,'w') as new_file:
		with open(path) as old_file:
			for line in old_file:
				if re.match(pattern,line):
					new_file.write(subst+line)
				else:
					new_file.write(line)
				
	remove(path)
	move(abs_path,path)

def main():
	file = open("doc",'r+');
	i = 0
	j = 0
	enabled = [None] * 10
	disabled = [None] * 10
	for line in file:
		if (line[0] == "#"):
			disabled[i] = line
			i=+1
		else:
			enabled[j] = line
			j=+1

	print("HABILITADOS \n")
	for enable in enabled:
		if enable != None:
			print(enable)
	print("DESHABILITADOS \n")
	for disable in disabled:
		if disable != None:
			print(disable)		
	
	inhabilitar(" ~/home/manuel/Documents/doc",enabled[0],"#")


	# bashCommand = "sudo reboot"
	# output = subprocess.check_output(['bash','-c', bashCommand])

if __name__ == '__main__':
	main()
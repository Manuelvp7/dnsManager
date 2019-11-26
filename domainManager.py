from os import fdopen, remove
from tempfile import mkstemp
from shutil import move
import subprocess
import re

def inhabilitarDeshabilitar(path,pattern,subst,habiDesabi):
	fh, abs_path = mkstemp()
	with fdopen(fh,'w') as new_file:
		with open(path) as old_file:
			for line in old_file:
				if re.match(pattern,line):
					if habiDesabi=="deshabilitar":						
						new_file.write(subst+line)
					else:
						new_file.write(subst)
				else:
					new_file.write(line)				
	remove(path)
	move(abs_path,path)



def leerReferencesForward(enabledDisabled):
	file = open("references",'r')
	array = [None] * 100
	i = 0
	if enabledDisabled == "disabled":
		for line in file:
			if (line[0] == "#"):
				array[i] = line[1:]
				i=i+1
	elif enabledDisabled == "enabled":
		for line in file:
			if (line[0] != "#"):
				array[i] = line
				i=i+1	
	return array			


		

def main():
	# file = open("../forward.equipo5.com",'r+')
	
	option = 5

	while  option!=0:	
		enabledArray = leerReferencesForward("enabled")
		disabledArray = leerReferencesForward("disabled")
		print("\n\n MENU DEL ADMINISTRADOR DE NOMBRES DE DOMINIO \n\n[1]Consultar sitios/servicios Disponibles\n\n[2]Deshabilitar\n\n[3]Habilitar\n\n[0]Salir y guardar cambios\n\n");
		option = input("INGRESE UNA OPCION  : ") 
		if option == "1":
			print("\nHABILITADOS \n")
			x = 0
			while x<len(enabledArray):
				if enabledArray[x] != None:
					print(enabledArray[x])
				x=x+2
			x = 0		
			print("\nDESHABILITADOS \n")
			while x<len(disabledArray):
				if disabledArray[x] != None:
					print(disabledArray[x])
				x=x+2
		elif option == "2":
			number = 0
			print("\n\nHABILITADOS \n")
			x = 0
			while x<len(enabledArray):
				if enabledArray[x] != None:
					print(x,enabledArray[x])
				x=x+2
			print("")
			optionDisable = input("\n\n INGRESE EL DOMINIO QUE DESEA DESHABILITAR: \n") 
			inhabilitarDeshabilitar("../reverse.equipo5.com",";"+disabledArray[int(optionDisable,10)],disabledArray[int(optionDisable,10)],"habilitar")
			inhabilitarDeshabilitar("../reverse.equipo5.com",";"+disabledArray[int(optionDisable,10)+1],disabledArray[int(optionDisable,10)+1],"habilitar")
			inhabilitarDeshabilitar("../forward.equipo5.com",";"+disabledArray[int(optionDisable,10)],disabledArray[int(optionDisable,10)],"habilitar")
			inhabilitarDeshabilitar("../forward.equipo5.com",";"+disabledArray[int(optionDisable,10)+1],disabledArray[int(optionDisable,10)+1],"habilitar")			
			inhabilitarDeshabilitar("references",enabledArray[int(optionDisable,10)],"#","deshabilitar")
			inhabilitarDeshabilitar("references",enabledArray[int(optionDisable,10)+1],"#","deshabilitar")

		elif option == "3":
			number = 0
			print("\n\nINHABILITADOS \n")
			x = 0
			while x<len(disabledArray):
				if disabledArray[x] != None:
					print(x,disabledArray[x])
				x=x+2
			print("")
			optionDisable = input("\n\n INGRESE EL DOMINIO QUE DESEA DESHABILITAR: \n") 
			inhabilitarDeshabilitar("../reverse.equipo5.com",";"+disabledArray[int(optionDisable,10)],disabledArray[int(optionDisable,10)],"habilitar")
			inhabilitarDeshabilitar("../reverse.equipo5.com",";"+disabledArray[int(optionDisable,10)+1],disabledArray[int(optionDisable,10)+1],"habilitar")
			inhabilitarDeshabilitar("../forward.equipo5.com",";"+disabledArray[int(optionDisable,10)],disabledArray[int(optionDisable,10)],"habilitar")
			inhabilitarDeshabilitar("../forward.equipo5.com",";"+disabledArray[int(optionDisable,10)+1],disabledArray[int(optionDisable,10)+1],"habilitar")			
			inhabilitarDeshabilitar("references","#"+disabledArray[int(optionDisable,10)],disabledArray[int(optionDisable,10)],"habilitar")
			inhabilitarDeshabilitar("references","#"+disabledArray[int(optionDisable,10)+1],disabledArray[int(optionDisable,10)+1],"habilitar")


	bashCommand = "sudo systemctl restart bind9"
	output = subprocess.check_output(['bash','-c', bashCommand])

if __name__ == '__main__':
	main()
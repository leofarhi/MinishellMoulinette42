#####################################################
#Exemple d'un cleanOutput avec de la coloration :
def remove_specialChar(output):
	lines = output.split(" \n\x1b[A")
	new_text = lines[0]
	del lines[0]
	for line in lines:
		if not "\x1b[K" in line:
			return output
		temp = line.split("\n",1)
		new_text += "\n"+temp[1]
	return new_text

def cleanOutput(output):
	output = remove_specialChar(output)
	res = ""
	if "\033[95m" in output:
		lines = output.split("\033[95m")
	else:
		lines = output.split("\033[96m")
	res = lines[0]
	del lines[0]
	for line in lines:
		temp = line.split("\x1b[39m$ ",1)
		if len(temp) > 1:
			res += '@MINISHELL@>' + temp[1]
		else:
			res += temp[0]
	return res
#####################################################

#Exemple d'un cleanOutput avec un prompt basique :
def cleanOutput(output):
	output = output.replace("minishell$ ","@MINISHELL@>")
	return output
# demoFileRead.py
# D. Thiebaut
# demonstrate how to read file and
# parse it for particular patterns.

def main():
	# read file
	fileName = input("What is the file name?")
	file = open( fileName, "r" )
	lines = file.readlines()
	file.close()

	file = open("export.csv")
	#look for patterns
	countW05 = 0
	for line in lines:
		line = line.strip().upper()
		#print (line)
	if line.find ( "W05" )!= -1:
		countW05 = countW05 + 1
                
	#display result
	print("File Name:" + fileName.name)
       print( "TRANSACTION NUM:", countW05 ) 
	
main()

# HTTP://CS.SMITH.EDU/dftwiki/

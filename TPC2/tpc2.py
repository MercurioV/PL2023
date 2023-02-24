import sys
 
suma = 0 
isAdding = False
def parse(line):
    global isAdding
    global suma
    if(line.rstrip().lower() == 'on'):
        isAdding = True
    elif(line.rstrip().lower() == 'off'):
        isAdding = False
    elif(line.rstrip() == '='):
        print(f"The result is {suma}")
    elif(line.rstrip().isdigit() and isAdding):
        suma+=int(line.rstrip())
    elif(' ' in line.rstrip()):
        if(isAdding):
            for digit in line.rstrip().split(' '):
                if digit.isdigit():
                    suma+=int(digit)
    else:
        print("Unknown command")
    
    
        
for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    parse(line)
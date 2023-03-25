import os
video=input("Please enter a converted video-to-ascii file: ")
f=open(video,"r")
while True:
       try:
            line=next(f)
            #on start of a new frame, it clears the screen
            if line[0]=="$":
                os.system("cls")
                #gets rid of new line character
                line=line[1:]
            #loops through each character and amount to print set
            prnt_ln=line.split(",")
            for y in prnt_ln:
                try:
                    #prints character given amount of times
                    for z in range(0,int(y[1:])):
                        print(y[0], end="")
                except:
                    pass
            print()
       except StopIteration:
            break
f.close()
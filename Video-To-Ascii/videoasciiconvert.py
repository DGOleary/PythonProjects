from moviepy.editor import VideoFileClip
from PIL import Image, ImageOps

def makeAscii(filename, charfile):
    image= Image.open(filename)
    #sets to gray because the ascii image is based on how dark a pixel is
    image=ImageOps.grayscale(image)
    line=""
    templine=""
    file=open(charfile, "a")
    height=int(image.height)
    width=int(image.width)
    #normalizes the size if it's too large
    if height>300:
        wsize=300.0/float(width)
        hsize=int(float(height)*float(wsize))
        image=image.resize((300,hsize), Image.Resampling.LANCZOS)
    height=int(image.height)
    width=int(image.width)
    #goes through all the pixels and converts them to ascii based on their darkness in greyscale
    for x in range(0,height,4):
        for y in range(0, width,4):
            if (x+3)<=height and (y+3)<=width:
                #sets the ascii to the group of pixels based on their darkness
                val=image.getpixel((y,x))+image.getpixel((y,x+1))+image.getpixel((y,x+2))+image.getpixel((y,x+3))
                val/=4
                if val>229:
                    line+=" "
                elif val>203:
                    line+="."
                elif val>177:
                    line+=":"
                elif val>151:
                    line+="-"
                elif val>125:
                    line+="="
                elif val>99:
                    line+="+"
                elif val>73:
                    line+="*"
                elif val>47:
                    line+="#"
                elif val>21:
                    line+="%"
                else:
                    line+="@"
        #compresses line by putting the same character as a count
        #strings to track occurrences of character
        tempchar=line[0]
        tempcount=1
        #boolean variable to check if the current character was added to the file
        #because the last character will get cut off if it's not new otherwise
        add=False
        for z in range(0, len(line)-1):
            if tempchar==line[z+1]:
                add=False
                tempcount+=1
            else:
                #, deliniates new character-count set
                templine+=tempchar+str(tempcount)+","
                tempchar=line[z+1]
                tempcount=1
                add=True
        if not add:
            templine+=tempchar+str(tempcount)+","
        #skips the last character because it's a superfluous ,
        file.write(templine[0:-1]+"\n")
        templine=""
        line=""
    #string that signifies new frame
    file.write("$")
    file.close()
videofile=input("Please enter an mp4 file to convert: ")
print("start")
myclip = VideoFileClip(videofile)
#halves frame count to save more space
fps=int(myclip.fps/2)
#the amount to increment is how many seconds pass per frame
inc=float(1/fps)
cur_frame=0
save_file=videofile[0:(len(videofile)-4)]+".txt"
f=open(save_file,"w")
for x in range(0,int(fps*myclip.duration)):
    #uses the frame rate to find how many seconds to go to find the next frame
    cur_frame+=inc
    try:
        myclip.save_frame("frame.jpg",cur_frame,False)
        makeAscii("frame.jpg",save_file)
    except:
        pass
print("done")


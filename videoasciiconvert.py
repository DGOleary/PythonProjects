from moviepy.editor import *
from PIL import Image, ImageOps
import os

def makeAscii(filename):
    image= Image.open(filename)
    image=ImageOps.grayscale(image)
    line="";
    height=int(image.height)
    width=int(image.width)
    #normalizes the size if it's too large
    if height>300:
        wsize=300.0/float(width)
        hsize=int(float(height)*float(wsize))
        image=image.resize((300,hsize), Image.Resampling.LANCZOS)
    height=int(image.height)
    width=int(image.width)
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
        print(line)
        line=""

myclip = VideoFileClip('video.mp4')
fps=int(myclip.fps/2)
inc=float(1/fps)
cur_frame=0
for x in range(0,int(fps*myclip.duration)):
    cur_frame+=inc
    try:
        os.system('cls')
        myclip.save_frame("frame.jpg",cur_frame,False)
        makeAscii("frame.jpg")
    except:
        pass
#print ( [frame[0,:,0].max()
         #for frame in myclip.iter_frames()])
#for frame in myclip.iter_frames():
    #print(type(frame))
#myclip.save_frame("frame.jpg",3,False)


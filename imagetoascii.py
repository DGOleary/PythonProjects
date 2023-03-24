from PIL import Image, ImageOps
filename=input("Enter a picture to use: ");
image= Image.open(filename)
image=ImageOps.grayscale(image)
line="";
height=int(image.height)
width=int(image.width)
if height>300:
    wsize=300.0/float(width)
    hsize=int(float(height)*float(wsize))
    image=image.resize((300,hsize), Image.Resampling.LANCZOS)
height=int(image.height)
width=int(image.width)
print(width)
print(height)
for x in range(0,height,4):
    for y in range(0, width,4):
        if (x+3)<=height and (y+3)<=width:
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
            #print(y)
    #print(x)
    print(line)
    line=""

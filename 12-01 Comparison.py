import os
import time
import base64
start_time = time.time();

DIR = 'C:\\Users\\Muhammad Haad\\PycharmProjects\\VisualProgrammingProject\\MainVideoFrames'
i = TotalFramesOfMainVideo = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR,name))])

DIR = 'C:\\Users\\Muhammad Haad\\PycharmProjects\\VisualProgrammingProject\\Add1Frames'
j = TotalFramesOfAdd1 = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR,name))])

DIR = 'C:\\Users\\Muhammad Haad\\PycharmProjects\\VisualProgrammingProject\\Add2Frames'
k = TotalFramesOfAdd2 = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR,name))])
print(k)

DIR = 'C:\\Users\\Muhammad Haad\\PycharmProjects\\VisualProgrammingProject\\Add3Frames'
h = TotalFramesOfAdd3 = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR,name))])
print(h)
y=1
z=0;
str = []
new = []
flag = 0
for w in range (0, i):
    for l in range (0, 500):
        new.append("b'-\xab")
    str.append(new)
    new = []
z=1; q=0;
while (z<=TotalFramesOfMainVideo):
    currentAddFrame = "C:\\Users\\Muhammad Haad\\PycharmProjects\\VisualProgrammingProject\\MainVideoFrames\\output_image-" + z.__str__() + '.jpg'
    with open(currentAddFrame, "rb") as image1File:
        str[q] = base64.standard_b64decode(image1File.read())
        q=q+1
        z=z+1

z=1
while(j>0):
    currentAddFrame = "C:\\Users\\Muhammad Haad\\PycharmProjects\\VisualProgrammingProject\Add1Frames\\output_image-" + z.__str__() + '.jpg'
    with open(currentAddFrame, "rb") as image1File:
        str1 = base64.standard_b64decode(image1File.read())
    for l in range(0,i):
        if(str[l]==str1):
            print('yeah')
            flag=1
    j = j - 1
    z = z + 1
    if(z==2 and flag==0):
        print('didnt match')
        break;

z=1
while(k>0):
    currentAddFrame = "C:\\Users\\Muhammad Haad\\PycharmProjects\\VisualProgrammingProject\Add2Frames\\output_image-" + z.__str__() + '.jpg'
    with open(currentAddFrame, "rb") as image1File:
        str1 = base64.standard_b64decode(image1File.read())
    for l in range(0,i):
        if(str[l]==str1):
            print('yeah 2nd')
            flag=1

    k = k - 1
    z = z + 1
    if(z==4 and flag==0):
        print('didnt match')
        break;
z=1
while(h>0):
    currentAddFrame = "C:\\Users\\Muhammad Haad\\PycharmProjects\\VisualProgrammingProject\Add3Frames\\output_image-" + z.__str__() + '.jpg'
    with open(currentAddFrame, "rb") as image1File:
        str1 = base64.standard_b64decode(image1File.read())
        print(str1)
    for l in range(0,i):
        if(str[l]==str1):
            print('yeah 3rd',l)
            flag=1

    h = h - 1
    z = z + 1
    if(z==4 and flag==0):
        print('didnt match')
        break;
print("Frame Comparing takes ", (time.time() - start_time));
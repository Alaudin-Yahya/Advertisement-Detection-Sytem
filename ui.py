import cv2;
from tkinter import *
from tkinter import filedialog
from subprocess import  check_output, CalledProcessError, STDOUT
from tkinter import ttk
import shutil
import subprocess;
import base64;
import time;
import os;
import numpy as np
import sys;
MainFile = "";
AdvertismentFiles=["asdasd","asdasd"];
Flag = 0;
start_time = time.time();

def BreakFrames(event):
    path = "C:\\Users\Public\VpProject\VisualProgrammingProject\output"
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=False, onerror=None)
    directory = "output"
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = "output/MainVideoFrames"
    if not os.path.exists(directory):
        os.makedirs(directory)
    Duration = getDuration(MainFile)
    args = 'ffmpeg.exe -ss 00:00:00 -t '+Duration+' -i ' + MainFile + ' -qscale:v 2 -r 2.0 '+directory+'/output_image-%0d.jpg'
    subprocess.call(args, shell=True)
    k=1;
    directory = "output/AdFrames"+k.__str__();
    for i in AdvertismentFiles:
        if not os.path.exists(directory):
            os.makedirs(directory)
        duration = getDuration(i)
        args = 'ffmpeg.exe -ss 00:00:00 -t ' + duration + ' -i ' + i + ' -qscale:v 2 -r 2.0 ' + directory + '/output_image-%0d.jpg'
        subprocess.call(args, shell=True)
        k+=1
        directory = "output/AdFrames" + k.__str__();
    print("Time",time.time()-start_time)

def getDuration(filename):

    command = ['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',filename]
    try:
        output = check_output( command, stderr=STDOUT ).decode()
    except CalledProcessError as e:
        output = e.output.decode()
    print(type(output), output)
    output = int(float(output))
    output = time.strftime('%H:%M:%S', time.gmtime(output))
    return output


def SelectMainFile(event):
    global MainFile
    file = filedialog.askopenfilenames(parent=root, title='Choose a file')
    file = root.tk.splitlist(file)
    MainFile = file[0]
    label = ttk.Label(root, text="Selected", font=("Calibri", 13))
    label.pack()
    label.place(x=320, y=90)

def SelectionofFiles(event):
    global AdvertismentFiles;
    global Flag;
    files = filedialog.askopenfilenames(parent=root, title='Choose a file')
    AdvertismentFiles = root.tk.splitlist(files)
    j= len(AdvertismentFiles);
    msg = j.__str__()+" files Selected"
    label = ttk.Label(root, text=msg, font=("Calibri", 13))
    label.pack()
    label.place(x=320, y=180)
    Flag=1;
    # for i in files:
        # y = 130+j;
        # i = i+"\n"
        # label = ttk.Label(root, text=i, font=("Calibri",8))
        # label.pack()
        # label.place(x=25,y=y)
        # j = j + 13;

def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

def ms_to_t(millis):
    millis=millis/2
    minutes=int(millis/60)
    if minutes<10:
        min = '0'+ str(minutes)
    else:
        min = str(minutes)
    s = millis / 60 - minutes
    seconds = int(s * 60)

    if seconds < 10:
        sec = '0' + str(seconds)
    else:
        sec = str(seconds)

    print("00:",min,":",sec)

def Detection(event):
    file = open("result.txt","w+");
    DIR = 'C:\\Users\Public\VpProject\VisualProgrammingProject\output'
    files = TotalNoOfFolders = 0;
    for _, dirnames, filenames in os.walk(DIR):
        TotalNoOfFolders += len(dirnames)
    print(TotalNoOfFolders);

    DIR = 'C:\\Users\Public\VpProject\VisualProgrammingProject\output\\MainVideoFrames'
    i = TotalFramesOfMainVideo = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    print(i)
    w = 1
    m = 1;
    p = 1;
    j = 0
    u=0
    arr = []
    for d in range(0,len(AdvertismentFiles)*2):
        arr.append(0)
    start_time = time.time()
    for l in range(1, TotalNoOfFolders):
        m = 1
        DIR = 'C:\\Users\Public\VpProject\VisualProgrammingProject\output\\AdFrames' + l.__str__();
        frames = f = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]);
        p = 1
        count = 0
        while (m < f + 1):
            img11 = cv2.imread(
                'C:\\Users\Public\VpProject\VisualProgrammingProject\output\\AdFrames' + l.__str__() + '\\output_image-' + str(
                    m) + '.jpg', cv2.IMREAD_COLOR)
            n = p
            while (n < i + 1):
                img12 = cv2.imread(
                    'C:\\Users\Public\VpProject\VisualProgrammingProject\output\\MainVideoFrames\\output_image-' + str(
                        n) + '.jpg', cv2.IMREAD_COLOR)
                # print(l,m,n)
                img = img11 - img12;
                if ((img[80][340][0] < 10 or img[80][340][0] > 245) and (img[80][340][1] < 10 or img[80][340][1] > 245) and (img[80][340][2] < 10 or img[80][340][2] > 245)):
                    if ((img[280][340][0] < 10 or img[280][340][0] > 245) and (img[280][340][1] < 10 or img[280][340][1] > 245) and (img[280][340][2] < 10 or img[280][340][2] > 245)):
                        if ((img[280][460][0] < 10 or img[280][460][0] > 245) and (img[280][460][1] < 10 or img[280][460][1] > 245) and (img[280][460][2] < 10 or img[280][460][2] > 245)):
                            if ((img[80][460][0] < 10 or img[80][460][0] > 245) and (img[80][460][1] < 10 or img[80][460][1] > 245) and (img[80][460][2] < 10 or img[80][460][2] > 245)):
                                if ((img[180][320][0] < 10 or img[180][320][0] > 245) and (img[180][320][1] < 10 or img[180][320][1] > 245) and (img[180][320][2] < 10 or img[180][320][2] > 245)):
                                    print("equal", l, m, n, count);
                                    file.write(os.path.basename(AdvertismentFiles[j]));
                                    file.write('\n')
                                    count += 1;
                                    p = n + 1;
                                    file.write(AdvertismentFiles[j])
                                    if (count == 1):
                                        arr[u]=n;
                                        u+=1
                                    if (m == f):
                                        arr[u] = n;
                                        u += 1
                                    break;
                                # print(time.time()-t2,"Comp")
                n += 1
            m += 1
        j += 1
    print(time.time()-start_time)
    print(arr)
    for t in arr:
        print(t)
        ms_to_t(t);


root = Tk()
root.geometry("500x500") #size of the app to be 500x500
root.resizable(0, 0)

#*************Ad Detection***************
Title = root.title( "Ad Detection")
label = ttk.Label(root, text="Advertisment Detection", font = ("Calibri",20,'bold'))
label.pack()
label.place(x=120,y=10)

#************Select Main Video***************

label = ttk.Label(root, text="Select Main Video", font = ("Calibri",13))
label.pack()
label.place(x=20,y=60)
Browse = Button(None, text='browse');
Browse.pack();
Browse.place(x=220,y=90)
Browse.bind('<Button-1>', SelectMainFile)

#*************Select Ad Videos***************

label = ttk.Label(root, text="Select Advertisements", font = ("Calibri",13))
label.pack()
label.place(x=20,y=150)
Browse = Button(None, text='browse');
Browse.pack()
Browse.place(x=220,y=180)
Browse.bind('<Button-1>', SelectionofFiles)

#********************Begin**************
Browse = Button(None, text='Extract Frames');
Browse.pack()
Browse.place(x=180,y=380)
Browse.bind('<Button-1>', BreakFrames)


#********************Start Detection***************
Browse = Button(None, text='Detect');
Browse.pack()
Browse.place(x=280,y=380)
Browse.bind('<Button-1>', Detection)

root.mainloop()
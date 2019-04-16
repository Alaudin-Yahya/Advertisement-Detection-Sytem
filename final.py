import numpy as np
import cv2
import os
import time

start_time = time.time();
count= 0
m=4
# for m in range (1,176):
DIR = 'C:\\Users\Public\VpProject\VisualProgrammingProject\output\\AdFrames2'
i = TotalFramesOfMainVideo = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
DIR = 'C:\\Users\Public\VpProject\VisualProgrammingProject\output\\MainVideoFrames'
j = TotalFramesOfMainVideo = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
p=1
n=1
print(i)
print(j)

str = np.empty((j,360,640,3))
# print(str)
# # new = []
# # for w in range(0, i):
# #     new.append("b'-\xab")
# #     for e in range(0,360):
# #         new.append("b'-\xab")
# #         for r in range(0,640):
# #             new.append("b'-\xab")
# #             for y in range(0,3):
# #                 new.append("b'-\xab")
# #             str.append(new)
# #         str.append(new)
# #     str.append(new)
# #     new = []
# z = 1;
# q = 0;
# m=1
# while (m <= j):
img11 = cv2.imread('C:\\Users\Public\VpProject\VisualProgrammingProject\output\\MainVideoFrames\\output_image-18.jpg',cv2.IMREAD_COLOR)
    # print(img11)
str[0] = img11;
img11 = cv2.imread('C:\\Users\Public\VpProject\VisualProgrammingProject\output\\AdFrames4\\output_image-5.jpg',cv2.IMREAD_COLOR)
str[1]= img11;
print(str[0]-str[1])
    # q = q + 1
    # m = m + 1


m=1
n=1
# while m<i:
#     n=p
#     while n<j:
#         # n=p
#     # for n in range (p,j):
#         t1 = time.time();
#         img11 = cv2.imread('C:\\Users\Public\VpProject\VisualProgrammingProject\output\\AdFrames2\\output_image-'+str(m)+'.jpg',cv2.IMREAD_COLOR)
#         img12 = cv2.imread('C:\\Users\Public\VpProject\VisualProgrammingProject\output\\MainVideoFrames\\output_image-'+str(n)+'.jpg', cv2.IMREAD_COLOR)
#         t2 = time.time()
#         # print(t2-t1,"Image Loading")
#         img = img11-img12;
#         # if(img11[10][10][0]==img12[10][10][0] and img11[20][20][0]==img12[20][20][0] and img11[30][30][0]==img12[30][30][0] ):
#         #     print("Equal",m,n)
#         # print("ssss",n)
#         if((img[80][340][0]<10 or img[80][340][0]>245) and (img[80][340][1]<10 or img[80][340][1]>245) and (img[80][340][2]<10 or img[80][340][2]>245)):
#             if ((img[280][340][0] < 10 or img[280][340][0] > 245) and (img[280][340][1] < 10 or img[280][340][1] > 245) and (img[280][340][2] < 10 or img[280][340][2] > 245)):
#                 if ((img[280][460][0] < 10 or img[280][460][0] > 245) and (img[280][460][1] < 10 or img[280][460][1] > 245) and (img[280][460][2] < 10 or img[280][460][2] > 245)):
#                     if ((img[80][460][0] < 10 or img[80][460][0] > 245) and (img[80][460][1] < 10 or img[80][460][1] > 245) and (img[80][460][2] < 10 or img[80][460][2] > 245)):
#                         if ((img[180][320][0] < 10 or img[180][320][0] > 245) and (img[180][320][1] < 10 or img[180][320][1] > 245) and (img[180][320][2] < 10 or img[180][320][2] > 245)):
#                             print("equal", m, n,count);
#                             count+=1;
#                             p=n+1;
#                             break;
#                         # print(time.time()-t2,"Comp")
#         n+=1
#     if(count==5):
#         # print("haha")
#         m=i-5
#     m+=1
# print(start_time-time.time())
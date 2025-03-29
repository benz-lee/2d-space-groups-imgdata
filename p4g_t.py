from PIL import Image,ImageDraw
import os,random


name='p4g'
i=75
r=3
a=100#basis width
b=100#basis height
width, height = 1600, 1600
output_dir = f'E:/data/test_set/{name}'
os.makedirs(output_dir, exist_ok=True)
for t in range(0,i,1):
 def make_sure(k1,k2):   
    if k1 == k2:
        return False
    return True
 img = Image.new("L", (width, height), "white")
 draw = ImageDraw.Draw(img)
 while True:
    k1 = random.randint(r, int(a/2-r)) 
    k2 = random.randint(r, int(a/2-r))
    if make_sure(k1,k2):
        break
 x1, y1 = k1, k1
 x2, y2 = a - k1, k1
 x3, y3 = a - k1, b - k1
 x4, y4 = k1, b - k1
 x5, y5 = k2, k2
 x6, y6 = a - k2, k2
 x7, y7 = a - k2, b - k2
 x8, y8 = k2, b - k2
 for n in range(0, width, 2*a):
    for m in range(0, height, 2*b):
        #left_top
        points = [
            (n+x1, m+y1),
            (n+x4, m+y4),
            (n+x5, m+y5)
        ]
        points_1 = [
            (n+x1, m+y1),
            (n+x2, m+y2),
            (n+x6, m+y6)
        ]
        points_2 = [
            (n+x7, m+y7),
            (n+x2, m+y2),
            (n+x3, m+y3)
        ]
        points_3 = [
            (n+x3, m+y3),
            (n+x4, m+y4),
            (n+x8, m+y8)
        ]
        #left_bottom
        points_4 = [
            (n+x1, m+y1+b),
            (n+x4, m+y4+b),
            (n+x8, m+y8+b)
        ]
        points_5 = [
            (n+x1, m+y1+b),
            (n+x2, m+y2+b),
            (n+x5, m+y5+b)
        ]
        points_6 = [
            (n+x2, m+y2+b),
            (n+x3, m+y3+b),
            (n+x6, m+y6+b)
        ]
        points_7 = [
            (n+x3, m+y3+b),
            (n+x4, m+y4+b),
            (n+x7, m+y7+b)
        ]
        #right_top
        points_8 = [
            (n+x1+a, m+y1),
            (n+x4+a, m+y4),
            (n+x8+a, m+y8)
        ]
        points_9 = [
            (n+x1+a, m+y1),
            (n+x2+a, m+y2),
            (n+x5+a, m+y5)
        ]
        points_10 = [
            (n+x2+a, m+y2),
            (n+x3+a, m+y3),
            (n+x6+a, m+y6)
        ]
        points_11 = [
            (n+x3+a, m+y3),
            (n+x4+a, m+y4),
            (n+x7+a, m+y7)
        ]
        #right_bottom
        points_12 = [
            (n+x1+a, m+y1+b),
            (n+x4+a, m+y4+b),
            (n+x5+a, m+y5+b)
        ]
        points_13 = [
            (n+x1+a, m+y1+b),
            (n+x2+a, m+y2+b),
            (n+x6+a, m+y6+b)
        ]
        points_14 = [
            (n+x2+a, m+y2+b),
            (n+x3+a, m+y3+b),
            (n+x7+a, m+y7+b)
        ]
        points_15 = [
            (n+x3+a, m+y3+b),
            (n+x4+a, m+y4+b),
            (n+x8+a, m+y8+b)
        ]
        draw.polygon(points, fill=0)
        draw.polygon(points_1, fill=0)
        draw.polygon(points_2, fill=0)
        draw.polygon(points_3, fill=0)
        draw.polygon(points_4, fill=0)
        draw.polygon(points_5, fill=0)
        draw.polygon(points_6, fill=0)
        draw.polygon(points_7, fill=0)
        draw.polygon(points_8, fill=0)
        draw.polygon(points_9, fill=0)
        draw.polygon(points_10, fill=0)
        draw.polygon(points_11, fill=0)
        draw.polygon(points_12, fill=0)
        draw.polygon(points_13, fill=0)
        draw.polygon(points_14, fill=0)
        draw.polygon(points_15, fill=0)
 img.save(f'{output_dir}/{name}_t_{t}.png')


for t in range(i,2*i,1):
 def make_sure(k1,k2):
    if k1 == k2:
        return False
    return True
 img = Image.new("L", (width, height), "white")
 draw = ImageDraw.Draw(img)
 while True:
    k1 = random.randint(r, int(a/2-r)) 
    k2 = random.randint(r, int(a/2-r))
    if make_sure(k1,k2):
        break
 x1, y1 = k1, k1
 x2, y2 = a - k1, k1
 x3, y3 = a - k1, b - k1
 x4, y4 = k1, b - k1
 x5, y5 = k2, b - k2
 x6, y6 = k2, k2
 x7, y7 = a - k2, k2
 x8, y8 = a - k2, b - k2
 for n in range(0, width, 2*a):
    for m in range(0, height, 2*b):
        #left_top
        points = [
            (n+x1, m+y1),
            (n+x4, m+y4),
            (n+x5, m+y5)
        ]
        points_1 = [
            (n+x1, m+y1),
            (n+x2, m+y2),
            (n+x6, m+y6)
        ]
        points_2 = [
            (n+x7, m+y7),
            (n+x2, m+y2),
            (n+x3, m+y3)
        ]
        points_3 = [
            (n+x3, m+y3),
            (n+x4, m+y4),
            (n+x8, m+y8)
        ]
        #left_bottom
        points_4 = [
            (n+x1, m+y1+b),
            (n+x4, m+y4+b),
            (n+x6, m+y6+b)#
        ]
        points_5 = [
            (n+x1, m+y1+b),
            (n+x2, m+y2+b),
            (n+x7, m+y7+b)#
        ]
        points_6 = [
            (n+x2, m+y2+b),
            (n+x3, m+y3+b),
            (n+x8, m+y8+b)#
        ]
        points_7 = [
            (n+x3, m+y3+b),
            (n+x4, m+y4+b),
            (n+x5, m+y5+b)#
        ]
        #right_top
        points_8 = [
            (n+x1+a, m+y1),
            (n+x4+a, m+y4),
            (n+x6+a, m+y6)
        ]
        points_9 = [
            (n+x1+a, m+y1),
            (n+x2+a, m+y2),
            (n+x7+a, m+y7)
        ]
        points_10 = [
            (n+x2+a, m+y2),
            (n+x3+a, m+y3),
            (n+x8+a, m+y8)
        ]
        points_11 = [
            (n+x3+a, m+y3),
            (n+x4+a, m+y4),
            (n+x5+a, m+y5)
        ]
        #right_bottom
        points_12 = [
            (n+x1+a, m+y1+b),
            (n+x4+a, m+y4+b),
            (n+x5+a, m+y5+b)
        ]
        points_13 = [
            (n+x1+a, m+y1+b),
            (n+x2+a, m+y2+b),
            (n+x6+a, m+y6+b)
        ]
        points_14 = [
            (n+x2+a, m+y2+b),
            (n+x3+a, m+y3+b),
            (n+x7+a, m+y7+b)
        ]
        points_15 = [
            (n+x3+a, m+y3+b),
            (n+x4+a, m+y4+b),
            (n+x8+a, m+y8+b)
        ]
        draw.polygon(points, fill=0)
        draw.polygon(points_1, fill=0)
        draw.polygon(points_2, fill=0)
        draw.polygon(points_3, fill=0)

        draw.polygon(points_4, fill=0)
        draw.polygon(points_5, fill=0)
        draw.polygon(points_6, fill=0)
        draw.polygon(points_7, fill=0)

        draw.polygon(points_8, fill=0)
        draw.polygon(points_9, fill=0)
        draw.polygon(points_10, fill=0)
        draw.polygon(points_11, fill=0)

        draw.polygon(points_12, fill=0)
        draw.polygon(points_13, fill=0)
        draw.polygon(points_14, fill=0)
        draw.polygon(points_15, fill=0)
 img.save(f'{output_dir}/{name}_t_{t}.png')
print('ok')
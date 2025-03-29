from PIL import Image,ImageDraw
import math,os,random

name='p3'
i=75
width, height = 1600, 1600
r=3
a=173#basis width
b=100#basis height
s=math.sqrt(3)
output_dir = f'E:/data/test_set/{name}'
os.makedirs(output_dir, exist_ok=True)
for t in range(0,i,1):
 img = Image.new("L", (width, height), "white")
 draw = ImageDraw.Draw(img)
 x = random.randint(r, int(b/(2*s)-2)) 
 x1, y1 = 0, 0
 x2, y2 = 0, b
 x3, y3 = b*s/2, b/2
 x4, y4 = x, s*x
 x5, y5 = s*b/2-2*x, b/2
 x6, y6 = x, b-s*x
 for n in range(0, width, a):
    for m in range(0, height, b):
        points = [
            (n+x1, m+y1),
            (n+x4, m+y4),
            (n+x2, m+y2)
        ]
        points_1 = [
            (n+x3, m+y3),
            (n+x5, m+y5),
            (n+x1, m+y1)
        ]
        points_2 = [
            (n+x2, m+y2),
            (n+x6, m+y6),
            (n+x3, m+y3)
        ]

        points_3 = [
            (n+x1+s*b/2, m+y1+b/2),
            (n+x4+s*b/2, m+y4+b/2),
            (n+x2+s*b/2, m+y2+b/2)
        ]
        points_4 = [
            (n+x1+s*b/2, m+y1+b/2),
            (n+x5+s*b/2, m+y5+b/2),
            (n+x3+s*b/2, m+y3+b/2)
        ]
        points_5 = [
            (n+x6+s*b/2, m+y6+b/2),
            (n+x2+s*b/2, m+y2+b/2),
            (n+x3+s*b/2, m+y3+b/2)
        ]
        draw.polygon(points, fill=0)
        draw.polygon(points_1, fill=0)
        draw.polygon(points_2, fill=0)
        draw.polygon(points_3, fill=0)
        draw.polygon(points_4, fill=0)
        draw.polygon(points_5, fill=0)
 img = img.crop((0,a,width,height))
 img.save(f'{output_dir}/{name}_t_{t}.png')



for t in range(i,2*i,1):
 img = Image.new("L", (width, height), "white")
 draw = ImageDraw.Draw(img)
 x = random.randint(r, int(b/(2*s)-2)) 
 x1, y1 = 0, 0
 x2, y2 = 0, b
 x3, y3 = b*s/2, b/2
 x4, y4 = x, s*x
 x5, y5 = s*b/2-2*x, b/2
 x6, y6 = x, b-s*x
 for n in range(0, width, a):
    for m in range(0, height, b):
        points = [
            (n+x1, m+y1),
            (n+x6, m+y6),
            (n+x2, m+y2)
        ]
        points_1 = [
            (n+x3, m+y3),
            (n+x4, m+y4),
            (n+x1, m+y1)
        ]
        points_2 = [
            (n+x2, m+y2),
            (n+x5, m+y5),
            (n+x3, m+y3)
        ]

        points_3 = [
            (n+x1+s*b/2, m+y1+b/2),
            (n+x6+s*b/2, m+y6+b/2),
            (n+x2+s*b/2, m+y2+b/2)
        ]
        points_4 = [
            (n+x1+s*b/2, m+y1+b/2),
            (n+x4+s*b/2, m+y4+b/2),
            (n+x3+s*b/2, m+y3+b/2)
        ]
        points_5 = [
            (n+x5+s*b/2, m+y5+b/2),
            (n+x2+s*b/2, m+y2+b/2),
            (n+x3+s*b/2, m+y3+b/2)
        ]
        draw.polygon(points, fill=0)
        draw.polygon(points_1, fill=0)
        draw.polygon(points_2, fill=0)
        draw.polygon(points_3, fill=0)
        draw.polygon(points_4, fill=0)
        draw.polygon(points_5, fill=0)

 img = img.crop((0,a,width,height))
 img.save(f'{output_dir}/{name}_t_{t}.png')
print('ok')

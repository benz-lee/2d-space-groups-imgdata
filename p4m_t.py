from PIL import Image,ImageDraw
import os,random

name='p4m'
i=150
r=3
a=100#basis width
b=100#basis height
width, height = 1600, 1600
output_dir = f'E:/data/test_set/{name}'
os.makedirs(output_dir, exist_ok=True)
for t in range(0,i,1):
 def make_sure(x,y,k):
    if x == y:
        return False
    if y == -x + a/2 +k:#垂直平分线
        return False
    return True
 img = Image.new("L", (width, height), "white")
 draw = ImageDraw.Draw(img)
 while True:
    k= random.randint(r, int(a/2-r))
    x = random.randint(r, int(a/2-r)) 
    y = random.randint(r, int(a/2-r))
    if make_sure(x,y,k):
        break
 x0 ,y0 = a/2, b/2

 x1, y1 = x, y
 x2, y2 = k, k
 x3, y3 = y, x

 x4, y4 = a - y, x
 x5, y5 = a - k, k
 x6, y6 = a - x, y

 x7, y7 = a - x, b - y
 x8, y8 = a - k, b - k
 x9, y9 = a - y, b - x

 x10, y10 = y, b - x
 x11, y11 = k, a - k
 x12, y12 = x, b - y

 for n in range(0, width, a):
    for m in range(0, height, b):
         draw.polygon([(x0 + n, y0 + m), (x1 + n, y1 + m), (x2 + n, y2 + m), (x3 + n, y3 + m)], fill=0) 
         draw.polygon([(x0 + n, y0 + m), (x4 + n, y4 + m), (x5 + n, y5 + m), (x6 + n, y6 + m)], fill=0)    
         draw.polygon([(x0 + n, y0 + m), (x7 + n, y7 + m), (x8 + n, y8 + m), (x9 + n, y9 + m)], fill=0) 
         draw.polygon([(x0 + n, y0 + m), (x10+ n, y10 + m), (x11+ n, y11 + m), (x12+ n, y12 + m)], fill=0)
 img.save(f'{output_dir}/{name}_t_{t}.png')
print('ok')
     

import math
from PIL import Image, ImageDraw
import random,os

name='p3m1'
width, height = 1400, 1400
i=150
r=3
a=173#basis width
b=100#basis height
s=math.sqrt(3)
output_dir = f'E:/data/test_set/{name}'
os.makedirs(output_dir, exist_ok=True)
for t in range(0,i,1):
 img = Image.new("L", (width, height), "white")
 draw = ImageDraw.Draw(img)
 k=random.randint(r, int((b/s)-r))
 x = random.randint(r, int(b/2)) 
 x1, y1 = s*b/6, b/2
 x2, y2 = 0, x
 x3, y3 = k/2, s*k/2
 x4, y4 = s*x/2, x/2
 x5, y5 = s*b/2-s*x/2, b/2-x/2
 x6, y6 = s*b/2-k, b/2
 x7, y7 = s*b/2-s*x/2, b/2+x/2
 x8, y8 = s*x/2, b-x/2
 x9, y9 = k/2, b-s*k/2
 x10, y10 = 0,b-x
 for n in range(0, width, a):
    for m in range(0, height, b):
        draw.polygon([(x1+n, y1+m),(x2+n, y2+m),(x3+n, y3+m),(x4+n, y4+m)],fill=0)
        draw.polygon([(x1+n, y1+m),(x5+n, y5+m),(x6+n, y6+m),(x7+n, y7+m)], fill=0)
        draw.polygon([(x1+n, y1+m),(x8+n, y8+m),(x9+n, y9+m),(x10+n, y10+m)], fill=0)

        draw.polygon([(x1+n+s*b/2, y1+m+b/2),(x2+n+s*b/2, y2+m+b/2),(x3+n+s*b/2, y3+m+b/2),(x4+n+s*b/2, y4+m+b/2)],fill=0)
        draw.polygon([(x1+n+s*b/2, y1+m+b/2),(x5+n+s*b/2, y5+m+b/2),(x6+n+s*b/2, y6+m+b/2),(x7+n+s*b/2, y7+m+b/2)], fill=0)
        draw.polygon([(x1+n+s*b/2, y1+m+b/2),(x8+n+s*b/2, y8+m+b/2),(x9+n+s*b/2, y9+m+b/2),(x10+n+s*b/2, y10+m+b/2)], fill=0)
 img = img.crop((a,b,width,height))
 img.save(f'{output_dir}/{name}_t_{t}.png')
print('ok')

from PIL import Image,ImageDraw
import math,os,random

name='pgg'
output_dir = f'E:/data/test_set/{name}'
os.makedirs(output_dir, exist_ok=True)
i=150
r=3
a=200#basis width
b=200#basis height
width, height = 1600, 1600
for t in range(0,i,1):
 def make_sure(p1, p2, p3):
    # 计算三边长度
    def distance(a, b):
        return math.hypot(a[0]-b[0], a[1]-b[1])
    edge_a = distance(p1, p2)
    edge_b = distance(p2, p3)
    edge_c = distance(p3, p1)
    # 排除任意两边相等
    if math.isclose(edge_a, edge_b, rel_tol=1e-3) or \
       math.isclose(edge_b, edge_c, rel_tol=1e-3) or \
       math.isclose(edge_c, edge_a, rel_tol=1e-3):
        return False
    return True
 img = Image.new("L", (width, height), "white")
 draw = ImageDraw.Draw(img)
 while True:
    x1, y1 = random.randint(r, int(a/4-r)), random.randint(r, int(b/2-r))
    x2, y2 = random.randint(r, int(a/4-r)), random.randint(r, int(b/2-r))
    x3, y3 = random.randint(r, int(a/4-r)), random.randint(r, int(b/2-r))
    points = [
        (x1, y1),
        (x2, y2),
        (x3, y3)
    ]
    if make_sure(points[0], points[1], points[2]):
        break
 x4, y4 = a/2 - x1, b/2 - y1
 x5, y5 = a/2 - x2, b/2 - y2
 x6, y6 = a/2 - x3, b/2 - y3
 x7, y7 = x1 + a/2, b - y1
 x8, y8 = x2 + a/2, b - y2
 x9, y9 = x3 + a/2, b - y3
 x10, y10 = a - x1, b/2 + y1
 x11, y11 = a - x2, b/2 + y2
 x12, y12 = a - x3, b/2 + y3
 for n in range(0, width, a):
    for m in range(0, height, b):
        points = [
            (n+x1, m+y1),
            (n+x2, m+y2),
            (n+x3, m+y3)
        ]
        points_1 = [
            (n+x4, m+y4),
            (n+x5, m+y5),
            (n+x6, m+y6)
        ]
        points_2 = [
            (n+x7, m+y7),
            (n+x8, m+y8),
            (n+x9, m+y9)
        ]
        points_3 = [
            (n+x10, m+y10),
            (n+x11, m+y11),
            (n+x12, m+y12)
        ]

        draw.polygon(points, fill=0)
        draw.polygon(points_1, fill=0)
        draw.polygon(points_2, fill=0)
        draw.polygon(points_3, fill=0)
 img = img.crop((0,0,width,height))
 img.save(f'{output_dir}/{name}_t_{t}.png')
print('ok')





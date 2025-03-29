import math,random,os
from PIL import Image, ImageDraw

name='p1'
output_dir = f'E:/data/test_set/{name}'
os.makedirs(output_dir, exist_ok=True)
r=3
a=100
width, height = 1600, 1600
i=150
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
    x1, y1 = random.randint(r, int(a-r)), random.randint(r, int(a-r))
    x2, y2 = random.randint(r, int(a-r)), random.randint(r, int(a-r))
    x3, y3 = random.randint(r, int(a-r)), random.randint(r, int(a-r))
    points = [
        (x1, y1),
        (x2, y2),
        (x3, y3)
    ]
    if make_sure(points[0], points[1], points[2]):
        break
 for n in range(0, width, a):
    for m in range(0, height, a):
        points = [
            (n+x1, m+y1),
            (n+x2, m+y2),
            (n+x3, m+y3)
        ]
        draw.polygon(points, fill=0)
    img.save(f'{output_dir}/{name}_t_{t}.png')
print('ok')

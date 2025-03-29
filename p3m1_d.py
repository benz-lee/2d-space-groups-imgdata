import math
from PIL import Image, ImageDraw
import random,os

name = 'p3m1'
output_dir = f'E:/data2/{name}'
os.makedirs(output_dir, exist_ok=True)
width, height = 1750, 1905  
k = 6          
i=6         
min_radius = 1
max_radius = 5
w,h=150,173
for t in range(0,i,1):
    img = Image.new('L', (width, height), "white")  
    draw = ImageDraw.Draw(img)
    dots = []  # 存储已生成的点信息，格式为(x, y, radius)
    for _ in range(k):
        radius = random.randint(min_radius, max_radius)
        while True:
            x = random.randint(radius, int(w/3+radius))
            y = random.randint(radius, int(h/2 - radius))
            valid = True
            for (ex_x, ex_y, ex_radius) in dots:
                distance = math.hypot(x - ex_x, y - ex_y)  
                min_distance = radius + ex_radius
                if distance <= min_distance:
                    valid = False
                    break
            if valid:
                dots.append((x, y, radius))#改变生成矩形new
                break    
        for n in range(0, width, 300):
            for m in range(0, height, h):
                dot = [(x - radius+n, y - radius+m), (x + radius+n, y + radius+m)]
                x0,y0=w/3,h/2
                x1=(x-x0)*math.cos(math.radians(120))-(y-y0)*math.sin(math.radians(120))+x0
                y1=(x-x0)*math.sin(math.radians(120))+(y-y0)*math.cos(math.radians(120))+y0
                x2=(x-x0)*math.cos(math.radians(240))-(y-y0)*math.sin(math.radians(240))+x0
                y2=(x-x0)*math.sin(math.radians(240))+(y-y0)*math.cos(math.radians(240))+y0    
                dot1 = [(x1 - radius+n, y1 - radius+m), (x1 + radius+n, y1 + radius+m)]
                dot2 = [(x2 - radius+n, y2 - radius+m), (x2 + radius+n, y2 + radius+m)]  
                dot3 = [(x+w - radius+n, y+h/2 - radius+m), (x+w + radius+n, y+h/2 + radius+m)]
                dot4 = [(x1+w - radius+n, y1+h/2 - radius+m), (x1+w + radius+n, y1+h/2 + radius+m)]
                dot5 = [(x2+w - radius+n, y2+h/2 - radius+m), (x2+w + radius+n, y2+h/2 + radius+m)]
                x_=(math.sqrt(3)*y-x)/2
                y_=(y+math.sqrt(3)*x)/2
                x1_=(math.sqrt(3)*y1-x1)/2
                y1_=(y1+math.sqrt(3)*x1)/2
                x2_=(math.sqrt(3)*y2-x2)/2
                y2_=(y2+math.sqrt(3)*x2)/2
                dot_ = [(x_ - radius+n, y_ - radius+m), (x_ + radius+n, y_ + radius+m)]
                dot1_ = [(x1_ - radius+n, y1_ - radius+m), (x1_ + radius+n, y1_ + radius+m)]
                dot2_ = [(x2_ - radius+n, y2_ - radius+m), (x2_ + radius+n, y2_ + radius+m)]  
                dot3_ = [(x_+w - radius+n, y_+h/2 - radius+m), (x_+w + radius+n, y_+h/2 + radius+m)]
                dot4_ = [(x1_+w - radius+n, y1_+h/2 - radius+m), (x1_+w + radius+n, y1_+h/2 + radius+m)]
                dot5_ = [(x2_+w - radius+n, y2_+h/2 - radius+m), (x2_+w + radius+n, y2_+h/2 + radius+m)]
                draw.ellipse(dot, fill=0)#原
                draw.ellipse(dot1, fill=0)
                draw.ellipse(dot2, fill=0)
                draw.ellipse(dot3, fill=0)#原向右下移动
                draw.ellipse(dot4, fill=0)
                draw.ellipse(dot5, fill=0)
                draw.ellipse(dot_, fill=0)#原对称
                draw.ellipse(dot1_, fill=0)
                draw.ellipse(dot2_, fill=0)
                draw.ellipse(dot3_, fill=0)#原对称向右下移动
                draw.ellipse(dot4_, fill=0)
                draw.ellipse(dot5_, fill=0)
    img = img.crop((0, h, width, height))        
    img.save(f'{output_dir}/{name}_{k}d_{t}.png')
print('ok')

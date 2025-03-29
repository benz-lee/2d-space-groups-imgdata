from PIL import Image,ImageDraw
import math,os,random


name = 'cmm'
output_dir = f'E:/data2/{name}'
os.makedirs(output_dir, exist_ok=True)
width, height = 1600, 1600  
k = 4          
i=6         
min_radius = 1
max_radius = 5
w,h=100,100
for t in range(0,i,1):
    img = Image.new('L', (width, height), "white")  
    draw = ImageDraw.Draw(img)
    dots = []  # 存储已生成的点信息，格式为(x, y, radius)
    for _ in range(k):
        radius = random.randint(min_radius, max_radius)
        while True:
            x = random.randint(radius, int(w/2 - radius))
            y = random.randint(radius, int(h/2 - radius))
            valid = True
            for (ex_x, ex_y, ex_radius) in dots:
                distance = math.hypot(x - ex_x, y - ex_y)  
                min_distance = radius + ex_radius
                if distance <= min_distance:
                    valid = False
                    break
            if valid:
                dots.append((x, y, radius))
                break    
        for n in range(0, width, 2*w):
            for m in range(0, height, 2*h):
                dot = [(x - radius+n, y - radius+m), (x + radius+n, y + radius+m)]
                dot1 = [(w-x - radius+n, y - radius+m), (w-x + radius+n, y + radius+m)]
                dot2 = [(x - radius+n, h-y - radius+m), (x + radius+n, h-y + radius+m)]
                dot3 = [(w-x - radius+n, h-y - radius+m), (w-x + radius+n, h-y + radius+m)]
                dot4 = [(x+w - radius+n, h+y - radius+m), (w+x + radius+n, h+y + radius+m)]
                dot5 = [(2*w-x - radius+n, h+y - radius+m), (2*w-x + radius+n, h+y + radius+m)]
                dot6 = [(x+w - radius+n, 2*h-y - radius+m), (w+x + radius+n, 2*h-y + radius+m)]
                dot7 = [(2*w-x - radius+n, 2*h-y - radius+m), (2*w-x + radius+n, 2*h-y + radius+m)]
                draw.ellipse(dot, fill=0)
                draw.ellipse(dot1,fill=0) 
                draw.ellipse(dot2, fill=0)
                draw.ellipse(dot3, fill=0) 
                draw.ellipse(dot4, fill=0)
                draw.ellipse(dot5, fill=0)
                draw.ellipse(dot6, fill=0)
                draw.ellipse(dot7, fill=0)       
    img.save(f'{output_dir}/{name}_{k}d_{t}.png')
print('ok')

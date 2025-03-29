from PIL import Image,ImageDraw
import os,random,math


name = 'p4m'
output_dir = f'E:/data2/{name}'
os.makedirs(output_dir, exist_ok=True)
width, height = 1600, 1600  
k = 3          
i=6         
min_radius = 1
max_radius = 5
w,h=100,100
for t in range(0,i,1):
    basis = Image.new('L', (int(w/2), int(h/2)), "white")  
    draw = ImageDraw.Draw(basis)
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
                if distance <= min_distance+1:
                    valid = False
                    break
            if valid:
                dots.append((x, y, radius))
                break    
        dot = [(x - radius, y - radius), (x + radius, y + radius)]
        dot1 = [(y - radius, x - radius),(y + radius, x + radius)]
        draw.ellipse(dot, fill=0)
        draw.ellipse(dot1,fill=0)
    img = Image.new('L', (width, height), "white")
    for n in range(0, width, w):
        for m in range(0, height, h):
            img.paste(basis, (n, m))
            img.paste(basis.rotate(90), (n, int(m+h/2)))
            img.paste(basis.rotate(180), (int(n+w/2), int(m+h/2)))
            img.paste(basis.rotate(270), (int(n+w/2), m))
    img.save(f'{output_dir}/{name}_{k}d_{t}.png')
print('ok')
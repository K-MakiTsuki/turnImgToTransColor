from PIL import Image
import math

# 定义颜色映射
blue = (91, 206, 250)
pink = (245, 169, 184)
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

# 定义颜色数组
colors = [blue, pink, white]

# 定义被忽略的颜色的数组
# not_colors = [yellow, black]
not_colors = []

# 定义最小距离
min_distance = 140

# 定义计算颜色距离的函数
def calc_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)

# 定义判断是否为同一个颜色的函数
def is_same_color(color1, color2):
    distance = calc_distance(color1, color2)
    return distance < min_distance

# 打开图片文件
image = Image.open("image.png")

# 转换为RGB模式
rgb_image = image.convert('RGB')

# 新建一个空白图片，大小与原图片相同
new_image = Image.new('RGB', rgb_image.size)

# 遍历每个像素，并将颜色转换为蓝、粉或白
for x in range(rgb_image.width):
    for y in range(rgb_image.height):
        r, g, b = rgb_image.getpixel((x, y))
        if any(is_same_color((r, g, b), color) for color in not_colors):
            # 如果像素点颜色为黄色或黑色，则不进行转换，保留原有颜色
            new_color = (r, g, b)
        else:
            # 否则，将像素点颜色转换为蓝、粉或白
            min_distance_sum = float('inf')
            closest_color = None
            for color in colors:
                distance_sum = 0
                for i in range(3):
                    distance_sum += calc_distance((r, g, b), color)
                if distance_sum < min_distance_sum:
                    min_distance_sum = distance_sum
                    closest_color = color
            new_color = closest_color
        new_image.putpixel((x, y), new_color)

# 保存新图片
new_image.save("new_image.png")

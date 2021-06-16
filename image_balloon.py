from PIL import Image, ImageDraw

def balloon(path, radius):
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    pixels_to_color = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x,y)) == (0, 0, 0, 255):
                #print('true')
                pixels_to_color.append((x,y))

    for i in pixels_to_color:
        x,y = i[0],i[1]
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill = 'black')

    img.save(path.repalce(path[-4:],'_ballooned'+path[-4:]))
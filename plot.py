import json
from PIL import Image, ImageFont, ImageDraw
import os
import requests


#============================#

mapDimentions = 2048
y_addon = -70 # For accuracy with the pin point. Don't mess with this value.

#============================#


try:
    os.remove('Assets/plotted_done.png')
except:
    pass

r = requests.get('https://fortnite-api.com/images/map.png')
open(f'Assets/Apollo_Terrain_Minimap.png', 'wb').write(r.content)
mapimage = Image.open('Assets/Apollo_Terrain_Minimap.png').convert('RGBA')

img = Image.new("RGB", (2048, 2048))
img.paste(mapimage, (0, 0), mapimage)
img.save('Assets/cache.png')

loadFont = 'Assets/BurbankBigCondensed-Black.otf'
draw=ImageDraw.Draw(mapimage)

print('How much locations will you like to plot?')
plotlocs = input('>> ')

locations = []

for i in range(int(plotlocs)):
    print('\nWhat is the X location?')
    x = int(float(input('>> ')))

    print('\nWhat is the Y location?')
    y = int(float(input('>> ')))

    y_1 = ((y+135000)/ (135000*2))*mapDimentions # Calculates Y value

    x_1  = (1-(x+135000)/ (135000*2))*mapDimentions # Calculates X value

    print(f"{y_1}, {x_1}")
    locations.append(f"{y_1}, {x_1}")
    point = i+1

    font=ImageFont.truetype(loadFont,35) # OG = 20
    draw=ImageDraw.Draw(mapimage)
    #draw.text((y_1,x_1),f'{point}',font=font,fill=(255, 201, 23), stroke_width=3, stroke_fill=(0, 0, 255))

    pin= Image.open('Assets/mappin.png').resize((46, 80)).convert('RGBA')
    mapimage.paste(pin, (int(y_1),int(x_1+y_addon)), pin)

    mapimage.save('Assets/cache.png')

os.rename('Assets/cache.png', 'Assets/plotted_done.png')

print(locations)

import pygame, sys
from pygame.locals import *
import math
from PIL import Image, ImageDraw

red = (230, 30, 30)
blue = (30, 30, 230)
green = (20, 220, 10)

duvar = [[10, 10], [450, 10], [450, 200], [550, 200], [910, 30], 
         [910, 550], [550, 550], [550, 300], [450, 300],
         [450, 590], [10, 590]]

pos = [730, 420]
angle = 180
llen = 300

degerler = []

window = pygame.display.set_mode((1000, 600))
window.fill((100, 100, 100))


image = Image.new("RGB", (1000, 600), "black")


def map():
    for n in range(len(duvar) - 1):
        pygame.draw.line(window, red, (duvar[n][0], duvar[n][1]), (duvar[n + 1][0], duvar[n + 1][1]), 5)
    pygame.draw.line(window, red, (duvar[len(duvar) - 1][0], duvar[len(duvar) - 1][1]), (duvar[0][0], duvar[0][1]), 5)

    for n in range(len(duvar)):
        pygame.draw.circle(window, blue, (duvar[n][0], duvar[n][1]), 7)

def lazer(pos, a, l):
    pygame.draw.line(window, blue, (pos[0], pos[1]), (pos[0] + l * math.cos(math.radians(a)), 
                                                     pos[1] + l * math.sin(math.radians(a))), 3)

def degdi(x, y):
    for n in range(len(duvar) - 1):
        if((duvar[n + 1][1] - duvar[n][1]) == 0):
            if(duvar[n][0] < duvar[n + 1][0]):
                if(x > duvar[n][0] and x < duvar[n + 1][0] and -0.5 < abs(y - duvar[n][1]) and 0.5 > abs(y - duvar[n][1])):
                    return True
            else:
                if(x < duvar[n][0] and x > duvar[n + 1][0] and -0.5 < abs(y - duvar[n][1]) and 0.5 > abs(y - duvar[n][1])):
                    return True 

        elif((duvar[n + 1][0] - duvar[n][0]) == 0):
            if(duvar[n][1] < duvar[n + 1][1]):
                if(y > duvar[n][1] and y < duvar[n + 1][1] and -0.5 < abs(x - duvar[n][0]) and 0.5 > abs(x - duvar[n][0])):
                    return True
            else:
                if(y < duvar[n][1] and y > duvar[n + 1][1] and -0.5 < abs(x - duvar[n][0]) and 0.5 > abs(x - duvar[n][0])):
                    return True  
                
        else:
            md = (duvar[n + 1][1] - duvar[n][1]) / (duvar[n + 1][0] - duvar[n][0])
            nd = duvar[n][1] - md * duvar[n][0]
            yd = md * x + nd

            if(-0.5 < abs(yd - y) and 0.5 > abs(yd - y)):
                return True
                
    return False

def olcum():
    for i in range(angle):
        for l in range(llen):
            lazer(pos, i * (360 / angle), l)
            if(degdi(pos[0] + l * math.cos(math.radians(i * (360 / angle))), pos[1] + l * math.sin(math.radians(i * (360 / angle))))):
                degerler.append([pos[0] + l * math.cos(math.radians(i * (360 / angle))), pos[1] + l * math.sin(math.radians(i * (360 / angle))), 0, i])
                break

    list1 = [n[3] for n in degerler]
    list2 = [n for n in range(angle)]
    list3 = []
    for e in list2:
        if e not in list1:
            list3.append(e)
            degerler.append([pos[0] + llen * math.cos(math.radians(e * (360 / angle))), pos[1] + llen * math.sin(math.radians(e * (360 / angle))), 1, e])

    degerler.append([pos[0] + llen * math.cos(math.radians(list3[0] * (360 / angle))), pos[1] + llen * math.sin(math.radians(list3[0] * (360 / angle))), 2, list3[0]])
    degerler.append([pos[0] + llen * math.cos(math.radians(list3[len(list3) - 1] * (360 / angle))), pos[1] + llen * math.sin(math.radians(list3[len(list3) - 1] * (360 / angle))), 2, list3[0]])
    for i in range(len(list3) - 1):
        if list3[i] + 1 != list3[i + 1]:
            degerler.append([pos[0] + llen * math.cos(math.radians(list3[i] * (360 / angle))), pos[1] + llen * math.sin(math.radians(list3[i] * (360 / angle))), 2, list3[i]])
            degerler.append([pos[0] + llen * math.cos(math.radians(list3[i + 1] * (360 / angle))), pos[1] + llen * math.sin(math.radians(list3[i + 1] * (360 / angle))), 2, list3[i + 1]])


map()
olcum()
pygame.draw.circle(window, green, (pos[0], pos[1]), 10)


for n in degerler:
    if(n[2] == 0):
        pygame.draw.circle(window, green, (n[0], n[1]), 5)
        ImageDraw.Draw(image).line([(pos[0], pos[1]), (n[0], n[1])], fill="white", width=1)
        for x in range(3):
            for y in range(3):
                image.putpixel((int(n[0] + x - 1), int(n[1] + y - 1)), green)

    if(n[2] == 1):
        pygame.draw.circle(window, red, (n[0], n[1]), 5)
        ImageDraw.Draw(image).line([(pos[0], pos[1]), (n[0], n[1])], fill="white", width=1)
        for x in range(3):
            for y in range(3):
                image.putpixel((int(n[0] + x - 1), int(n[1] + y - 1)), red)

    if(n[2] == 2):
        pygame.draw.circle(window, red, (n[0], n[1]), 5)
        ImageDraw.Draw(image).line([(pos[0], pos[1]), (n[0], n[1])], fill="white", width=1)
        image.putpixel((int(n[0]), int(n[1])), blue)

""""
for x in range(6):
    for y in range(6):
        pos = [730 + (x - 1) * 20, 420 + (y - 1) * 20]
        olcum()

for n in degerler:
    if(n[2] == 0):
        pygame.draw.circle(window, green, (n[0], n[1]), 5)
        ImageDraw.Draw(image).line([(pos[0], pos[1]), (n[0], n[1])], fill="white", width=1)
        for x in range(3):
            for y in range(3):
                image.putpixel((int(n[0] + x - 1), int(n[1] + y - 1)), green)

    if(n[2] == 1):
        pygame.draw.circle(window, red, (n[0], n[1]), 5)
        ImageDraw.Draw(image).line([(pos[0], pos[1]), (n[0], n[1])], fill="white", width=1)
        for x in range(3):
            for y in range(3):
                image.putpixel((int(n[0] + x - 1), int(n[1] + y - 1)), red)
"""

image.show()
image.save("beyaz_resim.png")

while False:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
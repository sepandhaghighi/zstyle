# -*- coding: utf-8 -*-
import random
import math
import os
import matplotlib.pyplot as plt
import art
from samila import GenerativeImage, Projection

DETAILS_TEMPLATE = """F1 : {0}

F2 : {1}

Seed : {2}

Color : {3}

Spot Size : {4}
"""

INTRO_MESSAGE = """This code create Z-style generative art NFTs that can serve as unique memorabilia and avatars.
The method used in this project is based on our other library called Samila.
"""

def f1(x,y):
    result = random.uniform(1,10) * y + random.uniform(0.25,2) * math.cos(-x + y)
    return result

def f2(x,y):
    result = random.uniform(1,100) * math.sin(y) + random.uniform(1,40) * math.sin(abs(x-y))
    return result

def f3(x,y):
    result = random.uniform(1,20) * y**3 - random.uniform(1,20) * math.cos(x**2) + x
    return -1 * result

def line(char="*", num=70):
    """
    Print line of characters.

    :param char: character
    :type char: str
    :param num: number of characters
    :return: None
    """
    print(num * char)


if __name__ == "__main__":
    folder_path = os.path.join(os.getcwd(),"Z_Style")
    nft_num = 100
    art.tprint("Generative ART")
    line()
    print(INTRO_MESSAGE)
    line()
    functions_dict = {"F1":f1, "F2":f2, "F3":f3}
    functions_pair = [["F1","F3"],["F2","F3"],["F1","F2"]]
    for item in range(nft_num):
        print("File : {0}".format(item + 1))
        file_path = os.path.join(folder_path,str(item+1))
        color_r = round(random.uniform(0,0.5),3)
        color_g = round(random.uniform(0,0.5), 3)
        color_b = round(random.uniform(0,0.5), 3)
        color = (color_r,color_g,color_b)
        spot_size = random.uniform(0.1, 2)
        [f1_name, f2_name] = random.choice(functions_pair)
        g = GenerativeImage(functions_dict[f1_name], functions_dict[f2_name])
        g.generate()
        g.plot(color = color, spot_size=spot_size)
        g.save_image(file_adr=file_path + ".png")
        details = DETAILS_TEMPLATE.format(f1_name,f2_name,g.seed,color,spot_size)
        with open(file_path + ".txt","w") as details_file:
            details_file.write(details)
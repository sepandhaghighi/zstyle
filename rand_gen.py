# -*- coding: utf-8 -*-
import random
import os
import art
import math
from samila import GenerativeImage, Projection, VALID_COLORS

ELEMENTS_LIST = ["{0}*math.cos({1})**{2}","{0}*math.sin({1})**{2}","{0}*{1}**{2}","{0}*math.ceil({1})**{2}","{0}*abs({1})**{2}","{0}*math.floor({1})**{2}"]

ARGUMENT_LIST = ["x*y","x","y","y-x","x-y","x+y","x**2","y**2","x**2*y","y**2*x"]

OPERATORS_LIST = ["+","-"]

DETAILS_TEMPLATE = """F1 : {0}

F2 : {1}

Seed : {2}

Color : {3}

Projection : {4}

Spot Size : {5}
"""

INTRO_MESSAGE = """This code create generative art NFTs that can serve as unique memorabilia, wallpapers or even avatars.
The method used in this project is based on our other library called Samila.
"""

def random_equation_gen():
    """
    Generate random equation.

    :return: equation as str
    """
    num_elements = random.randint(1,len(ELEMENTS_LIST))
    result = ""
    index = 1
    while(index<=num_elements):
        random_coef1 = round(random.uniform(1,50),3)
        random_coef2 = round(random.uniform(1,2), 3)
        argument = random.choice(ARGUMENT_LIST)
        result = result + random.choice(ELEMENTS_LIST).format(str(random_coef1),argument,str(random_coef2))
        if index<num_elements:
            result = result + random.choice(OPERATORS_LIST)
        index = index + 1
    return result


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
    folder_path = os.path.join(os.getcwd(),"Rand_NFT")
    nft_num = 50
    art.tprint("Generative ART")
    line()
    print(INTRO_MESSAGE)
    line()
    for item in range(nft_num):
        print("File : {0}".format(item + 1))
        file_path = os.path.join(folder_path,str(item+1))
        f1_str = random_equation_gen()
        f2_str = random_equation_gen()
        f1 = lambda x,y : eval(f1_str)
        f2 = lambda x,y : eval(f2_str)
        projection = random.choice([Projection.POLAR, Projection.RECTILINEAR])
        color_r = round(random.uniform(0,0.5),3)
        color_g = round(random.uniform(0,0.5), 3)
        color_b = round(random.uniform(0,0.5), 3)
        color = (color_r,color_g,color_b)
        spot_size = random.uniform(0.1, 2)
        g = GenerativeImage(f1,f2)
        g.generate()
        g.plot(projection=projection, color = color, spot_size=spot_size)
        g.save_image(file_adr=file_path + ".png")
        details = DETAILS_TEMPLATE.format(f1_str,f2_str,g.seed,color,projection,spot_size)
        with open(file_path + ".txt","w") as details_file:
            details_file.write(details)





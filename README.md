<div align="center">
<img src="otherfiles/logo.png" width=400 height=400>
<br/>
<h1>Zil Gen</h1>
</div>

----------

## Overview



<p align="justify">	
In this work I tried to generate generative arts for <a href="https://gitcoin.co/issue/Zilliqa/Zilliqa/2714/100026476">[ZILLIQA ON GITCOIN: NFTs BEYOND ART] Generative Art Pieces</a> that can serve as unique memorabilia or even avatars.
This project is based on our other library called <a href="https://github.com/sepandhaghighi/samila">Samila</a> and consist of two main part:

1. Generative Wallpapers
2. Generative Z-Style Avatars

</p>


## Requirements

1. [Samila](https://github.com/sepandhaghighi/samila)
2. [Art](https://github.com/sepandhaghighi/art)

`pip3 install -r requirements.txt`

## Generative Wallpapers

`python3 rand_gen.py`

This part lets you create infinite unique wallpapers based on many thousand points. The position of every single point is calculated by a formula, which has random parameters. Because of the random numbers, every image looks different.

Parameters :

1. Input formula
2. Projection
3. Color
4. Spot size

### Sample1
<img src="" width=400 height=400>
```
```

### Sample2
<img src="" width=400 height=400>
```
```

### Sample3
<img src="" width=400 height=400>
```
```

For more example take a look at [Wallpapers]() folder


## Z-Style Avatars

`python3 rand_gen.py`

This part lets you create infinite unique z-style avatars based on many thousand points. The position of every single point is calculated by a formula, which has random parameters. Because of the random numbers, every image looks different.

Parameters :

1. Input formula
2. Color
3. Spot size

### Sample1
<img src="" width=400 height=400>
```
```

### Sample2
<img src="" width=400 height=400>
```
```

### Sample3
<img src="" width=400 height=400>
```
```

For more example take a look at [Z-Style]() folder

## Technical Details
A transformation between a square-shaped space from the Cartesian coordinate system to any arbitrary coordination like [Polar coordinate system](https://en.wikipedia.org/wiki/Polar_coordinate_system).

### Example
<img src="otherfiles/transformation.png">

We have set of points in the first space (left square) which can be define as follow:

<img src="otherfiles/S1.jpg">

And bellow functions are used for transformation:

```pycon
>>> def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
>>> def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result
```

<img src="otherfiles/S2.jpg">

here we uses `Projection.POLAR` so later space will be the polar space and we have:

```pycon
>>> g = GenerativeImage(f1,f2)
>>> g.generate(seed=10)
>>> g.plot(projection=Projection.POLAR)
```
<img src="otherfiles/S2_.jpg">

<img src="otherfiles/6.png">


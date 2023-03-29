from typing import List, Dict
from PIL import Image

# In all formulas we switch x and y due to Pillow coordinate system
 
def m(f: List[List[int]], p: int, q: int) -> int:
    res = 0
    for y in range(len(f)):
        for x in range(len(f[y])):
            res += (y ** p) * (x ** q) * f[y][x]

    return res

def mu(f: List[List[int]], p: int, q: int) -> float:
    m00 = m(f, 0, 0)
    y_dash = m(f, 1, 0) / m00
    x_dash = m(f, 0, 1) / m00

    res = 0
    for y in range(len(f)):
        for x in range(len(f[y])):
            res += ((y - y_dash) ** p) * ((x - x_dash) ** q) * f[y][x]

    return res

def eta(f: List[List[int]], p: int, q: int) -> float:
    if (p + q < 2):
        raise Exception('Eta is defined only for p + q >= 2')
    
    gamma = (p + q) / 2 + 1
    
    return mu(f, p, q) / (mu(f, 0, 0) ** gamma)

def Phi1(f: List[List[int]]) -> float:
    return eta(f, 2, 0) + eta(f, 0, 2)

def Phi2(f: List[List[int]]) -> float:
    return (eta(f, 2, 0) - eta(f, 0, 2)) ** 2 + 4 * (eta(f, 1, 1) ** 2)

def image_Phi1_Phi2(image: Image.Image) -> Dict[str, float]:
    image_pixels_intensity = []

    for y in range(image.height):
        image_pixels_intensity.append([])
        for x in range(image.width):
            image_pixels_intensity[-1].append(image.getpixel((x, y)))
    
    return {'Phi1': Phi1(image_pixels_intensity), 'Phi2': Phi2(image_pixels_intensity)}
from typing import List, Dict, Iterable
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

def image_Phi1Phi2(image: Image.Image) -> Dict[str, float]:
    image_pixels_intensity = []

    for y in range(image.height):
        image_pixels_intensity.append([])
        for x in range(image.width):
            image_pixels_intensity[-1].append(image.getpixel((x, y)))
    
    return {'Phi1': Phi1(image_pixels_intensity), 'Phi2': Phi2(image_pixels_intensity)}

def euclidean_distance(dim: int, p: Iterable[float], q: Iterable[float]) -> float:
    if (dim < 1):
        raise Exception(f'Wrong input in euclidean distance. dim should be integer >= 1')        
    if (len(p) != dim and len(p) != len(q)):
        raise Exception(f'Wrong input in euclidean distance. p,q should be 2 iterables of {dim} length')
    
    res = 0
    for i in range(dim):
        res += (p[i] - q[i]) ** 2
    
    return res ** 0.5

def distances_to_standart_Phi1Phi2(Phi1Phi2: Dict[str, float], standartImageNames: List[str]) -> Dict[str, Dict[str, float]]:
    imageToClassifyNames = [key for key in Phi1Phi2.keys() if key not in standartImageNames]

    Phi1Phi2_distances = {}

    for imageToClassifyName in imageToClassifyNames:
        Phi1Phi2_distances[imageToClassifyName] = {'Phi1': {}, 'Phi2': {}, 'Phi1Phi2': {}}
        for standartImageName in standartImageNames:
            Phi1Phi2_distances[imageToClassifyName]['Phi1'][standartImageName] = euclidean_distance(1, [Phi1Phi2[imageToClassifyName]['Phi1']], [Phi1Phi2[standartImageName]['Phi1']])
            Phi1Phi2_distances[imageToClassifyName]['Phi2'][standartImageName] = euclidean_distance(1, [Phi1Phi2[imageToClassifyName]['Phi2']], [Phi1Phi2[standartImageName]['Phi2']])
            Phi1Phi2_distances[imageToClassifyName]['Phi1Phi2'][standartImageName] = euclidean_distance(2, [Phi1Phi2[imageToClassifyName]['Phi1'], Phi1Phi2[imageToClassifyName]['Phi2']], [Phi1Phi2[standartImageName]['Phi1'], Phi1Phi2[standartImageName]['Phi2']])
    
    return Phi1Phi2_distances
from os import path
from traceback import print_exc
from PIL import Image
from calculations import image_Phi1Phi2, distances_to_standart_Phi1Phi2, classify
from utils import Phi1Phi2_info_print, distances_to_standart_Phi1Phi2_info_print

if __name__ == "__main__":
    try:
        # setting images names and paths
        imagesFolder = 'assets/'

        standartImageNames = ['a.bmp', 'b.bmp', 'f.bmp', 'm.bmp']
        standartImageInfo = {standartImageName : path.abspath(f'{imagesFolder + standartImageName}') for standartImageName in standartImageNames}

        imageToClassifyNames = ['a1.bmp', 'a2.bmp', 'b1.bmp', 'f1.bmp', 'm1.bmp']
        imageToClassifyInfo = {imageToClassifyName : path.abspath(f'{imagesFolder + imageToClassifyName}') for imageToClassifyName in imageToClassifyNames}

        imagesInfo = dict(standartImageInfo, **imageToClassifyInfo)

        # getting Phi1, Phi2
        Phi1Phi2 = {}
        for imageName, imagePath in imagesInfo.items():
            with Image.open(imagePath) as im:
                im = im.convert("L")
                Phi1Phi2[imageName] = image_Phi1Phi2(im)

        # printing Phi1, Phi2 results
        Phi1Phi2_info_print(Phi1Phi2, standartImageNames)
        
        # getting distances
        distances_to_standart_Phi1Phi2_res = distances_to_standart_Phi1Phi2(Phi1Phi2, standartImageNames)

        # getting classification
        classification = classify(distances_to_standart_Phi1Phi2_res)

        # printing distances with classification
        distances_to_standart_Phi1Phi2_info_print(distances_to_standart_Phi1Phi2_res, standartImageNames, classification)

    except Exception as e:
        print('Error occured:')
        print_exc()
from os import path
from traceback import print_exc
from PIL import Image
from calculations import image_Phi1_Phi2

if __name__ == "__main__":
    try:
        imagesFolder = 'assets/'

        standartImageNames = ['a.bmp', 'b.bmp', 'f.bmp', 'm.bmp']
        standartImageInfo = {standartImageName : path.abspath(f'{imagesFolder + standartImageName}') for standartImageName in standartImageNames}

        imageToClassifyNames = ['a1.bmp', 'a2.bmp', 'b1.bmp', 'f1.bmp', 'm1.bmp']
        imageToClassifyInfo = {imageToClassifyName : path.abspath(f'{imagesFolder + imageToClassifyName}') for imageToClassifyName in imageToClassifyNames}

        imagesInfo = dict(standartImageInfo, **imageToClassifyInfo)
        Phi1Phi2 = {}

        for imageName, imagePath in imagesInfo.items():
            with Image.open(imagePath) as im:
                im = im.convert("L")
                Phi1Phi2[imageName] = image_Phi1_Phi2(im)

        noDrift = 1 
        for key in imagesInfo.keys():
            if noDrift and key in imageToClassifyNames:
                noDrift = 0
                print()
            print(key, Phi1Phi2[key])

    except Exception as e:
        print('Error occured:')
        print_exc()
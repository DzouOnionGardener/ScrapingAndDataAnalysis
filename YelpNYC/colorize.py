import cv2
import numpy as np
import csv
import os

def colorize(BusinessName, average):
    try:
        image = cv2.imread('map/manhattan.png') if (os.path.isfile('map/NYC.png') ==  False) else cv2.imread('map/NYC.png')
        ManhattanImage = image
        csvFile = open('Manhattan.csv', 'rU')
        reader = csv.reader(csvFile, delimiter=',')
        restaurants = []
        rows = 0
        for row in reader:
            restaurants.append(row)
            rows += 1
        csvFile.close()
        for row in restaurants:
            if BusinessName in row:
                RestaurantIndex = 0
                RestaurantIndex = restaurants.index(row)
                #acquire RGB
                r = int(restaurants[RestaurantIndex][1])
                g = int(restaurants[RestaurantIndex][2])
                b = int(restaurants[RestaurantIndex][3])                                                          
                if average == 1.00 or average <= 1.20:                                      ##R    G    B
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [191, 189, 255]
                elif average == 1.20 or average < 1.40:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [176, 173, 242]
                elif average == 1.40 or average < 1.60:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [161, 157, 229]
                elif average == 1.60 or average < 1.80:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [146, 141, 217]
                elif average == 1.80 or average < 2.00:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [131, 126, 204]
                elif average == 2.00 or average < 2.20:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [116, 110, 192]
                elif average == 2.20 or average < 2.40:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [101, 94, 179]
                elif average == 2.40 or average < 2.60:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [87, 78, 167]
                elif average == 2.60 or average < 2.80:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [72, 63, 154]
                elif average == 2.80 or average < 3.00:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [57, 47, 142]
                elif average == 3.00 or average < 3.20:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [42, 31, 129]
                elif average == 3.20 or average < 3.40:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [28, 16, 117]
                elif average == 3.40 or average < 3.60:
                     ManhattanImage[np.where(( ManhattanImage == [b, g, r]).all(axis=2))] = [17, 7, 86]
        im = ManhattanImage
        cv2.imwrite('map/NYC.png', im)
    except:
        pass

"""

imageBIN = np.array(image)
red, green, blue, alpha = imageBIN.T
##RGBA = (128,128,128)
#(0, 64, 64)
grayAreas = (red == 0) & (blue == 64) & (green == 64)
imageBIN[..., :-1][grayAreas.T] = (128, 128, 128)
im2 = Image.fromarray(imageBIN)
im2.save('/home/dzou/Desktop/NYC_MAP.png')
im2.show()

                R     G    B              avg
starting color:
                255, 189, 191      1.00 - 1.20
                242, 173, 176      1.20 - 1.40
                229, 157, 161      1.40 - 1.60
                217, 141, 146      1.60 - 1.80
                204, 126, 131      1.80 - 2.00
                192, 110, 116      2.00 - 2.20
                190, 053, 230      2.20 - 2.40
                167, 078, 087      2.40 - 2.60
                154, 063, 072      2.60 - 2.80
                142, 047, 057      2.80 - 3.00
                129, 031, 042      3.00 - 3.20
                117, 016, 028      3.20 - 3.40
                086, 007, 017      3.40 - 3.60
"""

##store image area coordinates

if __name__ == "__main__":
    colorize("boob", 5.5)
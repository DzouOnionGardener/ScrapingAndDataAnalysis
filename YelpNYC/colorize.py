import Image
import numpy as np
import csv
import os

def colorize(BusinessName, average):
    try:
        image = Image.open('map/manhattan.png') if (os.path.isfile('map/NYC.png') == False) else Image.open('map/NYC.png')
        image = image.convert('RGBA')
        manhattanBIN = np.array(image) ##turns image into an array of pixel values
        red, green, blue = manhattanBIN[:,:,0], manhattanBIN[:,:,1],manhattanBIN[:,:,2]
        print average
        with open('map/Manhattan.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if row[0] == BusinessName:
                    print row[0], row[1], row[2], row[3]
                    r = int(row[1])
                    g = int(row[2])
                    b = int(row[3])
                    areaColor = (red == r) & (green == g) & (blue == b) ##select the RGB color from the CSV
                    ##set color based on average range
                    if average == 1.00 and average < 1.20:
                        manhattanBIN[:, :, :3][areaColor] = (255, 189, 191)
                    if average == 1.20 and average < 1.40:
                        manhattanBIN[:, :, :3][areaColor] = (242, 173, 176)
                    if average == 1.40 and average < 1.60:
                        manhattanBIN[:, :, :3][areaColor] = (229, 157, 161)
                    if average == 1.60 and average < 1.80:
                        manhattanBIN[:, :, :3][areaColor] = (217, 141, 146)
                    if average == 1.80 and average < 2.00:
                        manhattanBIN[:, :, :3][areaColor] = (204, 126, 131)
                    if average == 2.00 and average < 2.20:
                        manhattanBIN[:, :, :3][areaColor] = (192, 110, 116)
                    if average == 2.20 and average < 2.40:
                        manhattanBIN[:, :, :3][areaColor] = (179, 94, 101)
                    if average == 2.40 and average < 2.60:
                        manhattanBIN[:, :, :3][areaColor] = (167, 78, 87)
                    if average == 2.60 and average < 2.80:
                        manhattanBIN[:, :, :3][areaColor] = (154, 63, 72)
                    if average == 2.80 and average < 3.00:
                        manhattanBIN[:, :, :3][areaColor] = (142, 47,57)
                    if average == 3.00 and average < 3.20:
                        manhattanBIN[:, :, :3][areaColor] = (129, 31, 42)
                    if average == 3.20 and average < 3.40:
                        manhattanBIN[:, :, :3][areaColor] = (117, 16, 28)
                    if average == 3.40 and average < 3.60:
                        manhattanBIN[:, :, :3][areaColor] = (86, 7, 17)
            csvfile.close()
        im = Image.fromarray(manhattanBIN)
        im.save('map/NYC.png')
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
import Image
import numpy as np

image = Image.open('./neighborhoodsfinancial_District.png')
image = image.convert('RGBA')

imageBIN = np.array(image)
red, green, blue, alpha = imageBIN.T
##RGBA = (128,128,128)
grayAreas = (red == 128) & (blue == 128) & (green == 128)
imageBIN[..., :-1][grayAreas.T] = (255, 0, 0)
im2 = Image.fromarray(imageBIN)
im2.save('cFinancialDistrict.png')
im2.show()


"""
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
import cv2

'''
    Syntax: cv2.imread(path, flag)
    
    Parameters:
    path: A string representing the path of the image to be read.
    flag: It specifies the way in which image should be read. It’s default value is cv2.IMREAD_COLOR
    
    Return Value: This method returns an image that is loaded from the specified file.
    
    cv2.IMREAD_COLOR: It specifies to load a color image. 
    Any transparency of image will be neglected. It is the default flag. 
    Alternatively, we can pass integer value 1 for this flag.
    
    cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. 
    Alternatively, we can pass integer value 0 for this flag.
    
    cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. 
    Alternatively, we can pass integer value -1 for this flag.
'''


source = "motivationalImage.jpg"
destination = './resizedImage3.jpg'
# Percent by which the image is resized
scale_percent = 50


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# todo  displaying the image
cv2.imshow("title", src)

#todo  calculating the 50 percent of original dimension
new_width = int(src.shape[1] * scale_percent/ 100)
new_height = int(src.shape[0] * scale_percent/ 100)

# dsize
dsize = (new_width, new_height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)
cv2.waitKey(0)
from PIL import Image as im
import numpy as np

def pure_pil_alpha_to_color(image, color=(255, 255, 255)):
    try:
        image.load()  # needed for split()
        background = im.new('RGB', image.size, color)
        background.paste(image, mask=image.split()[3])  # 3 is the alpha channel
    except IndexError:
        image.load()  # needed for split()
        background = im.new('RGB', image.size, color)
        background.paste(image)
    return background
    

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    gray /= 255
    gray = np.around(gray,2)
    return gray

class feature:
    #Return a 10X10 array from a monochrome BMP Image
    @staticmethod
    def getImageArray(imagepath):
        try:
          image = im.open(imagepath)
          image = pure_pil_alpha_to_color(image)
          imagearray=np.asarray(image.crop(image.getbbox()).resize((12,15))).astype(float)
          imagearray = rgb2gray(imagearray)
          return imagearray
        except IOError:
           print "\n\n File Not Found"
           return np.zeros((10,10))
    
    # Normalizes a 2D array cell.
    @staticmethod
    def normalizeArrayCell( array, x, y):
        for c in range(1,5):
            for i in range(x-c,x+c+1):
                for j in range(y-c, y+c+1):
                    if i<=9 and i>=0 and j<=9 and j>=0:
                        if array[i,j] < array[x,y] and array[i,j] < array[x,y]-0.2*c:
                            array[i,j]=array[x,y]-0.2*c
    
    # Returns a Normalized 2D Array from an Input Array. 
    # normalizeArrayCell is called for all non zero cells
    @staticmethod
    def getNormalizedArray( imagearray):
        nonzerocells = np.transpose(imagearray.nonzero())
        for i in range (0, nonzerocells.shape[0]):
            feature.normalizeArrayCell(imagearray, nonzerocells[i][0],nonzerocells[i][1])
        return imagearray
    
    # Returns Normalized 2D array from an Image
    @staticmethod
    def getNormalizedImageArray( imagepath):
        return feature.getNormalizedArray(feature.getImageArray(imagepath))
    
    # Returns Feature Vector of an Image
    @staticmethod
    def getImageFeatureVector( imagepath):
        array = feature.getNormalizedImageArray(imagepath)
        vector = np.resize(array,(1,500))
        return vector[0]

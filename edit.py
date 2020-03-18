#%%
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def showImg(img_path):
    #print(mpimg.imread(img_path))
    plt.imshow(mpimg.imread(img_path))

def getImagesFromDir(dir_path):
    paths = []

    for image_file in os.listdir(dir_path):
        if image_file.endswith(".jpg"):
            paths.append( os.path.join(dir_path, image_file))

    return paths



#%%
starting_dir = "./cards"
showImg(getImagesFromDir(starting_dir)[0])

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


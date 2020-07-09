#
# Created by Cognolato Samuel 1237767 and Fusaro Daniel 1233437
#
import glob, os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import xml.etree.ElementTree as ET
import shutil

sp = {}

#NOTE: absolute paths must be used!

target_train = '/train/'
target_test = '/test/'
path_train1 = '/ImageCLEF2013PlantTaskTrainPackage-PART-1/train/'
path_train2 = '/ImageCLEF2013PlantTaskTrainPackage-PART-2/train/'
path_test = '/ImageCLEF2013PlantTaskTestAndTaskPackage/TestAndTaskPackage/Data/Test/'
ground_test = '/ImageCLEF2013PlantTaskTestAndTaskPackage/TestAndTaskPackage/Data/GroundTruth/'

print("STARTING FROM path_train1")

os.chdir(path_train1)

for file in glob.glob("*.xml"):

    tree = ET.parse(file)
    root = tree.getroot()

    image = root.iter('Image')
    classID = root.find('ClassId').text
    content = root.find('Content').text
    typ = root.find('Type').text
    
    if content=='Leaf' and typ=='SheetAsBackground' and (classID=='Fraxinus angustifolia' or classID == 'Liquidambar styraciflua' or classID == 'Ruscus aculeatus' or classID == 'Vitex agnus-castus' or classID=='Phillyrea angustifolia'):
        fn = root.find('FileName').text
        shutil.copy(path_train1+fn, target_train+fn) # copy the image jpg
        shutil.copy(path_train1+file, target_train+file) # copy the xml
        print(fn)
        

print("STARTING FROM path_train2")
os.chdir(path_train2)

for file in glob.glob("*.xml"):

    tree = ET.parse(file)
    root = tree.getroot()

    image = root.iter('Image')
    classID = root.find('ClassId').text
    content = root.find('Content').text
    typ = root.find('Type').text
    
    if content=='Leaf' and typ=='SheetAsBackground' and (classID=='Fraxinus angustifolia' or classID == 'Liquidambar styraciflua' or classID == 'Ruscus aculeatus' or classID == 'Vitex agnus-castus' or classID=='Phillyrea angustifolia'):
        fn = root.find('FileName').text
        shutil.copy(path_train2+fn, target_train+fn) # copy the image jpg
        shutil.copy(path_train2+file, target_train+file) # copy the xml
        print(fn)


print("STARTING FROM path_test")
os.chdir(ground_test)

for file in glob.glob("*.xml"):

    tree = ET.parse(file)
    root = tree.getroot()

    image = root.iter('Image')
    classID = root.find('ClassId').text
    content = root.find('Content').text
    typ = root.find('Type').text
    
    if content=='Leaf' and typ=='SheetAsBackground' and (classID=='Fraxinus angustifolia' or classID == 'Liquidambar styraciflua' or classID == 'Ruscus aculeatus' or classID == 'Vitex agnus-castus' or classID=='Phillyrea angustifolia'):
        fn = root.find('FileName').text
        shutil.copy(path_test+fn, target_test+fn)   # copy the image jpg
        shutil.copy(ground_test+file, target_test+file) # copy the xml
        print(fn)
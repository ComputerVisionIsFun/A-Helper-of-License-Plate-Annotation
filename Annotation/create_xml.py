import xml.etree.ElementTree as ET
import numpy as np
import random
import os
import cv2


def create_xml(folder, filename, objs, sample_xml_path, new_xml_save_path, img_w, img_h, img_d,obj_name):
    '''
    objs = [obj0, obj1, ...], where obji = [[xmin,ymin], [], [xmax,ymax], []]

    '''
    # read xml
    tree = ET.parse(sample_xml_path)
    root = tree.getroot()
    # assign folder, filename, path
    root.find('folder').text = folder
    root.find('filename').text = filename
    root.find('path').text = folder + filename
    
    # assign width and height
    root.find('size').find('width').text = str(int(img_w))
    root.find('size').find('height').text = str(int(img_h))
    root.find('size').find('depth').text = str(int(img_d))

    # create objs
    for obj in objs:
        print(obj[0][0],'\n')
        xmin, ymin = str(obj[0][0][0]), str(obj[0][0][1])
        xmax, ymax = str(obj[0][2][0]), str(obj[0][2][1]) 
        new_element = create_an_object(obj_name, xmin, ymin, xmax, ymax)
        root.insert(6, new_element)

    # write to a new xml
    tree.write(new_xml_save_path)



def create_an_object(name:str, xmin:str, ymin:str, xmax:str, ymax:str):
    obj_elements = ['name','pose','truncated','difficult','bndbox']
    new_element = ET.Element('object')
    
    # 
    for obj_element in obj_elements:
        ET.SubElement(new_element, obj_element)
        ET.dump(new_element)

    new_element[0].text = name
    new_element[1].text = 'Unspeicfied'
    new_element[2].text = '0'
    new_element[3].text = '0'
    
    # check 
    # print(float(xmin), float(xmax), float(ymin), float(ymax))
    if float(xmin)>=float(xmax) or float(ymin)>=float(ymax): 
        print('ValueError:xmin>=xmax or ymin>=ymax')
        return 

    # edit bndbox
    bndbox_elements = ['xmin','ymin','xmax','ymax']
    for i, ele in enumerate(bndbox_elements):
        ET.SubElement(new_element[4], ele)#add ele in {xmin, xmax, ymin, ymax} to new_element[4]=bndbox
        ET.dump(new_element[4])

        if ele=='xmin':
            new_element[4][i].text = xmin
        elif ele=='ymin':
            new_element[4][i].text = ymin
        elif ele=='xmax':
            new_element[4][i].text = xmax
        else:
            new_element[4][i].text = ymax

    return new_element

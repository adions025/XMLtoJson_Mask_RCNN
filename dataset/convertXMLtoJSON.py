"""
converterXMLtoJSON

Detect all annotations in xml files (bounding boxes) and convert to json (polygon shape)
It works for one class in Mask R-CNN

@author Adonis Gonzalez

"""

import xml.etree.cElementTree as ET
import json, os
import os.path as path

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
train = os.path.join(ROOT_DIR, "train")
val = os.path.join(ROOT_DIR, "val")
path = [train, val]


def save_img_to_file():
    for file in path:
        files = os.listdir(file)
        with open(file + '/image.txt', 'w') as f:
            for item in files:
                if (item.endswith('.jpg')):
                    f.write("%s\n" % item)
        f.close()


def convert_xml_to_json():
    for dir in path:
        images, size, polygon, all_json = {}, {}, {}, {}
        images_list = open(dir + '/image.txt', 'r').read().splitlines()

        for img in images_list:
            root = ET.ElementTree(file=dir + '/' + img.split('.jpg')[0] + '.xml').getroot()
            counterObject, xmin, xmax, ymin, ymax, regionsTemp, regi = {}, {}, {}, {}, {}, {}, {}

            number = 0
            for child_of_root in root:
                if child_of_root.tag == 'filename':
                    image_id = child_of_root.text
                    images.update({"filename": image_id})
                    sizetmp = os.path.getsize(dir + '/' + image_id)

                if child_of_root.tag == 'object':
                    for child_of_object in child_of_root:
                        if child_of_object.tag == 'name':
                            category_id = child_of_object.text
                            counterObject[category_id] = number

                        if child_of_object.tag == 'bndbox':
                            for child_of_root in child_of_object:
                                if child_of_root.tag == 'xmin':
                                    xmin[category_id] = int(child_of_root.text)
                                if child_of_root.tag == 'xmax':
                                    xmax[category_id] = int(child_of_root.text)
                                if child_of_root.tag == 'ymin':
                                    ymin[category_id] = int(child_of_root.text)
                                if child_of_root.tag == 'ymax':
                                    ymax[category_id] = int(child_of_root.text)

                    xmintmp = int(xmax[category_id] - xmin[category_id]) / 2
                    xvalue = int(xmin[category_id] + xmintmp)

                    ymintemp = int(ymax[category_id] - ymin[category_id]) / 2
                    yvalue = int(ymin[category_id] + ymintemp)

                    regions = {}
                    regionsTemp = ({"all_points_x": (
                        xmin[category_id], xvalue, xmax[category_id], xmax[category_id], xmax[category_id], xvalue,
                        xmin[category_id], xmin[category_id], xmin[category_id]),
                        "all_points_y": (
                            ymin[category_id], ymin[category_id], ymin[category_id], yvalue,
                            ymax[category_id], ymax[category_id], ymax[category_id], yvalue,
                            ymin[category_id])})

                    category_id_name = (category_id.split(' ')[0])  # cause some <name>SD 1<name>, just use SD
                    regions.update({"region_attributes": {"name": category_id_name}})
                    regions.update({"shape_attributes": regionsTemp})
                    polygon.update({"name": "polygon"})
                    regions.update({"shape_attributes": regionsTemp})
                    regions.update(polygon)
                    regi[number] = regions.copy()
                    regions = {"regions": regi}
                    images.update(regions)
                    size = {"size": sizetmp}
                    images.update(size)
                    all_json[img] = images.copy()
                    number += 1

        with open(dir + '/' + "dataset.json", "a") as outfile:
            json.dump(all_json, outfile)
            print("File dataset.json was save in: ", dir)


if __name__ == "__main__":

    # check if alreday exist dataset.json file in /train and /val
    fileindirTrain = (train + "/dataset.json")
    fileindirVal = (val + "/dataset.json")

    if os.path.isfile(fileindirTrain):
        os.remove(fileindirTrain)
        print("deleting an existent file --> dataset.json from /train")

    if os.path.isfile(fileindirVal):
        os.remove(fileindirVal)
        print("deleting an existent file --> dataset.json from /val")

    save_img_to_file()
    convert_xml_to_json()

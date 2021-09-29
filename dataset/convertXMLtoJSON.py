"""
converterXMLtoJSON

Detect annotations in xml files (bounding boxes) and
converts to json (polygon shape).

@author Adonis Gonzalez

"""

import xml.etree.cElementTree as ET
import json
import os
from os import listdir
from os.path import join

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
train_dir = os.path.join(ROOT_DIR, "train")
val_dir = os.path.join(ROOT_DIR, "val")


def has_files(path: str) -> bool:
    """
    Checks if there is any file in the given path.
    If not files, is not possible continue.

    :param path: A str like /to/path/
    :return: A bool True/False
    """
    assert os.path.exists(path), "--path is not correct"
    return any([j for j in listdir(path) if j.endswith('.jpg')])


def list_images(path: str) -> list:
    """
    Return a list of files that ends with .txt extension

    :param path: A str like /to/path/
    :return: A list that contains all found files
    """
    assert os.path.exists(path), "--path is not correct"
    return [j for j in listdir(path) if j.endswith('.jpg')]


def save_images_log(path: str) -> list:
    """
    Grab images list and save a log in a specific path.

    :param path: A str like /to/path/
    """
    assert os.path.exists(path), "--path is not correct"
    if not has_files(path):
        print("Not images found, try using other path or adding images")
        exit(0)  # If not images exit, cause it is necessary to have xml and jpg together
    else:
        images = list_images(path)
        f = open(join(path, "image.txt"), 'w')
        [f.write("%s\n" % x) for x in images]
        f.close()
        return images


def read_json(dir_path: str, filename: str):
    """
    To read json files

    :param dir_path: A str like /to/path/
    :param filename: A str, json file name e.g data.json
    :return: A JSON file object
    """
    file = join(dir_path, filename)
    assert os.path.isfile(file), "-- check your path file"
    return json.load(open(file))


def remove_file(file_name: str):
    """
    Remove a given file, if not raises assert.

    :param file_name: A str like /to/path/file
    """
    assert os.path.isfile(file_name), "-- check your path file"
    os.remove(file_name)
    print("Deleting file %s" % file_name)


def convert_xml_to_json(path: str, image_list: list):
    images, size, polygon, all_json = {}, {}, {}, {}

    for img in image_list:
        name_xml = img.split('.jpg')[0] + '.xml'
        images.update({"filename": img})
        root = ET.ElementTree(file=path + '/' + name_xml).getroot()
        counterObject, xmin, xmax, ymin, ymax, regionsTemp, regi = {}, {}, {}, {}, {}, {}, {}
        number = 0
        for child_of_root in root:
            if child_of_root.tag == 'filename':
                image_id = child_of_root.text
                sizetmp = os.path.getsize(path + '/' + image_id)
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
                shapes = {"shape_attributes": regionsTemp}
                regions.update(shapes)
                polygon.update({"name": "polygon"})
                regions.update(shapes)
                regions.update(polygon)
                regi[number] = regions.copy()
                regions = {"regions": regi}
                images.update(regions)
                images.update({"size": sizetmp})
                all_json[img] = images.copy()
                number += 1

    out_file = open(join(path, "dataset.json"), "a")
    json.dump(all_json, out_file)
    print("File dataset.json was save in: ", path)


if __name__ == "__main__":
    # Json file for both train and val dir
    file_train = os.path.join(train_dir, "dataset.json")
    file_val = os.path.join(val_dir, "dataset.json")

    # Remove if exist dataset.json in both train and val
    # Just to create a new files
    remove_file(file_train)
    remove_file(file_val)

    # Grab images and save a log in both train and val
    images_train = save_images_log(train_dir)
    images_val = save_images_log(val_dir)

    # Convert from xml to json in both train and val
    convert_xml_to_json(train_dir, images_train)
    convert_xml_to_json(val_dir, images_val)

    # json1 = json.dumps(read_json(train_dir, "dataset.json"), sort_keys=True)
    # json2 = json.dumps(read_json(train_dir, "dataset_good.json"), sort_keys=True)
    # if json1 == json2:
    #     print("Equals!")

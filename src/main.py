"""
converterXMLtoJSON

Detect annotations in xml files (bounding boxes) and
converts to json (polygon shape).

@author Adonis Gonzalez

"""
from os.path import dirname, realpath
import xml.etree.cElementTree as et
from src.util import *
import json

# Paths
ROOT_DIR = dirname(realpath(__file__))
data_dir = join(ROOT_DIR, "../dataset")
train_dir = join(data_dir, "train")
val_dir = join(data_dir, "val")

# Files to create, just path definition
filename_json = "dataset.json"
file_train = join(train_dir, filename_json)
file_val = join(val_dir, filename_json)


def convert_xml_to_json(path: str, image_list: list):
    """
    Convert from xml to json. For each img is necessary
    a xml file annotation. This function save json file.

    :param path: A str like /to/path/file
    :param image_list: A list of images in the same path
    """
    all_json = {}

    for img in image_list:
        name_xml = img.split('.jpg')[0] + '.xml'
        images = ({"filename": img})
        root = et.ElementTree(file=join(path, name_xml)).getroot()
        obj_counter, regi = {}, {}
        number = 0
        for child_of_root in root:
            if child_of_root.tag == 'object':
                for child_of_object in child_of_root:
                    if child_of_object.tag == 'name':
                        obj_id = child_of_object.text.split(' ')[0]  # cause some <name>SD 1<name>, just use SD
                        obj_counter[obj_id] = number
                    if child_of_object.tag == 'bndbox':
                        for child_of_root in child_of_object:
                            if child_of_root.tag == 'xmin':
                                x_min = int(child_of_root.text)
                            if child_of_root.tag == 'xmax':
                                x_max = int(child_of_root.text)
                            if child_of_root.tag == 'ymin':
                                y_min = int(child_of_root.text)
                            if child_of_root.tag == 'ymax':
                                y_max = int(child_of_root.text)

                x_value, y_value = calculate_xy(x_max, x_min, y_max, y_min)
                coord = get_points(x_max, x_min, y_max, y_min, x_value, y_value)

                regions = ({"region_attributes": {"name": obj_id}})
                regions.update({"shape_attributes": coord})
                regions.update({"name": "polygon"})
                regi[number] = regions.copy()
                regions = {"regions": regi}
                images.update(regions)
                images.update({"size": os.path.getsize(join(path, img))})
                all_json[img] = images.copy()
                number += 1

    out_file = open(join(path, filename_json), "a")
    json.dump(all_json, out_file)
    print("File dataset.json was save in: ", path)


if __name__ == "__main__":
    # I convert for both train and val dataset annotation.
    # If you just have a folder, just comment step for val.
    # If not file dataset.json, just comment next two lines.
    # remove_file(file_train)
    # remove_file(file_val)

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

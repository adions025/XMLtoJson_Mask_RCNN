"""
indentation

To indentation json documents

@author Adonis & Tom
"""
import json

your_json = '{"IMG_20180413_091455.jpg": {"filename": "IMG_20180413_091455.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [2241, 2477, 2713, 2713, 2713, 2477, 2241, 2241, 2241], "all_points_y": [997, 997, 997, 1161, 1325, 1325, 1325, 1161, 997]}, "name": "polygon"}}, "size": 1231831}, "IMG_20180413_092043.jpg": {"filename": "IMG_20180413_092043.jpg", "regions": {"0": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [1411, 1540, 1669, 1669, 1669, 1540, 1411, 1411, 1411], "all_points_y": [1767, 1767, 1767, 1875, 1983, 1983, 1983, 1875, 1767]}, "name": "polygon"}, "1": {"region_attributes": {"damage": "damage"}, "shape_attributes": {"all_points_x": [1307, 1361, 1415, 1415, 1415, 1361, 1307, 1307, 1307], "all_points_y": [2337, 2337, 2337, 2395, 2454, 2454, 2454, 2395, 2337]}, "name": "polygon"}}, "size": 1149276}}'
parsed = json.loads(your_json)

print(json.dumps(parsed, indent=4, sort_keys=True))

   
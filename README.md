# XMLtoJson_Mask_RCNN
Use the segmentation in Mask_RCNN, even if the annotation form is rectangular instead of polygon.

The use of false masks does not help the model being generated to be more
precise, as it is not providing new information beyond the bounding boxes.

Generates the polygon shape between the four points of the rectangle in order to achieve the polygon shape, a false mask for the maskrcnn.


### run this file inside your /dataset folder
* /dataset
    * /train
    * /val
    * convertXMLtoJSON.py

````````````$ python convertXMLtoJSON.py````````````


### How should your XML be?

```
<annotation>
	<folder>keuring</folder>
	<filename>IMG_20180413_091455.jpg</filename>
	<path>D:\Seafile\Archive\Projects\125 IWAUC\WP1\fotos 04-13-2018\keuring\IMG_20180413_091455.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>3968</width>
		<height>2976</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>SD</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>2241</xmin>
			<ymin>997</ymin>
			<xmax>2713</xmax>
			<ymax>1325</ymax>
		</bndbox>
	</object>
</annotation>

```

### to achieve this

```
{
    "IMG_20180413_091455.jpg": {
        "filename": "IMG_20180413_091455.jpg",
        "regions": {
            "0": {
                "name": "polygon",
                "region_attributes": {
                    "name": "SD"
                },
                "shape_attributes": {
                    "all_points_x": [
                        2241,
                        2477,
                        2713,
                        2713,
                        2713,
                        2477,
                        2241,
                        2241,
                        2241
                    ],
                    "all_points_y": [
                        997,
                        997,
                        997,
                        1161,
                        1325,
                        1325,
                        1325,
                        1161,
                        997
                    ]
                }
            }
        },
        "size": 1231831
    }
}

```





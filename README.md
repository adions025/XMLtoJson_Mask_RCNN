# XMLtoJson_Mask_RCNN
Now you can use segmentation in Mask_RCNN, even if your annotations are rectangular instead of polygon.
A false masks does not help to be more precise, as it is not providing new information beyond the bounding boxes.
Generates the polygon shape between the four points of the rectangle in order to achieve the polygon shape.


### Usage
* /dataset
    * /train
    * /val
* main.py

````````````$ python main.py````````````


### How should your XML be?

You can check this [xml](dataset/val/IMG_20180413_092050.xml) and see the result [JSON](dataset/val/dataset.json).

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
                        2241, # xmin
                        2477, # X
                        2713, # xmax
                        2713, # xmax
                        2713, # xmax
                        2477, # X
                        2241, # xmin
                        2241, # xmin
                        2241  # xmin
                    ],
                    "all_points_y": [
                        997,  #ymin
                        997,  #ymin
                        997,  #ymin
                        1161, #Y
                        1325, #ymax
                        1325, #ymax
                        1325, #ymax
                        1161, #Y
                        997   #ymin
                    ]
                }
            }
        },
        "size": 1231831
    }
}

```
## Info
If you noticed, the rectangular shape only has the four points, but for the polygon shape we need more points, these points will be created from what we have.

### keyworks
xml, json, converterter, xml to json, convertidor de xml a json, mask rcnn

```
X = xmin + ((xmax-xmin)/2)
Y = ymin + ((ymax-ymin)/2)
```

The way to create a false mask for MaskRCNN with annotations made with LabelImg.

## Author

* **Adonis González Godoy** ([Email](adions025@gmail.com) - [Github](https://github.com/adions025))





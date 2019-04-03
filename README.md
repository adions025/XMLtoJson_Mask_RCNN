# XMLtoJson_Mask_RCNN
Use the segmentation in Mask_RCNN, even if the annotation form is rectangular instead of polygon.

The use of false masks does not help the model being generated to be more
precise, as it is not providing new information beyond the bounding boxes.

Generates the polygon shape between the four points of the rectangle in order to achieve the polygon shape, a false mask for the maskrcnn.


### run this file inside your /dataset folder
/dataset contains two folders /train and /val 

### How should your XML be?

```<annotation>
	<folder>tesName</folder>
	<filename>DSC_9469.jpg</filename>
	<path>/home/images/testName/test</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>7360</width>
		<height>4912</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>damage</name>
		<pose>Unspecified</pose>
		<truncated>1</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1</xmin>
			<ymin>2384</ymin>
			<xmax>7360</xmax>
			<ymax>2813</ymax>
		</bndbox>
	</object>
</annotation>`
``

### to achieve this

```{
    "test.jpg": {
        "filename": "test.jpg",
        "regions": {
            "0": {
                "name": "polygon",
                "region_attributes": {
                    "name": "damage"
                },
                "shape_attributes": {
                    "all_points_x": [
                        1,
                        3680,
                        7360,
                        7360,
                        7360,
                        3680,
                        1,
                        1,
                        1
                    ],
                    "all_points_y": [
                        2384,
                        2384,
                        2384,
                        2598,
                        2813,
                        2813,
                        2813,
                        2598,
                        2384
                    ]
                }
            }
        },
        "size": 5982673
    }
}

```





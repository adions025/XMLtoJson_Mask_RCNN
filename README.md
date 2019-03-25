# XMLtoJson_Mask_RCNN
Use the segmentation in Mask_RCNN, even if the annotation form is rectangular instead of polygon.

The use of false masks does not help the model being generated to be more
precise, as it is not providing new information beyond the bounding boxes.

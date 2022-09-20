# A Helper of License Plate Annotation
## Description
When developing an object detection application, you usually need to annotate where objects are located on the images before training the detector. Such routine are tidious but necessary. Here is an examle showing how to make it more efficient by using a pretrained model. 

<div>
<img src='https://github.com/ComputerVisionIsFun/A-Helper-of-License-Plate-Annotation/blob/main/intro.png' width=300 style='left'>
</div>

## Usage
```
python test.py -v ./test_videos/ -of ./output/ -sr 5 -sxp ./Annotation/sample.xml
```

## Requirements
1. OpenCV
2. xml

## References
<ul>[1] https://github.com/JaidedAI/EasyOCR </ul>
<ul>[2] https://github.com/heartexlabs/labelImg </ul>

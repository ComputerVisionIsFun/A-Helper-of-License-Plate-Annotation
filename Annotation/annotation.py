import cv2
import os
import easyocr
import Parameters.anno_parameters as ap
from .create_xml import create_xml


def _video2frames(video_path, save_folder, save_prefix='_', period=2, img_format = ap.img_format):
    cap = cv2.VideoCapture(video_path)
    frame_i, save_i = 0, 0
    while(1):
        ret, frame = cap.read()
        if ret==False:
            break

        if frame_i%period==0:
            save_path = save_folder + save_prefix + '_' + str(save_i) + '.' + img_format
            cv2.imwrite(save_path, frame)
            save_i+=1

        frame_i+=1


def video2frames(video_folder, save_folder, period, video_formats = ap.video_formats):
    video_names = os.listdir(video_folder)
    for video_name in video_names:
        for video_format_i, video_format in enumerate(video_formats):
            if video_format_i==0:
                save_prefix = video_name.replace(video_format,'')
            else:
                save_prefix = save_prefix.replace(video_format,'')

            

        video_path = video_folder + video_name
        _video2frames(video_path, save_folder, save_prefix, period)


def _automatic_annotation(img_folder, sample_xml_path='sample.xml', language = ap.language, img_format = ap.img_format, obj_name = ap.obj_name, img_depth = ap.img_depth):
    files = os.listdir(img_folder)
    img_names = []
    for file in files:
        if file[-1]=='g':
            img_names.append(file)

    reader = easyocr.Reader(language)
    for img_name in img_names:
        img = cv2.imread(img_folder + img_name, 1)

        objs = reader.readtext(img_folder + img_name)
        if len(objs)==0:
            continue

        new_xml_save_path = img_folder + img_name.replace(img_format,'xml')
        create_xml(img_folder, img_name,objs,sample_xml_path,new_xml_save_path,img.shape[1],img.shape[0],img_depth,obj_name)


def automatic_annotation(video_folder, save_folder, period, sample_xml_path,video_formats=ap.video_formats,language=ap.language,img_format=ap.img_format,obj_name=ap.obj_name,img_depth=ap.img_depth):
    # video 2 frames
    video2frames(video_folder,save_folder,period,video_formats)

    # annot via easyocr
    img_folder = save_folder
    _automatic_annotation(img_folder,sample_xml_path,language,img_format,obj_name,img_depth)

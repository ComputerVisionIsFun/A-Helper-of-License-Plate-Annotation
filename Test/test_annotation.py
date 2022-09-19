from Annotation import annotation as A

video_folder = 'C:/Users/Chiang-En Chen/Desktop/LPR_dataset/videos/'
save_folder = 'C:/Users/Chiang-En Chen/Desktop/LPR_dataset/xml/'
period = 2
sample_xml_path = 'D:/GitHub/LPR_TOOLBOX/Annotation/sample.xml'





A.automatic_annotation(video_folder,save_folder,period,sample_xml_path)
from Annotation import annotation as A
import argparse
import os

def prase_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_folder','-v',default='./test_videos/',type=str,required=True,help='folder of videos to be annotated.')
    parser.add_argument('--output_folder','-of',default='./data/',type=str,required=True,help='folder of output containing images and annotations.')
    parser.add_argument('--sampling_rate','-sr',default=5,type=int,required=True,help='sampling rate of extracting frames.')
    parser.add_argument('--sample_xml_path','-sxp',default='./Annotation/sample.xml',type=str,required=True,help='')


    return parser.parse_args()


def main(args):
    video_folder = args.video_folder
    output_folder = args.output_folder
    sampling_rate = args.sampling_rate
    sample_xml_path = args.sample_xml_path

    A.automatic_annotation(video_folder,output_folder,sampling_rate,sample_xml_path)



if __name__=='__main__':
    args = prase_args()
    video_folder = args.video_folder
    output_folder = args.output_folder
    sampling_rate = args.sampling_rate
    sample_xml_path = args.sample_xml_path

    try:
        os.mkdir(output_folder)
    except:
        pass

    main(args)
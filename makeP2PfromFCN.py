import os
from glob import glob
import shutil
import sys


def transfer(src_dir, dst_dir):
    is_exist = os.path.exists(dst_dir)
    if not is_exist:
        os.makedirs(dst_dir)

    # Iterate over all subdirectories of this dataset directory.
    for image_dir_path, subdir_list, file_list in os.walk(src_dir, topdown=True):
        # print(image_dir_path)
        # print(subdir_list)
        # print(file_list)

        image_paths = glob(os.path.join(image_dir_path, '*.' + 'png'))  # Get all images in this directory
        if len(image_paths) > 0:  # If there are any images, add them to the list of images.
            image_paths += image_paths

        subdir = os.path.basename(os.path.normpath(image_dir_path))  # Get the subdirectory we're currently in.
        dir_path = os.path.join(src_dir, subdir)
        print(dir_path)
        print('-------------')
        for image in file_list:
            newpath=dst_dir+'/'+image
            shutil.move(dir_path+'/'+image,newpath)
        print('finish--'+image_dir_path)



if __name__ == '__main__':
    transfer('C:\\Users\\Z\\Downloads\\gtFine_trainvaltest\\gtFine\\val','C:\\Users\\Z\\Downloads\\gtFine_trainvaltest\\val_test')

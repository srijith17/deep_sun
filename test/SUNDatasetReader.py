import json
import os

import cv2
import numpy
import scipy.io


class SunDatasetReader():
    dataset_path = ''
    def read(self, file_path):
        if os.path.isdir(file_path):
            self.dataset_path = file_path
        else:
            raise Exception('invlaid path')

    @property
    def getDatasetPath(self):
        return self.dataset_path

    def readImage(self, image_path, image_file_name):
        image = []
        if os.path.isdir(image_path):
            if len(image_file_name) <= 0:
                image_file_name = os.listdir(image_path)[0]
            image_path = os.path.join(image_path, image_file_name)

            if os.path.isfile(image_path):
                image = cv2.imread(image_path)
            else:
                raise Exception('image does not exist')
        else:
            raise Exception('folder does not exist')
        return image

    def getRGBImage(self):
        rgb_path = os.path.join(self.dataset_path, 'image')
        return self.readImage(rgb_path, '')

    def getDepthImage(self):
        depth_path = os.path.join(self.dataset_path, 'depth')
        return self.readImage(depth_path, '')

    def getFullResRGBImage(self):
        fullres_rgb_path = os.path.join(self.dataset_path, 'fullres')
        head, tail = os.path.split(self.dataset_path)
        file_name = tail + '.jpg'
        return self.readImage(fullres_rgb_path, file_name)

    def getDepthDenoisedImage(self):
        denoised_depth_path = os.path.join(self.dataset_path, 'depth_bfx')
        return self.readImage(denoised_depth_path, '')

    def getFullResDepthImage(self):
        fullres_depth_path = os.path.join(self.dataset_path, 'fullres')
        head, tail = os.path.split(self.dataset_path)
        file_name = tail + '_abs.png'
        return self.readImage(fullres_depth_path, file_name)

    def getIntrinsics(self):
        intrinsics_path = os.path.join(self.dataset_path, 'intrinsics.txt')
        return numpy.genfromtxt(intrinsics_path, delimiter='')

    def getFullResIntrinsics(self):
        fullres_intrinsics_path = os.path.join(self.dataset_path, 'fullres', 'intrinsics.txt')
        fullres_instrinsics = numpy.genfromtxt(fullres_intrinsics_path, delimiter='')
        return fullres_instrinsics.reshape(3, 3)

    def getFullExtrinsics(self):
        extrinsics_folder_path = os.path.join(self.dataset_path, 'extrinsics')
        extrinsics_file_path = os.path.join(extrinsics_folder_path, os.listdir(extrinsics_folder_path)[0])
        return numpy.genfromtxt(extrinsics_file_path, delimiter='')

    def getSegmentatedLabels(self):
        semented_mat_file = os.path.join(self.dataset_path, 'seg.mat')
        segmentation_mat = scipy.io.loadmat(semented_mat_file)
        labeled_image = segmentation_mat['seglabel']
        labels_string = segmentation_mat['names']
        labels = [str(''.join(letter)) for letter_array in labels_string[0] for letter in letter_array]
        return labeled_image, labels

    def get2DAnnotation(self):
        annotation_file = os.path.join(self.dataset_path, 'annotation', 'index.json')
        annotation_data = []
        with open(annotation_file) as json_data:
            annotation_data = json.load(json_data)
        print(annotation_data)
        pass



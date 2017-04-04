import unittest
import os
import numpy
import cv2

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

    def getRGBImage(self):
        rgb_path = os.path.join(self.dataset_path, 'image')
        if os.path.isdir(rgb_path):
            rgb_image_path = os.path.join(rgb_path, os.listdir(rgb_path)[0])
            if os.path.isfile(rgb_image_path):
                return cv2.imread(rgb_image_path)
            else:
                raise Exception('image does not exist')
        else:
            raise Exception('folder does not exist')



class SUNDatasetReaderFolderValidityTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        """ Set up for the test """

    def tearDown(self):
        """ Tear Down for the test """

    def test_dataSetFolderDoesnotExist(self):
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'path_does_not_exist')
        try:
            self.datasetReader.read(test_data_path)
            self.fail('Did not throw expected execption')
        except:
            pass

    def test_retrieveDataSetPath(self):
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'good_dataset')
        self.datasetReader.read(test_data_path)
        self.assertEqual(self.datasetReader.getDatasetPath, test_data_path)

class SUNDatasetReaderFolderWithNoDatasetTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        """ Set up for the test """
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'folder_exists_not_dataset')
        self.datasetReader.read(test_data_path)

    def tearDown(self):
        """ Tear Down for the test """

    def test_retrieveRGBImage1(self):
        try:
            rgb_image = self.datasetReader.getRGBImage()
            self.fail('Did not throw expected execption')
        except:
            pass

class SUNDatasetReaderEmptyFolderTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        """ Set up for the test """
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'empty_dataset')
        self.datasetReader.read(test_data_path)

    def tearDown(self):
        """ Tear Down for the test """

    def test_retrieveRGBImage(self):
        try:
            rgb_image = self.datasetReader.getRGBImage()
            self.fail('Did not throw expected execption')
        except:
            pass


class SUNDatasetReaderTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'good_dataset')
        self.datasetReader.read(test_data_path)
        """ Set up for the test """

    def tearDown(self):
        """ Tear Down for the test """

    def test_retrieveRGBImage(self):
        rgb_image = self.datasetReader.getRGBImage()
        self.assertEquals(rgb_image.shape, (427, 561, 3))

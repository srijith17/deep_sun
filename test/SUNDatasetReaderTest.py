import os
import unittest

import numpy

from test.SUNDatasetReader import SunDatasetReader


# mat = scipy.io.loadmat('file.mat')


class SUNDatasetReaderFolderValidityTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        """ Set up for the test """

    def tearDown(self):
        """ Tear Down for the test """

    def test_dataSetFolderDoesnotExist(self):
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'path_does_not_exist')
        try:
            self.datasetReader.read(test_data_path)
            self.fail('Did not throw expected execption')
        except:
            pass

    def test_retrieveDataSetPath(self):
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'good_dataset')
        self.datasetReader.read(test_data_path)
        self.assertEqual(self.datasetReader.getDatasetPath, test_data_path)

class SUNDatasetReaderFolderWithNoDatasetTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        """ Set up for the test """
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'folder_exists_not_dataset')
        self.datasetReader.read(test_data_path)

    def tearDown(self):
        """ Tear Down for the test """

    def test_retrieveRGBImage(self):
        try:
            rgb_image = self.datasetReader.getRGBImage()
            self.fail('Did not throw expected execption')
        except:
            pass

    def test_retrieveFullResRGBImage(self):
        try:
            rgb_image = self.datasetReader.getFullResRGBImage()
            self.fail('Did not throw expected execption')
        except:
            pass

    def test_retrieveDepthImage(self):
        try:
            depth_image = self.datasetReader.getDepthImage()
            self.fail('Did not throw expected execption')
        except:
            pass

    def test_retrieveFullResDepthImage(self):
        try:
            depth_image = self.datasetReader.getFullResDepthImage()
            self.fail('Did not throw expected execption')
        except:
            pass



class SUNDatasetReaderEmptyFolderTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        """ Set up for the test """
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'empty_dataset')
        self.datasetReader.read(test_data_path)

    def tearDown(self):
        """ Tear Down for the test """

    def test_retrieveRGBImage(self):
        try:
            rgb_image = self.datasetReader.getRGBImage()
            self.fail('Did not throw expected execption')
        except:
            pass

    def test_retrieveFullResRGBImage(self):
        try:
            rgb_image = self.datasetReader.getFullResRGBImage()
            self.fail('Did not throw expected execption')
        except:
            pass

    def test_retrieveDepthImage(self):
        try:
            rgb_image = self.datasetReader.getDepthImage()
            self.fail('Did not throw expected execption')
        except:
            pass

    def test_retrieveFullResDepthImage(self):
        try:
            depth_image = self.datasetReader.getFullResDepthImage()
            self.fail('Did not throw expected execption')
        except:
            pass


class SUNDatasetReaderTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        test_data_path = os.path.join(os.getcwd(), 'test', 'test_data', 'good_dataset')
        self.datasetReader.read(test_data_path)
        """ Set up for the test """

    def tearDown(self):
        """ Tear Down for the test """

    def test_retrieveRGBImage(self):
        rgb_image = self.datasetReader.getRGBImage()
        self.assertEquals(rgb_image.shape, (427, 561, 3))

    def test_retrieveFullResRGBImage(self):
        rgb_image = self.datasetReader.getFullResRGBImage()
        self.assertEquals(rgb_image.shape, (480, 640, 3))

    def test_retrieveDepthImage(self):
        depth_image = self.datasetReader.getDepthImage()
        self.assertEquals(depth_image.shape, (427, 561, 3))

    def test_retrieveDenoisedDepthImage(self):
        depth_image = self.datasetReader.getDepthDenoisedImage()
        self.assertEquals(depth_image.shape, (427, 561, 3))

    def test_retrieveFullResDepthImage(self):
        rgb_image = self.datasetReader.getFullResDepthImage()
        self.assertEquals(rgb_image.shape, (480, 640, 3))

    def test_retrieveIntrinsics(self):
        expected_intrinsics = [ [ 520.532,       0.0,  277.9258 ],
                                [     0.0,  520.7444,  215.115  ],
                                [     0.0,       0.0,      1.0  ]]
        intrinsics = self.datasetReader.getIntrinsics()
        self.assertTrue(numpy.allclose(intrinsics, expected_intrinsics));

    def test_retrieveFullResIntrinsics(self):
        expected_fullres_intrinsics = [ [ 520.532,       0.0,  318.9258 ],
                                        [     0.0,  520.7444,  260.115  ],
                                        [     0.0,       0.0,      1.0  ]]

        fullres_intrinsics = self.datasetReader.getFullResIntrinsics()
        self.assertTrue(numpy.allclose(fullres_intrinsics, expected_fullres_intrinsics));

    def test_retrieveExtrinsics(self):
        expected_extrinsics = [[ 0.999997, -0.002568, -0.000358, 0.000000],
                               [ 0.002568,  0.961833,  0.273625, 0.000000],
                               [-0.000358, -0.273625,  0.961836, 0.000000]]
        full_extrinsics = self.datasetReader.getFullExtrinsics()
        self.assertTrue(numpy.allclose(full_extrinsics, expected_extrinsics));

    def test_retrieveSegmentationLabels(self):
        expected_labels = ['wall', 'wall', 'monitor', 'monitor', 'window', 'window', 'window', 'floor', 'wall', 'mouse', 'keyboard', 'bottle', 'bottle', 'board', 'table', 'wall', 'bottle', 'bottle', 'wall', 'wall', 'wall', 'floor', 'cpu', 'table'];
        labeled_image, labels = self.datasetReader.getSegmentatedLabels()
        self.assertListEqual(expected_labels, labels);

    def test_retrieveAnnotation2D(self):
        annotation = self.datasetReader.get2DAnnotation()
    #     mat = scipy.io.loadmat('file.mat')

    # def test_retrieveAnnotation3DFinal(self):
    #     depth_image = self.datasetReader.getDepthDenoisedImage()
    #     self.assertEquals(depth_image.shape, (427, 561, 3))
    #
    # def test_retrieveAnnotation3DLayout(self):
    #     depth_image = self.datasetReader.getDepthDenoisedImage()
    #     self.assertEquals(depth_image.shape, (427, 561, 3))
    #
    # def test_retrieveScene(self):
    #     depth_image = self.datasetReader.getDepthDenoisedImage()
    #     self.assertEquals(depth_image.shape, (427, 561, 3))




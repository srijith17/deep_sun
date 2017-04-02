import unittest
import os
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

class SUNDatasetReaderTest(unittest.TestCase):
    datasetReader = SunDatasetReader()

    def setUp(self):
        """ Set up for the test """

    def tearDown(self):
        """ Tear Down for the test """

    def test_retrieveDataSetPath(self):
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'good_dataset')
        self.datasetReader.read(test_data_path)
        self.assertEqual(self.datasetReader.getDatasetPath, test_data_path)

    def test_dataSetFolderDoesnotExist(self):
        test_data_path = os.path.join(os.getcwd(), 'test_data', 'path_does_not_exist')
        try:
            self.datasetReader.read(test_data_path)
            self.fail('Did not throw expected execption')
        except:
            pass


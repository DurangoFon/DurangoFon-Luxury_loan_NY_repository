import os
import urllib.request
import shutil
import zipfile

shutil.rmtree('./data')

url = 'https://storage.googleapis.com/kaggle-data-sets/3052759/5246433/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230510%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230510T164513Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=5729fddbbf6935aeff216032f2d7299bd6ee8546f923d25dc3350cbca22a02ad365f4e5eea81fbc77f71b77359121c6a08ae6bbbccf440484b1129c2adcd39beb3722ce99106557dcac624ff2a3f67f6a25ce205275f5bc78591ccc7de0d7cc0f46f65c9fc853a32c8e6a3aadfdffc95fec8a0d0d2413e466acde8a67da1a9dba77369faf286e51d331b1cc35f9b20b369d6926d0e3f03710ede38b735686b6903c70c1e54175de35e60c0bcf9155546179ce27146bcfd51d1fff7b861c8abdf3120026dd713f08a12844a64d528e456fa3ead1b37951f40aab68b3121ddc6bea969e5f41b5d3d263ff633848acf6392a3daf90fd0590a5308af16807fceb8af'
os.mkdir('./data')
urllib.request.urlretrieve(url,'./data/data.zip')

data_extraction = zipfile.ZipFile('./data/data.zip')
data_extraction.extractall('./data/')
data_extraction.close()

os.unlink('./data/data.zip ')
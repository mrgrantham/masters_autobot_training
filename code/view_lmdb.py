import caffe
import lmdb
import numpy as np
import matplotlib.pyplot as plt
from caffe.proto import caffe_pb2
from caffe.io import datum_to_array, array_to_datum
import os
import PIL.Image
from StringIO import StringIO

def read_images_from_lmdb(db_name, visualize):
	env = lmdb.open(db_name)
	txn = env.begin()
	cursor = txn.cursor()
	X = []
	y = []
	idxs = []
	for idx, (key, value) in enumerate(cursor):
		datum = caffe_pb2.Datum()
		datum.ParseFromString(value)
		# X.append(np.array(datum_to_array(datum)))
		X.append(np.fromstring(datum.data, dtype=np.uint8).reshape(
            datum.height, datum.width,datum.channels )
)
		y.append(datum.label)
		idxs.append(idx)
	if visualize:
		print "Visualizing a few images..."
		for i in range(9):
			img = X[i]
			plt.subplot(3, 3, i + 1)

			temp = img.shape
			print "OG: " + str(temp)
			# plt.axis('off')
			plt.imshow(img)
			plt.title(y[i])
		plt.show()
	print " ".join(["Reading from", db_name, "done!"])
	return X, y, idxs

# def read_lmdb(lmdb_file):
#     cursor = lmdb.open(lmdb_file, readonly=True).begin().cursor()
#     datum = caffe.proto.caffe_pb2.Datum()
#     for _, value in cursor:
#         datum.ParseFromString(value)
#         s = StringIO()
#         s.write(datum.data)
#         s.seek(0)

#         yield np.array(PIL.Image.open(s)), datum.label



traindb = os.path.dirname(os.path.realpath(__file__)) + '/../train_lmdb'
testdb = os.path.dirname(os.path.realpath(__file__)) + '/../validation_lmdb'

read_images_from_lmdb(traindb, 1)
read_images_from_lmdb(testdb, 1)
# read_lmdb(traindb)

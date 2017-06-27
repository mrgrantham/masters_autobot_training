'''
Title           :create_lmdb.py
Description     :This script creates a label file that can be used with create_imageset
Author          :Adil Moujahid
Date Created    :20160619
Date Modified   :20160625
version         :0.2
usage           :python create_lmdb.py
python_version  :2.7.11
'''

import os
import glob
import random
import numpy as np
import sys
import cv2

import caffe
from caffe.proto import caffe_pb2
import lmdb
import matplotlib.pyplot as plt

# train_list = os.path.dirname(os.path.realpath(__file__)) + '/../train/train.txt'

train_list = sys.argv[1] + '/' + sys.argv[2]
train_data = [img for img in glob.glob(sys.argv[1] + "/*jpg")]



print 'Creating training list'
print 'train list: ' + train_list

with open(train_list, "a") as myfile:    
    for id, img_path in enumerate(train_data):
        if 'door_' in img_path:
            label = 0
        elif 'doorstop' in img_path:
            label = 1
        elif 'person' in img_path:
            label = 2
        elif 'desk' in img_path:
            label = 3
        else:
            print "unsure: " + img_path
        line = os.path.basename(img_path) +  " " + str(label) + "\n"
        print line
        myfile.write(line)

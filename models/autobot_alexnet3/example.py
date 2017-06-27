from visualize_caffe import *
import sys

# Make sure caffe can be found
sys.path.append('../caffe/python/')

import caffe


# Load model
net = caffe.Net('/home/james/autobot/models/autobot_alexnet3/deployAlexnet3.prototxt',
                '/home/james/autobot/models/autobot_alexnet3/caffe_alexnet3_train_iter_180000.caffemodel',
                caffe.TEST)

visualize_weights(net, 'conv1', filename='conv1.png')
visualize_weights(net, 'conv2', filename='conv2.png')
visualize_weights(net, 'conv3', filename='conv3.png')
visualize_weights(net, 'conv4', filename='conv4.png')
visualize_weights(net, 'conv5', filename='conv5.png')

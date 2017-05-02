OBJECT RECOGNITION FOR AUTOBOT
==============================

This is the Description of the Process for Training the Autobot to detect different objects
-------------------------------------------------------------------------------------------

This component of the overall projects consists of the following peices

- Training Data for the following objects:

    *   Closed Doors
    *   Open Doors
    *   Doorstops
    *   Centered Hallways
    *   Pedestrians

- Data Processiong
    * To be completed using a modified version of the python script from [here](http://adilmoujahid.com/posts/2016/06/introduction-deep-learning-python-caffe/)

- Model Definition for the Training of the Neural Network
    
        see notes in  autobot_train.prototext

- Model Definition for the Deployment of the Neural Network

        see notes in autobot_deploy.prototext

    From [Stack Overflow](http://stackoverflow.com/questions/33770190/how-to-create-caffe-deploy-from-train-prototxt):
    
    There are two main differences between a "train" prototxt and a "deploy" one:

    1. Inputs: While for training data is fixed to a pre-processed      training dataset (lmdb/HDF5 etc.), deploying the net require     it to process other inputs in a more "random" fashion.
        Therefore, the first change is to remove the input layers (layers that push "data" and "labels" during TRAIN and TEST phases). To replace the input layers you need to add the following declaration:

        input: "data"
        input_shape: { dim:1 dim:3 dim:224 dim:224 }
        
        This declaration does not provide the actual data for the net, but it tells the net what shape to expect, allowing caffe to pre-allocate necessary resources.

    2. Loss: the top most layers in a training prototxt define the      loss function for the training. This usually involve the         ground truth labels. When deploying the net, you no longer       have access to these labels. Thus loss layers should be          converted to "prediction" outputs. For example, a                "SoftmaxWithLoss" layer should be converted to a simple          "Softmax" layer that outputs class probability instead of        log-likelihood loss. Some other loss layers already have         predictions as inputs, thus it is sufficient just to remove      them.

Installation instructions for Caffe on Training System
- Portion of scripts taken from [A Practical Introduction to Deep Learning with Caffe and Python](http://adilmoujahid.com/posts/2016/06/introduction-deep-learning-python-caffe/)
- TO BE COMPLETED

Enter the following command to generate the mean photo of your dataset

        /home/james/caffe/build/tools/compute_image_mean -backend=lmdb /home/james/autobot/train_lmdb /home/james/autobot/mean.binaryproto

Enter the following command to initiate training

        /home/james/caffe/build/tools/caffe train --solver /home/james/autobot/autobot_googlenet/quick_solver.prototxt 2>&1 | tee /home/james/autobot/autobot_googlenet/autobot_googlenet_train.log        
        /home/james/caffe/build/tools/caffe train --solver /home/james/autobot/Catdog_net/autobot_solver.prototxt 2>&1 | tee /home/james/autobot/Catdog_net/autobot__train.log
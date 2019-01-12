from keras.models import Sequential
from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
from keras.models import Model
from keras.layers.normalization import BatchNormalization
from keras.layers.pooling import MaxPooling2D, AveragePooling2D
from keras.layers.merge import Concatenate
from keras.layers.core import Lambda, Flatten, Dense
from keras.initializers import glorot_uniform
from keras.engine.topology import Layer
from keras import backend as K
K.set_image_data_format('channels_first')
import cv2
import os
import numpy as np
from numpy import genfromtxt
import pandas as pd
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
import csv

np.set_printoptions(threshold=np.nan)

FRmodel = faceRecoModel(input_shape=(3, 96, 96))
print("Total Params:", FRmodel.count_params())

def triplet_loss(y_true, y_pred, alpha = 0.2):
    """
    Implementation of the triplet loss as defined by formula (3)
    
    Arguments:
    y_true -- true labels, required when you define a loss in Keras, you don't need it in this function.
    y_pred -- python list containing three objects:
            anchor -- the encodings for the anchor images, of shape (None, 128)
            positive -- the encodings for the positive images, of shape (None, 128)
            negative -- the encodings for the negative images, of shape (None, 128)
    
    Returns:
    loss -- real number, value of the loss
    """
    
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    
    ### START CODE HERE ### (≈ 4 lines)
    # Step 1: Compute the (encoding) distance between the anchor and the positive, you will need to sum over axis=-1
    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis=-1)
    # Step 2: Compute the (encoding) distance between the anchor and the negative, you will need to sum over axis=-1
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis=-1)
    # Step 3: subtract the two previous distances and add alpha.
    basic_loss = tf.add(tf.subtract(pos_dist, neg_dist),alpha)
    # Step 4: Take the maximum of basic_loss and 0.0. Sum over the training examples.
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0))
    ### END CODE HERE ###
    
    return loss

with tf.Session() as test:
    tf.set_random_seed(1)
    y_true = (None, None, None)
    y_pred = (tf.random_normal([3, 128], mean=6, stddev=0.1, seed = 1),
              tf.random_normal([3, 128], mean=1, stddev=1, seed = 1),
              tf.random_normal([3, 128], mean=3, stddev=4, seed = 1))
    loss = triplet_loss(y_true, y_pred)
    
    print("loss = " + str(loss.eval()))

FRmodel.compile(optimizer = 'adam', loss = triplet_loss, metrics = ['accuracy'])
load_weights_from_FaceNet(FRmodel)

database = {}
database["ashish"] = img_to_encoding("../Images1/2/2_1_resize.png", FRmodel)
database["aman"] = img_to_encoding("../Images1/2/2_3_resize.png", FRmodel)
database["mayur"] = img_to_encoding("../Images1/2/2_4_resize.png", FRmodel)
database["ketan"] = img_to_encoding("../Images1/2/2_2_resize.png", FRmodel)

# GRADED FUNCTION: who_is_it
def cosine_similar(u,v):
    dis=0.0
    dot=np.dot(u,np.transpose(v))
    norm_u=np.sqrt(np.sum(u**2))
    norm_v=np.sqrt(np.sum(v**2))
    cos=dot/(norm_u*norm_v)
    return cos

def who_is_it(image_path, database, model):

    encoding = img_to_encoding(image_path, model)
    
    min_dist = 100
    
    for (name, db_enc) in database.items():
        
        dist = np.linalg.norm(encoding - db_enc)
        if dist < min_dist:
            min_dist = dist
            identity = name
    
    if min_dist > 0.7:
        print(str(min_dist))
        print("Not in the database.")
    else:
        print ("it's " + str(identity) + ", the distance is " + str(min_dist))
        
    return min_dist, identity

path11=os.listdir('../Images/')
name={}
name["ashish"] =  0
name["aman"] =    0
name["mayur"] =   0
name["ketan"] =   0
for elem2 in path11:
  path1='../Images/'+elem2
  if os.path.isdir(path1):
      list1=os.listdir(path1)
      for elem in list1:
         if elem.endswith('_blurred_resize.png'):
             a,b=who_is_it(path1+'/'+elem, database, FRmodel)
             name[b]=name[b]+1


dd=[]
ff=[]
for elem in name:
    dd.append(elem)
    ff.append(name[elem])
#dd=np.transpose(np.array(dd)).tolist()
#ff=np.transpose(np.array(ff)).tolist()


# b=np.chararray((len(dd),2),itemsize=20)
# b[:,0]=dd
# b[:,1]=ff

#myData = [dd,ff]  
myFile = open('csvexample3.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile)
   writer.writerows(zip(dd,ff))
# -*- coding:utf-8 -*-
# python2

'''
mian .py for conv-rotor project
0. initialize
1. get data;
2. make models;
3. train;
4. test;
5. visualize;
'''

# initialize
from __future__ import print_function, division 

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

import numpy as np

import time
import copy
import os

# get data
import data_loader

rsn = True
data_arr = data_loader.load_data('dis_data.txt','rpm_data.txt')
label_vec = data_loader.load_label('label_vec.txt')
print('data size: ', np.shape(data_arr))
print('label size: ', np.shape(label_vec))

dataset = data_loader.arr_to_dataset(data_arr,label_vec)
print(dataset)


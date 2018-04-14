#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:17:39 2018

@author: lakshay
"""

import numpy as np
import re
import itertools
from collections import Counter


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels(text_file, path_file, map_file, clean_text=True):
    
    f = open(text_file)
    x_text = [line.strip() for line in f.readlines()]
    f.close()
    
    if clean_text:
        x_text = [clean_str(sent) for sent in x_text]
    
    f = open(path_file)
    y_labels = [line.strip().split('/')[-2] for line in f.readlines()]
    f.close()
    
    f = open(map_file)
    labels = [line.strip() for line in f.readlines()]
    f.close()
    
    label_map = {}
    for i in range(len(labels)):
        label_map[labels[i]] = i
        
    y = [label_map[_] for _ in y_labels]
    
    from sklearn.preprocessing import LabelBinarizer
    binarizer = LabelBinarizer()
    y = binarizer.fit_transform(y)
    
    return [x_text, y, y_labels]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]

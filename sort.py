#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:54:12 2018

@author: lakshay
"""

import cv2
import codecs
import pandas as pd

train = 'book30-listing-train.csv'
test = 'book30-listing-test.csv'

header_names = ['Amazon ID (ASIN)', 'Filename', 'Image URL', 'Title', 'Author', 'Category ID', 'Category']

with codecs.open(train, mode='r', encoding='utf-8', errors='ignore') as f:
    train_file = pd.read_csv(f, delimiter=",", header=None, names=header_names)
    
with codecs.open(test, mode='r', encoding='utf-8', errors='ignore') as f1:
    test_file = pd.read_csv(f1, delimiter=",", header=None, names=header_names)
    
"""
for i in range(train_file.shape[0]):
    if i % 500 == 0:
        print(i)
    
    catergory = train_file['Category'][i]
    img = train_file['Filename'][i]
    
    img_rows = 299
    img_cols = 299

    image = cv2.imread('BookCover30_/train/' + img)
    
    cv2.imwrite("./BookCover30_original_size/train/" + catergory + "/" + img, image)
   
for i in range(test_file.shape[0]):
    if i % 500 == 0:
        print(i)
    
    catergory = test_file['Category'][i]
    img = test_file['Filename'][i]
    
    img_rows = 299
    img_cols = 299

    image = cv2.imread('BookCover30_/test/' + img)
    
    cv2.imwrite("./BookCover30_original_size/test/" + catergory + "/" + img, image)
    
"""
"""

for i in range(train_file.shape[0]):
    if i % 500 == 0:
        print(i)
    
    catergory = train_file['Category'][i]
    img = train_file['Filename'][i]
    
    img_rows = 299
    img_cols = 299

    image = cv2.imread('BookCover30_/train/' + img)
    
    
    sz = image.shape
    if sz[0] < img_rows or sz[1] < img_cols :
        image = cv2.resize(image, (img_rows, img_cols), 0, 0, cv2.INTER_CUBIC)
    else:
        image = cv2.resize(image, (img_rows, img_cols), 0, 0, cv2.INTER_AREA)
    
    
    cv2.imwrite("./BookCover30/train/" + catergory + "/" + img, image)

"""    
for i in range(test_file.shape[0]):
    if i % 500 == 0:
        print(i)
    
    catergory = test_file['Category'][i]
    img = test_file['Filename'][i]
    
    img_rows = 299
    img_cols = 299

    image = cv2.imread('BookCover30_/test/' + img)
    
    
    sz = image.shape
    if sz[0] < img_rows or sz[1] < img_cols :
        image = cv2.resize(image, (img_rows, img_cols), 0, 0, cv2.INTER_CUBIC)
    else:
        image = cv2.resize(image, (img_rows, img_cols), 0, 0, cv2.INTER_AREA)
    
    
    cv2.imwrite("./BookCover30/test/" + catergory + "/" + img, image)
    

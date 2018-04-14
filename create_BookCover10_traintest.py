#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 16:23:16 2018

@author: lakshay
"""

f = open('./BookCover30_text/train_data.txt')
train_text_30 = [line.strip() for line in f.readlines()]
f.close()

f = open('./BookCover30_text/test_data.txt')
test_text_30 = [line.strip() for line in f.readlines()]
f.close()

f = open('BookCover30files.txt')
train_files_30 = [line.strip() for line in f.readlines()]
f.close()

f = open('BookCover30_testfiles.txt')
test_files_30 = [line.strip() for line in f.readlines()]
f.close()


f = open('BookCover10_map.txt')
labels_10 = [line.strip() for line in f.readlines()]
f.close()


f = open('./BookCover10_text/test_data.txt', 'w')
for i in range(len(test_files_30)):
    if test_files_30[i].split('/')[-2] in labels_10:
        f.write(test_text_30[i] + '\n')
f.close()

f = open('./BookCover10_text/train_data.txt', 'w')
for i in range(len(train_files_30)):
    if train_files_30[i].split('/')[-2] in labels_10:
        f.write(train_text_30[i] + '\n')
f.close()

f = open('BookCover10_testfiles.txt', 'w')
for i in range(len(test_files_30)):
    if test_files_30[i].split('/')[-2] in labels_10:
        f.write(test_files_30[i] + '\n')
f.close()

f = open('BookCover10files.txt', 'w')
for i in range(len(train_files_30)):
    if train_files_30[i].split('/')[-2] in labels_10:
        f.write(train_files_30[i] + '\n')
f.close()

f = open('./BookCover10_text/train_data.txt')
train_text_10 = [line.strip() for line in f.readlines()]
f.close()

f = open('./BookCover10_text/test_data.txt')
test_text_10 = [line.strip() for line in f.readlines()]
f.close()
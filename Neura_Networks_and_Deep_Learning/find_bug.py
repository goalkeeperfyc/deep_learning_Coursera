#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 02:59:48 2019

@author: fangyucheng
Email: 664947387@qq.com
"""

import numpy as np

w = np.array([[1.],[2.]])
b = 2
X = np.array([[1.,2.,-1.],[3.,4.,-3.2]])
Y = np.array([[1,0,1]])

A = 1 / (1 + (-(w.T.dot(X)+b)))
print(A)
print("="*20)

m = X.shape[1]
print(np.log(A))
print(np.log(1-A))
print(Y*np.log(A))
print((1-Y)*np.log(1-A))

cost = -1/m * np.sum(Y*np.log(A) + (1-Y)*np.log(1-A))

print(cost)
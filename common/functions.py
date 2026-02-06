# coding: utf-8
import numpy as np


def identity_function(x):
    return ### 빈칸 ###


def step_function(x):
    return ### 빈칸 ###


def sigmoid(x):
    return ### 빈칸 ###  
    

def relu(x):
    return ### 빈칸 ###
    

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))
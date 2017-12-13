#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__="朴素贝叶斯算法"
"""
基于贝叶斯决策理论的分类方法之朴素贝叶斯

    优点：在数据较少的情况下仍然有效，可以处理多类别问题
    缺点：对于输入数据的准备方式较为敏感
    适用数据类型：标称型数据。

朴素贝叶斯的一般过程

    收集数据：可以使用任何方式
    准备数据：需要数据型或是布尔型数据
    分类数据：有大量特征时，绘制特征作用不大，此时使用直方图效果更好
    训练算法：计算不同的独立特征的条件概率
    测试算法：计算错误率
    使用算法：文档分类

"""

# 1 加载数据集
from numpy import *


def loadDataSet():

    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec
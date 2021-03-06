#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataProcess 
@File    ：filters.py
@Author  ：Zhang Qihang
@Date    ：2021/11/14 18:35 
"""
import numpy as np
import config


def hampel(X):
    length = X.shape[0] - 1
    k = config.HAMPEL
    nsigma = 3
    iLo = np.array([i - k for i in range(0, length + 1)])
    iHi = np.array([i + k for i in range(0, length + 1)])
    iLo[iLo < 0] = 0
    iHi[iHi > length] = length
    xmad = []
    xmedian = []
    for i in range(length + 1):
        w = X[iLo[i]:iHi[i] + 1]
        medj = np.median(w)
        mad = np.median(np.abs(w - medj))
        xmad.append(mad)
        xmedian.append(medj)
    xmad = np.array(xmad)
    xmedian = np.array(xmedian)
    scale = 0.4826  # 缩放
    # scale = 0.0826
    xsigma = scale * xmad
    xi = ~(np.abs(X - xmedian) <= nsigma * xsigma)  # 找出离群点（即超过nsigma个标准差）

    # 将离群点替换为中为数值
    xf = X.copy()
    xf[xi] = xmedian[xi]
    # xf[xi] = None
    return xf

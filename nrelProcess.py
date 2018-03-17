#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 18:16:43 2018

@author: user

选取预测周期

（1）参数相关性分析 
"""
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.decomposition import PCA  

outputfile = "data.xls"
def procData(filename):
    a=[];b=[];c=[];d=[];e=[];f=[];g=[];h=[];i=[];j=[];k=[];l=[];
    with open(filename,'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
                pass
            a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1= [ i for i in lines.split(',')]
            a.append(a1);b.append(b1);c.append(c1);d.append(d1);e.append(e1);f.append(f1);
            g.append(g1);h.append(h1);i.append(i1);j.append(j1);k.append(k1);l.append(l1);
    a=np.array(a);b=np.array(b);c=np.array(c);d=np.array(d);e=np.array(e);f=np.array(f);
    g=np.array(g);h=np.array(h);i=np.array(i);j=np.array(j);k=np.array(k);l=np.array(l);
    s = {"Data":a,"Hour":b.astype(int),"DNI":d.astype(float),"Temp":g.astype(float),"RH":h.astype(float),"Cloud":i.astype(float),"Ws":j.astype(float),"Pres":k.astype(float)}
    df = pd.DataFrame(s,columns=["Data","Hour","Temp","RH","Cloud","Ws","Pres","DNI"])
    return df
dniNrel=procData("Nrel.txt")
#相关系数矩阵 三种方法
a=np.round(dniNrel.corr(method='spearman'),2)
#Lasso
model = linear_model.Lasso(alpha=0.1)
model.fit(dniNrel.iloc[:,1:7],dniNrel['DNI'])
#print(model.coef_)
#PCA
pca = PCA(2)
pca.fit(dniNrel.iloc[:,2:8])
print(pca.explained_variance_ratio_)
low_d = pca.transform(dniNrel.iloc[:,2:8])

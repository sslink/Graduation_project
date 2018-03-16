# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

太阳辐射时空分布特征

（1）多年空间；（2）时间：日、月、季、多年
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#获取目标信息
def getData(filename): 
    dest = []  #Average Clear Sky Diffuse Insolation
    year = []
    mon = []
    day = []
    with open(filename,'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
                pass
            y_temp,m_temp,d_temp,c_temp = [ i for i in lines.split()]
            dest.append(c_temp)
            year.append(y_temp)
            mon.append(m_temp)
            day.append(d_temp)
            pass
        dest = np.array(dest)
        year = np.array(year)
        mon = np.array(mon)
        day = np.array(day)
        pass
    return year,mon,day,dest #meteonorm数据中代表 G_Gh G_Dh Ta FF
#数据滤波(只写了缺省值的滤波)
def dataFilter(data):
    for i in range(np.size(data)):
        if data[i]=='-':
            data[i] = 0.0
        else:
            data[i] = float(data[i])
    return data

#pandas建立数据表 
def dataTable(data1,data2,name):
    s = pd.Series(data2,index=data1)
    df = pd.DataFrame(s,columns = [name])
    return df
#处理数据获得分析几轮
def dataProc(data):
    Sum = data.sum()
    
#NASA数据
year = []
mon = []
day = []
clr_dif = [] #Average Clear Sky Diffuse Insolation
year,mon,day,clr_dif = getData("DI_22.txt")
clr_dnr = [] #Average Clear Sky Direct Normal Radiation 
clr_dnr = getData("DNI_22.txt")[3]
swv_dwn = [] #Average Insolation Incident On A Horizontal Surface (kWh/m^2/day) 
swv_dwn = getData("HI_22.txt")[3]
#meteonorm数据
G_Gh = []
G_Dh = []
Ta = []
FF = []
G_Gh,G_Dh,Ta,FF = getData("Kunlun_Station-hour.txt")
#滤波
clr_dif = dataFilter(clr_dif)
df = dataTable(year,clr_dif.astype(float),"clr_dif")# astpye转化数组数据格式




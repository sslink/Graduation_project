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
<<<<<<< HEAD
def dataTable(data1,data2,data3,data4,name1,name2,name3,name4):
    s = {name1:data1,name2:data2,name3:data3,name4:data4}
    df = pd.DataFrame(s)
    return df
#分析年总辐射量和日均辐射量
def dataAnalyse_YsDm(data,column):
    result=[] 
    #年总辐射量
    Sum = data.sum()/21   #应该从索引中获取！！！！！！
    Sum = Sum[column]
    if Sum>=1750:   #年总辐射量
        print("年总：I 丰富"); result.append('I')
    elif(Sum>=1400):
        print("年总：II 丰富");result.append('II')
    elif(Sum>=1050):
        print("年总：III 丰富");result.append('III')
    else:
        print("年总：一般量");result.append('IIII')
        pass
    #日均辐射量
    dayMean = Light.mean()[column]
    if dayMean >= 4.8:
        print("日均：I 丰富");result.append('I')
    elif dayMean >= 3.8:
        print("日均：II 丰富");result.append('II')
    elif dayMean >= 2.9:
        print("日均：III 丰富");result.append('III')
    else:
        print("日均：一般量");result.append('IIII')
#稳定度分析 针对极昼 月平均(有待改进 目前对pandas掌握不熟 应该按照字符索引筛选)
def dataAnalyse_Stab(data,name,value):
    avMon = []
    avMon.extend([data[value][data[name]=='01'].mean(),data[value][data[name]=='02'].mean(), 
                  data[value][data[name]=='03'].mean(),data[value][data[name]=='04'].mean(), 
                  data[value][data[name]=='05'].mean(),data[value][data[name]=='06'].mean(),  
                  data[value][data[name]=='07'].mean(),data[value][data[name]=='08'].mean(), 
                  data[value][data[name]=='09'].mean(),data[value][data[name]=='10'].mean(), 
                  data[value][data[name]=='11'].mean(),data[value][data[name]=='12'].mean()])
    
    labels = 'Jau','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
    rects = plt.bar(np.arange(12),avMon,width = 0.5,color = 'y',align = "center")
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%.6s' % float(height))
    autolabel(rects)
    plt.show(rects)
#年平均   
def dataAnalyse_avY(data,name,value):
    avYear = []
    Light = data[data[value]>0]   #筛选出极昼极夜并分别建表
    Night = data[data[value]==0]   
    Light[name] = Light[name].astype(int)
    minY = Light[name].min();maxY = Light[name].max()
    #print(minY,maxY)
    for i in range(minY,maxY+1):
       avYear.append(Light[value][Light[name]==i].mean())
    #print(np.size(avYear),avYear)
    labels = 'Jau','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
    plt.plot(labels,avYear,'bp--')
    return 
#季度分析 季节分析  
def dataAnalyse_avSeason(data,name,value):
    avSeason = []#3-5 6-8 9-11 12-2
    Jau = data[value][data[name]=='01'];Feb = data[value][data[name]=='02'];
    Mar = data[value][data[name]=='03'];Apr = data[value][data[name]=='04'];
    May = data[value][data[name]=='05'];Jun = data[value][data[name]=='06'];
    Jul = data[value][data[name]=='07'];Aug = data[value][data[name]=='08'];
    Sep = data[value][data[name]=='09'];Oct = data[value][data[name]=='10'];
    Nov = data[value][data[name]=='11'];Dec = data[value][data[name]=='12'];
    Spring = (Mar.sum()+Apr.sum()+May.sum())/(Mar.count()+Apr.count()+May.count())
    Summer = (Jun.sum()+Jul.sum()+Aug.sum())/(Jun.count()+Jul.count()+Aug.count())
    Autumn = (Sep.sum()+Oct.sum()+Nov.sum())/(Sep.count()+Oct.count()+Nov.count())
    Winter = (Dec.sum()+Jau.sum()+Feb.sum())/(Dec.count()+Jau.count()+Feb.count())
    avSeason = [Spring,Summer,Autumn,Winter]
    print(avSeason)
    labels = ['Spr','Sum','Aut','Win']
    x = range(len(labels))
    plt.plot(x,avSeason,'rp--')
    plt.xticks(x,labels,rotation=45)
    plt.margins(0.08)
    plt.subplots_adjust(bottom=0.15)
    plt.show()
#进一步分析并得出结论
def dataProc(data): 
    print(1)
=======
def dataTable(data1,data2,name):
    s = pd.Series(data2,index=data1)
    df = pd.DataFrame(s,columns = [name])
    return df
#处理数据获得分析几轮
def dataProc(data):
    Sum = data.sum()
>>>>>>> 464d531c2f98c8c7768f9f69c87b1c07ac73c3df
    
#NASA数据
year = []
mon = []
day = []
<<<<<<< HEAD
#clr_dif = [] #Average Clear Sky Diffuse Insolation
#year,mon,day,clr_dif = getData("DI_22.txt")
#clr_dnr = [] #Average Clear Sky Direct Normal Radiation 
#clr_dnr = getData("DNI_22.txt")[3]
swv_dwn = [] #Average Insolation Incident On A Horizontal Surface (kWh/m^2/day) 
year,mon,day,swv_dwn = getData("HI_22.txt")
=======
clr_dif = [] #Average Clear Sky Diffuse Insolation
year,mon,day,clr_dif = getData("DI_22.txt")
clr_dnr = [] #Average Clear Sky Direct Normal Radiation 
clr_dnr = getData("DNI_22.txt")[3]
swv_dwn = [] #Average Insolation Incident On A Horizontal Surface (kWh/m^2/day) 
swv_dwn = getData("HI_22.txt")[3]
>>>>>>> 464d531c2f98c8c7768f9f69c87b1c07ac73c3df
#meteonorm数据
G_Gh = []
G_Dh = []
Ta = []
FF = []
<<<<<<< HEAD
#G_Gh,G_Dh,Ta,FF = getData("Kunlun_Station-hour.txt")
#滤波
swv_dwn = dataFilter(swv_dwn)
df = dataTable(year,mon,day,swv_dwn.astype(float),'year','mon','day','swv_dwn')# astpye转化数组数据格式
Light = df[df['swv_dwn']>0]
dataAnalyse_avSeason(Light,'mon','swv_dwn')
df.plot()
=======
G_Gh,G_Dh,Ta,FF = getData("Kunlun_Station-hour.txt")
#滤波
clr_dif = dataFilter(clr_dif)
df = dataTable(year,clr_dif.astype(float),"clr_dif")# astpye转化数组数据格式
>>>>>>> 464d531c2f98c8c7768f9f69c87b1c07ac73c3df




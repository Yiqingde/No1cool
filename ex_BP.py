# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:41:26 2019
BP神经网络训练模型
@author: Administrator
"""
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
#from sklearn.metrics import roc_curve
#from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
#from sklearn.externals import joblib


# tag表示选择哪一种训练集  
# x_train_num_start：训练集的起始行 x_train_num_end：训练集的结束行
# x_test_num_start：预测集的起始行 x_test_num_end：预测集的结束行
def read_BP(tag,x_train_num_start,x_train_num_end,x_test_num_start,x_test_num_end):
    if tag ==1:
        dates=pd.read_excel("E:\Water quality训练MAXMIN.xlsx",sheet_name=0)
        #print(dates.iloc[:,0:8])#左闭合又开
        x_train=dates.iloc[x_train_num_start:x_train_num_end,0:7]
        y_train=dates.iloc[x_train_num_start:x_train_num_end,8]
        x_test=dates.iloc[x_test_num_start:x_test_num_end,0:7]
        y_test=dates.iloc[x_test_num_start:x_test_num_end,8]
    if tag ==2:
        dates=pd.read_excel("E:\Water quality训练NDWI.xlsx",sheet_name=0)
        x_train=dates.iloc[x_train_num_start:x_train_num_end,0:8]
        y_train=dates.iloc[x_train_num_start:x_train_num_end,8]
        x_test=dates.iloc[x_test_num_start:x_test_num_end,0:8]
        y_test=dates.iloc[x_test_num_start:x_test_num_end,8]
    if tag ==3:
        dates=pd.read_excel("E:\Water quality训练降维.xlsx",sheet_name=0)
        x_train=dates.iloc[x_train_num_start:x_train_num_end,0:5]
        y_train=dates.iloc[x_train_num_start:x_train_num_end,5]
        x_test=dates.iloc[x_test_num_start:x_test_num_end,0:5]
        y_test=dates.iloc[x_test_num_start:x_test_num_end,5]
    '''
    # 神经网络对数据尺度敏感，所以最好在训练前标准化，或者归一化，或者缩放到[-1,1]
    #数据标准化
    scaler = StandardScaler() # 标准化转换
    scaler.fit(x_test)  # 训练标准化对象
    x_test_Standard= scaler.transform(x_test)   # 转换数据集
    scaler.fit(x_train)  # 训练标准化对象
    x_train_Standard= scaler.transform(x_train)   # 转换数据集
    '''
    
    bp=MLPClassifier(hidden_layer_sizes=(100, ), activation='identity', 
    solver='adam', alpha=0.0001, batch_size='auto', 
    learning_rate='constant')
    bp.fit(x_train,y_train.astype('int'))
    y_predict=bp.predict(x_test)
    y_test1=y_test.tolist()
    y_predict=list(y_predict)
    
    for i in range(len(y_test1)):
        y_test1[i]=int(y_test1[i])
        
    print('黑水体预测：\n',classification_report(y_test.astype('int'),y_predict))
    #print("真实数据：\t",y_test1)
    #print("预测数据：\t",y_predict)
    

if __name__ == "__main__":
    read_BP(2,1,2800,2501,2600)

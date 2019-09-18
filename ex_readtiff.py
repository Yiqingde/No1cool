# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:55:58 2019

@author: yiqing
"""

from osgeo import gdal
gdal.AllRegister()
epsion=1e-6

#提取有水部分    
def readtiff_water(filename):    
    dataset = gdal.Open(filename)
    adfGeoTransform = dataset.GetGeoTransform()
    # 左上角地理坐标
    print("adfGeoTransform[0](左上角X):"+str(adfGeoTransform[0]))
    print("adfGeoTransform[1](图像横向分辨率):"+str(adfGeoTransform[1]))
    print("adfGeoTransform[2]（图像旋转系数）:"+str(adfGeoTransform[2]))
    print("adfGeoTransform[3]（左上角Y）:"+str(adfGeoTransform[3]))
    print("adfGeoTransform[4]（图像旋转系数）:"+str(adfGeoTransform[4]))
    print("adfGeoTransform[5](图像纵向分辨率):"+str(adfGeoTransform[5]))
    nXSize = dataset.RasterXSize #列数
    nYSize = dataset.RasterYSize #行数
    cols=nXSize
    rows=nYSize
    band1 = dataset.GetRasterBand(1)
    data1 = band1.ReadAsArray(0, 0, cols, rows)
    band2 = dataset.GetRasterBand(2)
    data2 = band2.ReadAsArray(0, 0, cols, rows)
    band3 = dataset.GetRasterBand(3)  
    data3 = band3.ReadAsArray(0, 0, cols, rows)
    band4 = dataset.GetRasterBand(4)
    data4 = band4.ReadAsArray(0, 0, cols, rows)
    band5 = dataset.GetRasterBand(5)
    data5 = band5.ReadAsArray(0, 0, cols, rows)
    band6 = dataset.GetRasterBand(6)
    data6 = band6.ReadAsArray(0, 0, cols, rows)
    band7 = dataset.GetRasterBand(7)
    data7 = band7.ReadAsArray(0, 0, cols, rows)
    arr_xyband7 = [] # 用于存储每个像素的（X，Y）坐标,及七个波段信息
    for i in range(nYSize):
        row = []
        for j in range(nXSize):
            if ((data3[i,j]-data5[i,j])/(data3[i,j]+data5[i,j]+epsion))>0.02:#ndwi 提取有水部分
                px=adfGeoTransform[0] + i * adfGeoTransform[1] + j * adfGeoTransform[2]
                py=adfGeoTransform[3] + i * adfGeoTransform[4] + j * adfGeoTransform[5]
                b1=data1[i,j]
                b2=data2[i,j] 
                b3=data3[i,j]
                b4=data4[i,j]
                b5=data5[i,j]
                b6=data6[i,j]
                b7=data7[i,j]
                col=[px,py,b1,b2,b3,b4,b5,b6,b7]
                #print(col)
                row.append(col)
        arr_xyband7.append(row)
    print("该卫星图所有像素点个数:"+str(nYSize*nXSize))
    print("有水部分像素点个数:"+str(len(arr_xyband7)))
    print("使用的卫星影像格式(Drivers):"+dataset.GetDriver().ShortName+"/"+dataset.GetDriver().LongName)
    print("Size(横向x纵向)(nXSize x nYSize) : "+str(dataset.RasterXSize)+"x"+str(dataset.RasterYSize)+"\ndim:"+str(dataset.RasterCount))
    #print(dataset.GetProjection()+"\n")
    return arr_xyband7,nXSize,nYSize

#输出部分
def outtoexcel(arr_xyband7,nXSize,nYSize,outfilepath):
    output = open(r'E:\data.xls','w',encoding='gbk')
    all_water=0
    for i in range(500):
        if i==100:
            print(i)
        if i==200:
            print(i)
        if i==300:
            print(i)
        if i==400:
            print(i)
        if i==500:
            print(i)
        if len(arr_xyband7[i])!=0:
            for j in range(len(arr_xyband7[i])): 
                for k in range(9):
                    output.write(str(arr_xyband7[i][j][k]))
                    output.write('\t')
                output.write('\n')
                all_water=all_water+1;
    output.close()
    print("有水部分像素个数:"+str(all_water)+"\t"+"有水部分所占图像比例:"+str(all_water/(nYSize*nXSize)*100)+"%")         
if __name__ == "__main__":
    filename=r"E:\ziliao\dachuang\data\yuchuli\flaash\matlabformat\BaseImage.tif"
    outfilepath=""
    arr_xyband7,nXSize,nYSize=readtiff_water(filename)
    outtoexcel(arr_xyband7,nXSize,nYSize,outfilepath)
    

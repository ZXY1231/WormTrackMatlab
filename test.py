import os,sys
import re
import numpy as np
import linecache
import matplotlib.pyplot as plt
import matplotlib.animation as antt
#infer the haplotypes of SNPs

def PointPlot(x,y):
    x = x
    #print(location[0])
    y = y
    fig,ax = plt.subplots()
    #ax.set_xlim([0,4])
    #ax.set_ylim([0,4])
    #plt.yticks([])
    #plt.xticks([])
    print("Frame",len(x))
    for i in range(len(x)):
        #print(x[0])
        #plt.savefig(r"/Users/apple/Desktop/IGEM/post/tracking/WormTrack/trackfigure/Frame"+numstring(len(str(i)))+str(i)+".png")
        x = [float(i) for i in x]
        y = [float(i) for i in y]
        ax.plot(x[i],y[i],'ro',MarkerSize = 1)
        ax.set_title("Frame_"+str(i))
        plt.pause(10)
        break

if __name__ == "__main__":
    x = [['51.000000', '82.000000', '129.000000', '350.000000', '660.000000'],[]]
    y = [['1530.793991', '2216.237430', '1779.996198', '437.482667', '2456.329759'],[]]

    PointPlot(x,y)
    #PointPlot(point1)
    #PointSubPlot(LocationDenminationChange(ValidPoints))
















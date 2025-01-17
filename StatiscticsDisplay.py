import os,sys
import re
import numpy as np
import linecache
import matplotlib.pyplot as plt
import matplotlib.animation as antt
#infer the haplotypes of SNPs
def read_go(file_name):
    file = linecache.getlines(file_name)
    locations = ''.join(file)
    return locations

def changeformat(locations):
    locations = re.sub(r"\n\t","\t",locations)
    return locations

def getindivilocations(locations):
    #print(locations[0:10000])
    #print(len(re.findall(r"Point \d+.*\n",locations)))
    locations = re.findall(r"Point \d+[xy\d\t\n.]*",locations)
    indilocations = []
    #print(len(locations))
    for i in locations:
        indilocations.append(i)
    #print(indilocations[0])
    Pointdynamics = {}
    for i in indilocations:
        point = i.split("\n")
        x,y = point[2].split(),point[4].split()
        Pointdynamics[point[0]] = [x[10:len(x)-1],y[10:len(y)-1]]
    return Pointdynamics

def PointPlot(location):
    x = location[0]
    #print(location[0])
    y = location[1]
    fig,ax = plt.subplots()
    ax.set_xlim([0,3500])
    ax.set_ylim([0,3500])
    #plt.yticks([])
    #plt.xticks([])
    print("Frame",len(x))
    for i in range(len(x)):
        #print(x[0])
        #plt.yticks([])
        #plt.xticks([])
        #plt.savefig(r"/Users/apple/Desktop/IGEM/post/tracking/WormTrack/trackfigure/Frame"+numstring(len(str(i)))+str(i)+".png")
        #ax.plot(x[i][145:146],y[i][145:146],'ro',MarkerSize = 0.2)
        x[i] = [float(j) for j in x[i]]
        y[i] = [float(j) for j in y[i]]
        ax.plot(x[i][283:284],y[i][283:284],'ro',MarkerSize = 0.2)
        #print(len(x[i]))
        if i>64 and i<70:
            print(x[i][283:284],y[i][283:284])
        ax.set_title("Frame_"+str(i))
        plt.pause(0.02)

def PointSubPlot(location):
    x = location[0]
    #print(location[0])
    y = location[1]
    flg = plt.figure()
    ax = flg.add_subplot(2,2,4)
    ax1 = flg.add_subplot(2,2,1)
    ax2 = flg.add_subplot(2,2,2)
    ax3 = flg.add_subplot(2,2,3)
    ax.set_xlim([0,3500])
    ax.set_ylim([0,3500])
    ax1.set_xlim([0,3500])
    ax1.set_ylim([0,3500])
    ax2.set_xlim([0,3500])
    ax2.set_ylim([0,3500])
    ax3.set_xlim([0,3500])
    ax3.set_ylim([0,3500])
    print("Sub_Frame",len(x))
    for i in range(len(x)):
        #print(x[0])
        ax.plot(x[i],y[i],'ro',MarkerSize = 0.1)
        ax1.plot(x[i][0],y[i][0],'ro',MarkerSize = 2)
        ax2.plot(x[i][101],y[i][101],'ro',MarkerSize = 2)
        ax3.plot(x[i][200],y[i][200],'ro',MarkerSize = 2)
        ax.set_title("Frame_"+str(i))
        plt.pause(0.02)

def ExtractValidPoint(Pointdynamics):
    dis = 0
    ValidPoints = {}
    for i in Pointdynamics:
        [x,y] = Pointdynamics[i]
        dis = 0
        for j in range(len(x)-1):
            distance = ((float(x[j+1])-float(x[j]))**2+(float(y[j+1])-float(y[j]))**2)**(1/2)
            if distance <40:
                dis+=distance
        if dis >400:
            #print(i)
            ValidPoints[i] = Pointdynamics[i]
    return ValidPoints

def ExtractContinuesPoint(ValidPoints,gap = 5):
    dis = True
    count = 0
    ContinuesPoints = {}
    for i in ValidPoints:
        [x,y] = ValidPoints[i]
        for j in range(len(x)-1):
            distance = ((float(x[j+1])-float(x[j]))**2+(float(y[j+1])-float(y[j]))**2)**(1/2)
            if distance >140:
                count+=1
                if count == gap:
                    dis = False
                    break
        if dis:
            ContinuesPoints[i] = ValidPoints[i]
    return ContinuesPoints

def LocationDenminationChange(Points):#for plot multpoints
    points = []#contains all points' locations of one frame in one dimension
    for i in Points:
        points.append(Points[i])
    #print(len(points))
    #print(len(points[0][0]))
    #print(points[0])
    x = []
    y = []
    for i in range(len(points[0][0])):
        x.append([])
        y.append([])
        for j in range(len(points)):
            x[i].append(points[j][0][i])
            y[i].append(points[j][1][i])
    return [x,y]

def animate(i):
    return 
    anim = animation.FuncAnimation

def numstring(num):
    a = ""
    for i in range(num):
        a+="A"
    return a

if __name__ == "__main__":
    locations = read_go("Locations.txt")
    locations = changeformat(locations)
    #print(locations[0:102])
    #file = open("locations_py.txt",'a')
    #file.writelines(locations)
    Pointdynamics = getindivilocations(locations)
    print("points",len(Pointdynamics))
    ValidPoints = ExtractValidPoint(Pointdynamics)
    print("valid",len(ValidPoints))
    #point1 = Pointdynamics['Point 64']
    #print(point1)


    ContinuesPoints = ExtractContinuesPoint(ValidPoints)
    print("Continues",len(ContinuesPoints))
    #PointPlot(LocationDenminationChange(ValidPoints))
    locations = LocationDenminationChange(ValidPoints)
    #print(locations[0][0][0:5],locations[1][0][0:5])
    PointPlot(LocationDenminationChange(Pointdynamics))
    #PointPlot(LocationDenminationChange(ValidPoints))
    #PointPlot(point1)
    #PointSubPlot(LocationDenminationChange(ValidPoints))
















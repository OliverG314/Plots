from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

import pyqtgraph as pg
import random

import sys

class plotBars():
    def __init__(self, data = [], xRange = None, xLabels = None, colorList = None, plotSingleColor = (10, 200, 50), backgroundColor = (0,0,0), title="", left="", bottom="", showText=True):
        self.plot = pg.plot()

        self.plot.addLegend()

        self.data    = data
        self.xLabels = xLabels

        self.plot.setLabel("left", left)
        self.plot.setLabel("bottom", bottom)

        self.plot.setWindowTitle(title)
        
        self.width = 0.8

        if colorList == None: self.brushList = [plotSingleColor for i in self.data]
        else: self.brushList = colorList

        self.plotSingleColor = pg.mkBrush(plotSingleColor)

        self.plot.setBackground(pg.mkBrush(backgroundColor))

        if xRange == None: self.xRange = list(range(len(self.data)))
        else:              self.xRange = xRange

        self.bottomAxis = self.plot.getAxis("bottom")

        if xLabels == None: self.xLabels = ["" for i in self.data]
        else: self.bottomAxis.setTicks([list(zip(range(len(self.xLabels)), tuple(self.xLabels)))])

    def plotLayered(self):
        for i in self.data:
            barGraph = pg.BarGraphItem(x = list(range(len(i))), height = i, width = self.width, brush = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 50))

            self.plot.addItem(barGraph)

    def plotSingle(self):
        barGraph = pg.BarGraphItem(x = self.xRange, height = self.data, width = self.width, brushes = self.brushList)

        self.plot.addItem(barGraph)
        
        for i in range(len(self.data)):
            self.plot.plot([0], brush=self.brushList[i], pen=pg.mkPen(0,0,0), name=self.xLabels[i], fillLevel=0)
            print(1)

    def plotStacked(self):
        yShiftList = []
        
        initBarGraph = pg.BarGraphItem(x = self.xRange, height = self.data[0], width = self.width, brush = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        initBarGraphData = initBarGraph.getData()
        initBarGraphHeight = initBarGraphData[1]

        self.plot.addItem(initBarGraph)

        for i in initBarGraphHeight: yShiftList.append(i)

        for i in range(1,len(self.data)):
            barGraph = pg.BarGraphItem(x = self.xRange, height = self.data[i], y0 = yShiftList, width = self.width, brush = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

            self.plot.addItem(barGraph)

            for j in range(len(yShiftList)): yShiftList[j] += self.data[i][j]

    def plotGrouped(self, gap = 0):
        groupedTicksList = []
        
        for i in range(len(self.data)):
            for i in self.xLabels:
                groupedTicksList.append(i)
            groupedTicksList.append("")
                
        self.bottomAxis.setTicks([list(zip(range(len(groupedTicksList)), tuple(groupedTicksList)))])
        
        rotated = list(zip(*self.data))
        
        for i in rotated:
            currentData = []

            for j in range(rotated.index(i)): currentData.append(0)

            for j in i:
                currentData.append(j)

                if j != i[-1]:
                    for k in range(len(self.data[0])): currentData.append(0)

            barGraph = pg.BarGraphItem(x=list(range(len(currentData))), height = currentData, width = self.width, brush = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

            self.plot.addItem(barGraph)

if __name__ == "__main__":
##    p = plotBars([[1, 5, 8, 2, 5],
##                  [6, 4, 2, 2, 9],
##                  [4, 11, 4, 14, 2]],
##                 xLabels=["1", "2", "3", "4", "5"])
    p = plotBars([1,2,3,4,5],
                 xLabels=["a", "b", "c", "d", "e"])
    
##    p = plotBars([[306.73,  318.85,    355.68,    458.36,    278.19,    368.06,    170.17,   467.15, 451.24,  421.11,    264.96,  233.59,  305.18,  388.38,   344.88],#, 180.54],
##                  [817717,  1060901,   1393416,   1779109,   1307927,   1633111,   2046621, 2191484, 2288428, 2048836,   1356704, 1280648, 1575140, 1653005,  1690050]],
##                 xRange = range(2005, 2020),
##                 left="GDP (millions)",
##                 bottom="Year")

##    p = plotBars([20940, 13400, 4970, 4000, 2830, 379.27],
##                 colorList = [(25, 250, 75),
##                              (25, 250, 75),
##                              (25, 250, 75),
##                              (25, 250, 75),
##                              (25, 250, 75),
##                              (25, 75, 250)])

##    p1 = plotBars([22939.580, 16862.979, 5103.110, 4230.172, 3108.416, 379.27],
##                 colorList = [(25, 250, 75),
##                              (25, 250, 75),
##                              (25, 250, 75),
##                              (25, 250, 75),
##                              (25, 250, 75),
##                              (25, 75, 250)],
##                  xLabels = ["USA", "China", "Japan", "Germany", "UK", "Shell"],
##                  left = "USD (Billions)",
##                  bottom = "Country",
##                  title = "Total assets of Shell compared with GDP of other countries")
##
##    p2 = plotBars([414.6, 396.5, 392.9, 303.73, 290.2, 209.4],
##                  colorList = [(25, 250, 75),
##                               (25, 75, 250),
##                               (25, 250, 75),
##                               (25, 250, 75),
##                               (25, 250, 75),
##                               (25, 250, 75)],
##                  xLabels = ["Saudi Aramco", "Shell", "CNPC", "BP", "Exxon Mobil", "Total SA"],
##                  left = "USD (Billion)",
##                  bottom = "Company",
##                  title = "Revenue of Shell compared with other oil companies (2018)")
                               
##    p1.plotSingle()
##    p2.plotSingle()

##    p.plotGrouped()

    p.plotSingle()

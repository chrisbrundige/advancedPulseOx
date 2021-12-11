import pandas as pd
import math
#import matplotlib.pyplot as plt
import WaveForm
import pandas as pd
import numpy as np
from datetime import datetime
#import matplotlib.pyplot as plt
#from scipy import signal

# variables
a = 0,
b = 0,
c = 0,
d = 0,
e = 0,
start = 0,
end = 0,
rate = 60
r1 = 0,
r2 = 0,
irregular = True
# import raw data
df = pd.read_csv('data.csv')


# reformat data
df = df.drop(df.columns[[1, 3, 4, 5]], axis=1)
df = df.rename(columns={"Time [s]": "time", " PLETH": 'pleth'})

# X & Y values
x = df['time']
y = df['pleth'].round(4)
x = x[0:100]
y = y[0:100]
inflection_points = []


# Format Parameters

# Write Functions
def calcInflectionPoints(x, y):
    increasing = False

    newMaxMin = 0
    inflection_points = []

    for index, n in enumerate(y):

        if increasing == True:
            if index < 90 and n < y[index + 1]:
                newMaxMin = n
            else:
                inflection_points.append({'x': x[index], 'y': newMaxMin, 'delta': -1})
                increasing = False
        else:
            if index < 90 and n > y[index + 1]:
                newMaxMin = n
            else:
                inflection_points.append({'x': x[index], 'y': newMaxMin, 'delta': 1})
                increasing = True
    return inflection_points


def arterialStiffness(b, a):
    return b / a;


def leftVentricularAfterload(d, a):
    return d / a


def vascularAging(b, c, d, e, a):
    return (b - c - d - e) / a


def APGAgingIndex(a, b, c, d):
    return (c + d - b) / a


# def calcArea():


def cardiacOutput():
    return 1


def heartRate():
    return rate;


# Return Data

def returnAllData(a, b, c, d, e):
    print(

        f'arterial Stiffness: {arterialStiffness(b, a)} \n'
        f'leftVentricularAfterword:{leftVentricularAfterload(d, a)}\n'
        f'vascularAging:{vascularAging(b, c, d, e, a)}\n'
        f'APGAgingIndex:{APGAgingIndex(a, b, c, d)}\n'
        f'heartRate:{heartRate()}\n'
        f'cardiacOutput:{cardiacOutput(a)}\n'
        f'irregular:{irregular}\n'

    )


ptOne = WaveForm
ip = calcInflectionPoints(x,y)
ptOne.inflection_points = ip
print(ptOne.inflection_points)

# returnAllData(90, 32, 10, 12, 4)

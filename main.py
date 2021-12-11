import pandas as pd

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
irregular = True,
inflectionPoints=[],
diacroticNotch = 35


# import raw data
data = pd.read_csv('data.csv')
patientOne = data[1]
print(patientOne)






# Format Parameters

# Write Functions
def calculateinflectionPoints():
    return 1;

def arterialStiffness(b, a):
    return b / a;


def leftVentricularAfterload(d, a):
    return d / a


def vascularAging(b, c, d, e, a):
    return (b - c - d - e) / a


def APGAgingIndex(a, b, c, d):
    return (c + d - b) / a

#def calcArea():


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


returnAllData(90, 32, 10, 12, 4)

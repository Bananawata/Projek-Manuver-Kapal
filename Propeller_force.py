import math
import openpyxl

wb = openpyxl.load_workbook("input.xlsx",)
sheet = wb.active

L= sheet['B4'].value
Cb= sheet['B3'].value
d= sheet['B6'].value
n= sheet['B9'].value
Dp= sheet['B10'].value
C1= sheet['B18'].value; C2= sheet['B19'].value; C3= sheet['B20'].value #inputan user


def propeller(var):
    betap= var[1]-(-0.5)*var[2]
    Wp0= 0.5*Cb-0.05
    Wp= Wp0*math.exp(-4*pow(betap,2))
    Jp= var[0]*math.cos(var[1])*(1-Wp)/(n*Dp)
    Kt= C1+C2*Jp+C3*pow(Jp,2)
    XP= (1-(-0.27))*pow(n, 2)*pow(Dp, 4)*Kt*Jp/(L*d*pow(var[0], 2)/2)

    return XP

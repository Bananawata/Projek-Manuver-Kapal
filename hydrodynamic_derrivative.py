from added_mass_value import my, mm, mxx
import math
import openpyxl

wb = openpyxl.load_workbook("input.xlsx",)
sheet = wb.active

Cb= sheet['B3'].value
L= sheet['B4'].value
B= sheet['B5'].value
d= sheet['B6'].value

#   X_axis====================================================================
#   Xo=  hambatan total thdp kecepatan kapal
Xvv= 1.15*Cb/(L/B)-0.18
Xvr= my-1.91*Cb/(L/B)+0.08
Xrr= (-0.0027+0.0076*Cb*d/B)*L/d
Xvvvv= -6.68*Cb/(L/B)+1.1
#print(Xvv, Xvr, Xrr, Xvvvv)

#   Y_axis====================================================================
YB= (math.pi*d/L)+1.4*Cb*B/L
Yr= mm+mxx-1.5*Cb*B/L  
YBB= 2.5*d*(1-Cb)/B+0.5
Yrr= 0.343*d*Cb/B-0.07
YBBr= 1.5*d*Cb/B-0.65
Ybrr= 5.95*d*(1-Cb)/B
#print(YB, Yr, YBB, Yrr, YBBr, Ybrr)

#   N_axis====================================================================
k= 2*d/L
NB= k
Nr= -0.54*k+pow(k, 2)
NBB= -0.96*d*(1-Cb)/B+0.066
Nrr= 0.5*Cb*B/L-0.09
NBBr= -(57.5*pow(Cb*B/L, 2)-(18.4*Cb*B/L)+1.6)
Nbrr= -(0.5*d*Cb/B-0.05)
#print(NB, Nr, NBB, Nrr, NBBr, Nbrr)
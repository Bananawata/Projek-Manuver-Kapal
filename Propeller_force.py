import math

L= 3
Cb= 0.435
d= 0.1629
n= 1; Dp= 0.11144
C1= 0.5094; C2= -0.31857; C3= -0.14286 #inputan user


def propeller(var):
    betap= var[1]-(-0.5)*var[2]
    Wp0= 0.5*Cb-0.05
    Wp= Wp0*math.exp(-4*pow(betap,2))
    Jp= var[0]*math.cos(var[1])*(1-Wp)/(n*Dp)
    Kt= C1+C2*Jp+C3*pow(Jp,2)
    XP= (1-(-0.27))*pow(n, 2)*pow(Dp, 4)*Kt*Jp/(L*d*pow(var[0], 2)/2)

    return XP

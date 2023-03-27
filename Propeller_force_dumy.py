import math
from hydrodynamic_derrivative_dumy import Xuu

L= 3
Cb= 0.435
d= 0.1629
Dp= 0.11144
C1= 0.5094; C2= -0.31857; C3= -0.14286 #inputan user    


def propeller(var):
    Wp0= 0.5*Cb-0.05
    tp = 0.6*Wp0
    pa = C1*pow(Dp,4)
    pb = C2*pow(Dp,3)*var[0]*(1-Wp0)
    pc = C3*pow(Dp,2)*var[0]*pow((1-Wp0),2)+0.5*L*d*pow(var[0],2)*Xuu/(1-tp)
    n = (-pb + math.sqrt(pow(pb,2) - 4*pa*pc))/(2*pa)

    betap= var[1]-(-0.5)*var[2]
    Wp= Wp0*math.exp(-4*pow(betap,2))
    Jp= var[0]*math.cos(var[1])*(1-Wp)/(n*Dp)
    Kt= C1+C2*Jp+C3*pow(Jp,2)
    XP= (1-(tp))*pow(n, 2)*pow(Dp, 4)*Kt/(L*d*pow(var[0], 2)/2)

    return XP
    #print(betap, Wp, Jp, Kt, Xp)

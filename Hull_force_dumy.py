from hydrodynamic_derrivative_dumy import *
import math


def hull(var):
    XH= Xbr*var[2]*math.sin(var[1])+Xuu*pow(math.cos(var[1]),2)
    YH= YB*var[1]+Yr*var[2]+YBB*var[1]*abs(var[1])+Yrr*var[2]*abs(var[2])+(YBBr*var[1]+Ybrr*var[2])*var[1]*var[2]
    NH= NB*var[1]+Nr*var[2]+NBB*var[1]*abs(var[1])+Nrr*var[2]*abs(var[2])+(NBBr*var[1]+Nbrr*var[2])*var[1]*var[2]
    
    return XH, YH, NH
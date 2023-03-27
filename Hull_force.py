from hydrodynamic_derrivative import *

U= 1; rr= 1; beta= 1; r= rr*U/L

def hull(var):
    XH= Xvv*pow(var[2],2) + Xvr*var[2]*var[1] + Xrr*pow(var[1],2) + Xvvvv*pow(var[2],4)
    YH= YB*var[1]+Yr*var[2]+YBB*var[1]*abs(var[1])+Yrr*var[2]*abs(var[2])+(YBBr*var[1]+Ybrr*var[2])*var[1]*var[2]
    NH= NB*var[1]+Nr*var[2]+NBB*var[1]*abs(var[1])+Nrr*var[2]*abs(var[2])+(NBBr*var[1]+Nbrr*var[2])*var[1]*var[2]
    
    return XH, YH, NH
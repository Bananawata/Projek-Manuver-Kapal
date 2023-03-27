from hydrodynamic_derrivative import *

U= 1; rr= 1; beta= 1; r= rr*U/L

def hull(var):
    XH= Xvv*pow(U,2) + Xvr*U*r + Xrr*pow(r,2) + Xvvvv*pow(U,4)
    YH= YB*beta+Yr*rr+YBB*beta*abs(beta)+Yrr*rr*abs(rr)+(YBBr*beta+Ybrr*rr)*beta*rr
    NH= NB*beta+Nr*rr+NBB*beta*abs(beta)+Nrr*rr*abs(rr)+(NBBr*beta+Nbrr*rr)*beta*rr
    
    return XH, YH, NH
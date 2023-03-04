from hydrodynamic_derrivative import *

if __name__ == '__main__':
    XH= Xvv*pow(U,2) + Xvr*U*r + Xrr*pow(r,2) + Xvvvv*pow(U,4)
    YH= YB*beta+Yr*r+YBB*beta*abs(beta)+Yrr*r*abs(r)+(YBBr*beta+Ybrr*r)*beta*r
    NH= NB*beta+Nr*r+NBB*beta*abs(beta)+Nrr*r*abs(r)+(NBBr*beta+Nbrr*r)*beta*r
    print(XH, YH, NH)
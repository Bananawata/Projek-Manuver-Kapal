import numpy as np

L= 1; U= 1; Cb= 1; n= 1; Dp= 1; d= 1
C1= 1; C2= 1; C3= 1; r= 1; Ctp= 1 #inputan user
beta= 1

rr= r*L/U
betap= beta-(-0.5)*rr
Wp0= 0.5*Cb-0.05
Wp= Wp0*np.exp(-4*pow(betap,2))
Jp= U*np.cos(beta)*(1-Wp)/(n*Dp)
Kt= C1+C2*Jp+C3*pow(Jp,2)
Xp= Ctp*(1-(-0.27))*pow(n, 2)*pow(Dp, 4)*Kt*Jp/(L*d*pow(U, 2)/2)
#print(betap, Wp, Jp, Kt, Xp)

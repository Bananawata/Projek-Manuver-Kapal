from Propeller_force import *
import numpy as np


Wr0= 1; C= 1; delta= 1; y= 1; P= 1; Kr= 1  # inputan user
hr= 1; Ar= 1; L= 1; d= 1; B= 1


betar= beta-2*(-0.5)*rr
alpar= delta-y*betar
Wr= Wr0*Wp/Wp0
s= 1-(1-Wp)*U*np.cos(beta)*n*P
K= 0.6*(1-Wp)/(1-Wr)
nn= Dp/hr
gs= nn*K*(2-(2-K)*s)*s/(pow(1-s,2))
Ur= pow(1-Wr,2)*(1+C*gs)
Cn= 6.13*Kr/(Kr+2.25)
Fn= (Ar/(L*d))*Cn*pow(Ur, 2)*np.sin(alpar)

tr= 0.45-0.28*Cb
ah= 3.6*Cb*B/L
Xr= -(1-tr)*Fn*np.sin(delta)
Yr= -(1+ah)*Fn*np.cos(delta)
Nr= -(xrr+ah*xhh)*Fn*np.cos(delta)

#print(betar, alpar, Wr, s, K, nn, gs, Ur, Cn, Fn)
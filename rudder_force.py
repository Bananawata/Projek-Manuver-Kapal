import math


Wr0= 0.622; delta= 10; gamma= 0.332; P= 0.1175 # inputan user
L= 3
Cb= 0.435
d= 0.1629
Dp= 0.11144
hr= 0.132; Ar= 0.0078433

xhh = 9.72289*pow(Cb,2)-8.243538*Cb-0.00498539
if xhh > -0.45:
    xhh = -0.45

if delta > 0:
    C = 0.935
else:   
    C = 1.065

def rudder(var):
    xpp = -0.05
    betap= var[1]-(xpp)*var[2]
    Wp0= 0.5*Cb-0.05
    Wp= Wp0*math.exp(-4*pow(betap,2))
    
    
    xrr= -0.5
    beta_r= var[1]-2*(xrr)*var[2]
    alpa_r= delta-gamma*beta_r
    Wr= Wr0*Wp/Wp0
    mu = Dp/hr
    s= 1-(1-Wp)*var[0]*math.cos(var[1])/mu*P
    K= 0.6*(1-Wp)/(1-Wr)
    gs= mu*K*(2-(2-K)*s)*s/(pow(1-s,2))

    Ur= pow(1-Wr,2)*(1+C*gs)
    Kr = pow(hr, 2)/Ar
    Cn= 6.13*Kr/(Kr+2.25)

    tr= 0.45-0.28*Cb
    ah= 2.2835*pow(Cb,2)-0.833*Cb
    if ah>0.82:
        ah=0.82

    Fn= (Ar/(L*d))*Cn*Ur*math.sin(alpa_r)
    XR= -(1-tr)*Fn*math.sin(delta)
    YR= -(1+ah)*Fn*math.cos(delta)
    NR= -(xrr+ah*xhh)*Fn*math.cos(delta)

    return XR, YR, NR

    #print(beta_r, alpar, Wr, s, K, nn, gs, Ur, Cn, Fn)
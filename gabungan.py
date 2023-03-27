from scipy.integrate import odeint
import matplotlib.pyplot as plt
from Maneuver import model
import numpy as np
import math

print("Masukkan data")

print("Ship Dimension")
m = float(input("Ship Mass (m): "))
Cb = float(input("Block Coefficient (Cb): "))
l = float(input("Ship Length (l): "))
b = float(input("Breadth (b): "))
d = float(input("Draft (d): "))
rho = float(input("Fluid Density (rho): "))

print(30*"=")
print("Propeller")
n = float(input("Propeller Revolution (n): "))
Dp = float(input("Propeller Diameter (Dp): "))
P = float(input("Propeller Pitch (P): "))

print(30*"=")
print("Rudder")
Ar = float(input("Rudder Area (AR): "))
KR = float(input("Aspect Ratio of Rudder (KR): ")) #tidak dipanggil
hr = float(input("Rudder Height (hR): "))

print(30*"=")
print("Tambahan")
Izz = float(input("Izz: "))
C1 = float(input("C1: "))
C2 = float(input("C2: "))
C3 = float(input("C3: "))
Wr0 = float(input("Wr0: "))
delta = float(input("delta: "))
gamma = float(input("gamma: "))
P = float(input("P: "))

# ADDED MASS VALUE
mx = m * 0.05
my = m * (0.882 - 0.54 * Cb * (1-1.6*d/b)- 0.156 * (1-0.673*Cb) * l/b  + 0.826 * d/b * l/b*(1-0.678*d/b) - 0.638 * Cb * d/b * l/b * (1-0.669*d/b))
jz = m * (1/100 * (33 - 76.85 * Cb * (1-0.784*Cb) + 3.43 * l/b * (1-0.63*Cb))) ** 2

mm = m/(1/2*rho*(l**2)*d)
mxx = mx/(1/2*rho*(l**2)*d)
myy = my/(1/2*rho*(l**2)*d)
Jzz = jz/(1/2*rho*(l**4)*d)


# HYDRODYNAMIC DERRIVATIVE

#   X_axis====================================================================
#   Xo=  hambatan total thdp kecepatan kapal
Xvv= 1.15*Cb/(l/b)-0.18
Xvr= my-1.91*Cb/(l/b)+0.08
Xrr= (-0.0027+0.0076*Cb*d/b)*l/d
Xvvvv= -6.68*Cb/(l/b)+1.1
#print(Xvv, Xvr, Xrr, Xvvvv)

#   Y_axis====================================================================
YB= (math.pi*d/l)+1.4*Cb*b/l
Yr= mm+mxx-1.5*Cb*b/l  
YBB= 2.5*d*(1-Cb)/b+0.5
Yrr= 0.343*d*Cb/b-0.07
YBBr= 1.5*d*Cb/b-0.65
Ybrr= 5.95*d*(1-Cb)/b
#print(YB, Yr, YBB, Yrr, YBBr, Ybrr)

#   N_axis====================================================================
k= 2*d/l
NB= k
Nr= -0.54*k+pow(k, 2)
NBB= -0.96*d*(1-Cb)/b+0.066
Nrr= 0.5*Cb*b/l-0.09
NBBr= -(57.5*pow(Cb*b/l, 2)-(18.4*Cb*b/l)+1.6)
Nbrr= -(0.5*d*Cb/b-0.05)
#print(NB, Nr, NBB, Nrr, NBBr, Nbrr)

# HULL FORCE
def hull(var):
    XH= Xvv*pow(var[2],2) + Xvr*var[2]*var[1] + Xrr*pow(var[1],2) + Xvvvv*pow(var[2],4)
    YH= YB*var[1]+Yr*var[2]+YBB*var[1]*abs(var[1])+Yrr*var[2]*abs(var[2])+(YBBr*var[1]+Ybrr*var[2])*var[1]*var[2]
    NH= NB*var[1]+Nr*var[2]+NBB*var[1]*abs(var[1])+Nrr*var[2]*abs(var[2])+(NBBr*var[1]+Nbrr*var[2])*var[1]*var[2]
    
    return XH, YH, NH

# PROPELLER FORCE
def propeller(var):
    betap= var[1]-(-0.5)*var[2]
    Wp0= 0.5*Cb-0.05
    Wp= Wp0*math.exp(-4*pow(betap,2))
    Jp= var[0]*math.cos(var[1])*(1-Wp)/(n*Dp)
    Kt= C1+C2*Jp+C3*pow(Jp,2)
    XP= (1-(-0.27))*pow(n, 2)*pow(Dp, 4)*Kt*Jp/(l*d*pow(var[0], 2)/2)

    return XP


# RUDDER FORCE
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

    Fn= (Ar/(l*d))*Cn*Ur*math.sin(alpa_r)
    XR= -(1-tr)*Fn*math.sin(delta)
    YR= -(1+ah)*Fn*math.cos(delta)
    NR= -(xrr+ah*xhh)*Fn*math.cos(delta)

    return XR, YR, NR

    #print(beta_r, alpar, Wr, s, K, nn, gs, Ur, Cn, Fn)

# MANEUVER
def model(var, t):

    XP = propeller(var)
    XR, YR, NR = rudder(var)
    XH, YH, NH = hull(var)
    

    X = XH+XP+XR
    Y = YH+YR
    N = NH+NR

    dUdt = (pow(var[0],2)/l)*((X/(mm+mxx))*math.cos(var[1])-(Y/(mm+myy))*math.sin(var[1])-(((mm+myy)/(mm+mxx))-((mm+mxx)/(mm+myy)))*var[2]
            *math.sin(var[1])*math.cos(var[1]))
    dbdt = (var[0]/l)*((mm+mxx)/(mm+myy))*var[2]*pow(math.cos(var[1]), 2)+((mm+myy)/(mm+mxx))*var[2]*pow(math.sin(var[1]), 2)-((1/(mm+mxx))
            *math.sin(var[1])*X)-((1/(mm+myy))*math.cos(var[1])*Y)
    drdt = (var[0]/l)*(N/(Izz+Jzz))-var[2]*(var[0]/l)*((X/(mm+mxx))*math.cos(var[1])-(Y/(mm+myy))*math.sin(var[1])-(((mm+myy)/(mm+mxx))-((mm+mxx)/(mm+myy)))
            *var[2]*math.sin(var[1])*math.cos(var[1]))
    psi= var[0]*var[2]/l
    x0 = var[0]*math.cos(var[3]-var[1])
    y0 = var[0]*math.sin(var[3]-var[1])

    dydt = [dbdt, drdt, dUdt, psi, x0, y0]
    
    return dydt





# kondisi awal
y = [0.337, 0, 0, 0, 0, 0] #[U, beta, r, psi, x0, y0]

# waktu
def makeTime(start, end, dot):
    t = []
    jump = (start+end)/(dot-1)

    t.append(0)
    iterJump = jump
    for i in range(dot-1):
        t.append(iterJump)
        iterJump = iterJump + jump
    return t

t = makeTime(0, 10, 1001)
#t = np.linspace(0, 2, 101)

# selesaikan persamaan diferensial
dydt = odeint(model, y, t)

p1 = plt.plot(dydt[:, 4],dydt[:, 5],'-')
plt.title('Grafik Manuever Kapal')
plt.xlabel('time(t)')
plt.ylabel("Derajat($^o$)")
#plt.legend( (p1[0]), ('Beta'), loc='best' )
plt.show()
#print(dydt)
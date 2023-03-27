m = 0.2036 #nilai sebenarnya mm = 0.271
cb = 0.5717
l = 3
b = 0.435
d = 0.1629
rho = 1.025

mx = m * 0.05
my = m * (0.882 - 0.54 * cb * (1-1.6*d/b)- 0.156 * (1-0.673*cb)*l/b + 0.826 * d/b * l/b*(1-0.678*d/b) - 0.638 * cb * d/b * l/b * (1-0.669*d/b))
Jz = m * (1/100 * (33 - 76.85 * cb * (1-0.784*cb) + 3.43 * l/b * (1-0.63*cb))) ** 2 #added inertia ship

mm = 0.271
mxx = 0.0208
myy = 0.2286
Jzz = 0.0156
Izz = 0.0088


#print(mx,my,jz,mm,mxx,myy,izz)
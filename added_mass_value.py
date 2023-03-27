m,cb,l,b,d,rho = 1,1,1,1,1,1


mx = m * 0.05
my = m * (0.882 - 0.54 * cb * (1-1.6*d/b)- 0.156 * (1-0.673*cb)*l/b 
    + 0.826 * d/b * l/b*(1-0.678*d/b) - 0.638 * cb * d/b * l/b * (1-0.669*d/b))
    
jz = m * (1/100 * (33 - 76.85 * cb * (1-0.784*cb) + 3.43 * l/b * (1-0.63*cb))) ** 2

mm, mxx, myy = m/(1/2*rho*(l**2)*d), mx/(1/2*rho*(l**2)*d), my/(1/2*rho*(l**2)*d)
jzz = jz/(1/2*rho*(l**4)*d)

#print(mx,my,jz,mm,mxx,myy,jzz)
# kjflzsjfdlkzjflkzsdjf
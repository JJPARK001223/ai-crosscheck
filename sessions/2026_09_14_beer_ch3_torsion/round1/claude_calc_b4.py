import math
pi=math.pi
def Js(c): return pi*c**4/2
def Jh(c2,c1): return (pi/2)*(c2**4-c1**4)

def Tp_solid(c,tauY): return (2*pi/3)*c**3*tauY  # fully plastic
def TY_solid(c,tauY): return (pi/2)*c**3*tauY     # yield-onset torque
def T_elastoplastic(c,tauY,rhoY):
    TY=TY_solid(c,tauY)
    return (4/3)*TY*(1-0.25*(rhoY/c)**3)

print("=== 3.92 ===")
c=15.0; tauY=3.5; rhoY=12.5
T=T_elastoplastic(c,tauY,rhoY)
print("T=",T,"N*mm =",T/1000,"N*m")

print("=== 3.94 ===")
c=15.0; tauY=145.0; G=77200.0
TY=TY_solid(c,tauY)
print("TY=",TY, TY/1000)
for T in [600000.,1000000.]:
    if T<=TY:
        tau=2*T/(pi*c**3)
        print("T=",T/1000,"elastic, tau=",tau,"no plastic core")
    else:
        # solve rhoY from T=(4/3)TY(1-0.25(rhoY/c)^3)
        ratio = 1-(3*T)/(4*TY)
        rhoY3 = ratio*(-4)*c**3   # from 1-(4T/3TY)=... let's just invert numerically
        # (1/4)(rhoY/c)^3 = 1-3T/(4TY)
        val = 1-(3*T)/(4*TY)
        rhoYc3 = 4*val
        rhoY = c*(rhoYc3)**(1/3)
        print("T=",T/1000,"plastic, tau_max=tauY=",tauY,"rhoY=",rhoY)

print("=== 3.96 ===")
c=0.45
Tp=60.0 #N*mm
tauY=3*Tp/(2*pi*c**3)
print("tauY=",tauY)

print("=== 3.98 (3.93 base: c=32mm, assume G=77000 since not stated) ===")
c=32.0; tauY=145.0; L=1200.0; G=77000.0
for depth in [15.,25.]:
    rhoY=c-depth
    phi=tauY*L/(G*rhoY)
    print("depth=",depth,"rhoY=",rhoY,"phi(deg)=",math.degrees(phi))

print("=== 3.100 ===")
c=31.0; G=77200.0; tauY=147.0; L=900.0
phiY=tauY*L/(G*c)
print("phiY(deg)=",math.degrees(phiY))
J=Js(c)
for phi_deg in [2.5,5.0]:
    phi=math.radians(phi_deg)
    if phi<=phiY:
        T=phi*J*G/L
        print("phi=",phi_deg,"elastic T=",T/1000)
    else:
        rhoY=phiY*c/phi   # since phi/phiY=c/rhoY => rhoY=phiY*c/phi... check: phi=tauY*L/(G*rhoY), phiY=tauY*L/(G*c) => phi/phiY=c/rhoY => rhoY=c*phiY/phi
        T=T_elastoplastic(c,tauY,rhoY)
        print("phi=",phi_deg,"plastic rhoY=",rhoY,"T=",T/1000)

print("=== 3.102 (T value cut off in scan - method only, using placeholder) ===")
c=6.0; tauY=90.0; G=30000.0; L=2000.0
TY=TY_solid(c,tauY)
print("TY=",TY, "T_p=",Tp_solid(c,tauY))
print("(T value from scan illegible - cannot finalize numeric rhoY/phi)")

print("=== 3.104 ===")
c=9.0; tauY=145.0; G=77000.0; L=1200.0; T=200000.0
TY=TY_solid(c,tauY)
print("TY=",TY/1000)
val=1-(3*T)/(4*TY)
rhoY=c*(4*val)**(1/3)
phi=tauY*L/(G*rhoY)
print("rhoY=",rhoY,"tau_max=",tauY,"phi(deg)=",math.degrees(phi))

print("=== 3.106 ===")
c2,c1=35.0,15.0
tauY=180.0; G=77200.0; L=900.0
J=Jh(c2,c1)
TY=tauY*J/c2
phiY=tauY*L/(G*c2)
print("(a) TY=",TY/1000,"phiY(deg)=",math.degrees(phiY))
def T_hollow_plastic(c2,c1,tauY,rhoY):
    return (pi*tauY/2)*(rhoY**4-c1**4)/rhoY + (2*pi*tauY/3)*(c2**3-rhoY**3)
rhoY=25.0
T_b=T_hollow_plastic(c2,c1,tauY,rhoY)
phi_b=tauY*L/(G*rhoY)
print("(b) rhoY=25, T=",T_b/1000,"phi(deg)=",math.degrees(phi_b))

print("=== 3.108 ===")
T=4520000.0; tauY=145.0
d_B,d_C=62.,50.; Ltot=100.0
c_C=d_C/2
TY_C=TY_solid(c_C,tauY)
val=1-(3*T)/(4*TY_C)
rhoY_C=c_C*(4*val)**(1/3)
depth=c_C-rhoY_C
print("TY_C=",TY_C/1000,"rhoY_C=",rhoY_C,"plastic depth=",depth)
# find x_E where local elastic surface stress = tauY
cE3 = 2*T/(pi*tauY)
cE = cE3**(1/3)
# c(x) = 31 - 0.06x (31=d_B/2, slope=(31-25)/100=0.06)
cB=d_B/2.0
slope=(cB - d_C/2.0)/Ltot
xE=(cB-cE)/slope
print("cE=",cE,"xE(BE length)=",xE)

print("=== 3.110 (numeric integration using graph pts (0,0)(0.002,56)(0.004,84)(0.010,112)) ===")
import numpy as np
gpts=[(0,0),(0.002,56),(0.004,84),(0.010,112)]
def tau_of_gamma(g):
    for i in range(len(gpts)-1):
        g0,t0=gpts[i]; g1,t1=gpts[i+1]
        if g0<=g<=g1:
            return t0+(t1-t0)*(g-g0)/(g1-g0)
    return gpts[-1][1]
c2,c1=7.5,2.5
L=225.0
phi=math.radians(10.0)
N=2000
rs=[c1+(c2-c1)*i/N for i in range(N+1)]
vals=[]
for r in rs:
    g=r*phi/L
    tau=tau_of_gamma(g)
    vals.append(tau*r*r)
# simpson
h=(c2-c1)/N
S=vals[0]+vals[-1]
for i in range(1,N):
    S+= (4 if i%2==1 else 2)*vals[i]
S*=h/3
T=2*pi*S
print("gamma(c1)=",c1*phi/L,"gamma(c2)=",c2*phi/L)
print("T=",T," N*mm =",T/1000,"N*m")

print("=== 3.114 (T=8.475kN*m vs Tp check) ===")
c=15.0; tauY=154.0
TY=TY_solid(c,tauY); Tp=Tp_solid(c,tauY)
print("TY=",TY/1000,"Tp=",Tp/1000,"applied T=8475 N*m -> exceeds Tp, INCONSISTENT")

print("=== 3.116 ===")
c=8.0; tauY=145.0; G=77200.0; L=600.0
phiY=tauY*L/(G*c)
print("phiY(deg)=",math.degrees(phiY),"applied=6deg -> ", "STAYS ELASTIC" if 6<math.degrees(phiY) else "YIELDS")

print("=== 3.118 ===")
c2,c1=30.0,12.5
tauY=145.0
J=Jh(c2,c1)
Tmax=(2*pi*tauY/3)*(c2**3-c1**3)  # fully plastic hollow (rhoY=c1)
print("Tmax(fully plastic to inner)=",Tmax/1000)
tau_res_outer = tauY - Tmax*c2/J
tau_res_inner = tauY - Tmax*c1/J
print("residual at outer(c2)=",tau_res_outer,"residual at inner(c1)=",tau_res_inner)

print("=== 3.120 symbolic check ===")
print("tau_res(rho)=tauY*(1-(4/3)(rho/c)); at rho=c -> ",1-4/3)

print("=== 3.112 (points (0,0)(0.0015,55)(0.003,80) from 3.113 text) ===")
gpts2=[(0,0),(0.0015,55),(0.003,80)]
def tau2(g):
    for i in range(len(gpts2)-1):
        g0,t0=gpts2[i]; g1,t1=gpts2[i+1]
        if g0<=g<=g1+1e-9:
            return t0+(t1-t0)*(g-g0)/(g1-g0)
    return gpts2[-1][1]
c=25.0
L=725.0
phi=math.radians(5.0)
N=2000
h=c/N
S=0
vals=[]
for i in range(N+1):
    r=i*h
    g=r*phi/L
    vals.append(tau2(g)*r*r)
S=vals[0]+vals[-1]
for i in range(1,N):
    S+=(4 if i%2==1 else 2)*vals[i]
S*=h/3
T=2*pi*S
print("gamma_max=",c*phi/L,"T=",T/1000,"N*m")

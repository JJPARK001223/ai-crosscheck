import math
pi=math.pi
def Jh(c2,c1): return (pi/2)*(c2**4-c1**4)
def Js(c): return pi*c**4/2

print("=== 3.62 ===")
k=6000.0; L=1800.0; G=77000.0
J=k*L/G
c=(2*J/pi)**0.25
print("J=",J,"c=",c,"d=",2*c)

print("=== 3.64 ===")
c=6.0
P=2500.0
for f in [25,50]:
    w=2*pi*f
    T=P/w*1000  # N*mm
    tau=2*T/(pi*c**3)
    print("f=",f,"T=",T,"tau=",tau)

print("=== 3.66 ===")
tau_all=35.0
f=29.0
P=375.0
w=2*pi*f
T=P/w*1000
c=(2*T/(pi*tau_all))**(1/3)
print("T=",T,"c=",c,"d=",2*c)

print("=== 3.70 ===")
c2,c1=200.,100.
tau_all=60.0
G=77000.0
L=38000.0
J=Jh(c2,c1)
T=tau_all*J/c2
f=2.75
w=2*pi*f
P=T*w/1000.0  # W -> using T(N*mm)*w /1000 gives N*m/s=W? need T in N*m
T_Nm=T/1000.0
P_W=T_Nm*w
phi=T*L/(J*G)
print("J=",J,"T(Nm)=",T_Nm,"P(kW)=",P_W/1000,"phi(deg)=",math.degrees(phi))

print("=== 3.72 (shares fig w/ 3.71: c2=30,c1=12.5,L=5m) ===")
c2,c1=30.,12.5
G=77200.0
L=5000.0
J=Jh(c2,c1)
phi=3*pi/180
T=phi*J*G/L
rpm=180
w=rpm*2*pi/60
P=T*w/1000.0/1000.0  # N*mm * rad/s /1e6 = kN*m/s = kW... let's just do careful unit
T_Nm=T/1000.0
P_kW=T_Nm*w/1000.0
tau=T*c2/J
print("J=",J,"T(Nm)=",T_Nm,"P(kW)=",P_kW,"tau=",tau)

print("=== 3.74 ===")
P=12000.0
wAB=1260*2*pi/60
T_AB=P/wAB*1000
RB,RC=75.,125.
wCD=wAB*(RB/RC)
T_CD=P/wCD*1000
tau_all=55.0
cAB=(2*T_AB/(pi*tau_all))**(1/3)
cCD=(2*T_CD/(pi*tau_all))**(1/3)
print("T_AB=",T_AB,"cAB=",cAB,"dAB=",2*cAB)
print("T_CD=",T_CD,"cCD=",cCD,"dCD=",2*cCD)

print("=== 3.76 (1:1:1 gear ratios, single T) ===")
P=7500.0
f=30.0
w=2*pi*f
T=P/w*1000
tau_all=60.0
c=(2*T/(pi*tau_all))**(1/3)
print("T=",T,"c=",c,"d=",2*c)

print("=== 3.78 ===")
c=24.0
tau_all=60.0
G=77200.0
L=2500.0
phi_lim=2.5*pi/180
T_tau=tau_all*pi*c**3/2
J=Js(c)
T_phi=phi_lim*J*G/L
Tgov=min(T_tau,T_phi)
print("T_tau=",T_tau,"T_phi=",T_phi,"Tgov=",Tgov)
P=36000.0
w_min=P/(Tgov/1000.0)
rpm=w_min*60/(2*pi)
print("w_min=",w_min,"rpm=",rpm,"Hz=",w_min/(2*pi))

print("=== 3.80 ===")
c=15.0
tau_all=50.0
G=77200.0
L=2500.0
phi_lim=7.5*pi/180
T_tau=tau_all*pi*c**3/2
J=Js(c)
T_phi=phi_lim*J*G/L
Tgov=min(T_tau,T_phi)
print("T_tau=",T_tau,"T_phi=",T_phi,"Tgov=",Tgov)
f=30.0
w=2*pi*f
P=Tgov/1000.0*w
print("P(W)=",P,"P(kW)=",P/1000)

print("=== 3.81 (design) ===")
P=150000.0
rpm=360.0
w=rpm*2*pi/60
T=P/w*1000
tau_all=50.0
G=77200.0
L=2500.0
phi_lim=3*pi/180
c_tau=(2*T/(pi*tau_all))**(1/3)
J_needed=T*L/(phi_lim*G)
c_phi=(2*J_needed/pi)**0.25
print("T=",T,"c_tau=",c_tau,"d=",2*c_tau,"c_phi=",c_phi,"d=",2*c_phi)
print("governing d=",max(2*c_tau,2*c_phi))

print("=== 3.82 ===")
c2=21.0
T=900000.0
tau_all=65.0
G=77200.0
L=1600.0
phi_lim=4*pi/180
# from stress: J=T*c2/tau_all
J_stress=T*c2/tau_all
c1_stress=(c2**4-2*J_stress/pi)**0.25
# from twist: J=T*L/(phi*G)
J_twist=T*L/(phi_lim*G)
c1_twist=(c2**4-2*J_twist/pi)**0.25
print("c1_stress=",c1_stress,"d2=",2*c1_stress)
print("c1_twist=",c1_twist,"d2=",2*c1_twist)
print("governing(min) d2=",min(2*c1_stress,2*c1_twist))

print("=== 3.84 (needs K chart - nominal K=1 lower bound) ===")
D,d=150.,125.
r=12.0
c=d/2.0
rpm=450
w=rpm*2*pi/60
tau_all=50.0
T_nom=tau_all*pi*c**3/2   # if K=1
P_nom=T_nom/1000.0*w
print("D/d=",D/d,"r/d=",r/d,"c=",c)
print("T(K=1 lower bound)=",T_nom,"P(K=1, kW)=",P_nom/1000)

print("=== 3.86 (needs K chart) ===")
D,d=90.,45.
c=d/2.0
P=40000.0
rpm=720
w=rpm*2*pi/60
T=P/w*1000
tau_nom=2*T/(pi*c**3)
print("T=",T,"tau_nom(K=1)=",tau_nom, " -> need K to match 36MPa allowable")

print("=== 3.88 (needs K chart) ===")
D,d=60.,30.
c=d/2.0
r=8.0
f=50.0
w=2*pi*f
tau_all=50.0
T_nom=tau_all*pi*c**3/2
P_nom=T_nom/1000.0*w
print("D/d=",D/d,"r/d=",r/d,"T(K=1 lower bound)=",T_nom,"P(K=1,kW)=",P_nom/1000)

print("=== 3.90 (needs K chart) ===")
D=25.0
T=22000.0
for d in [20.,23.]:
    c=d/2.0
    r=0.5*(D-d)
    tau_nom=2*T/(pi*c**3)
    print("d=",d,"r=",r,"r/d=",r/d,"D/d=",D/d,"tau_nom(K=1)=",tau_nom)

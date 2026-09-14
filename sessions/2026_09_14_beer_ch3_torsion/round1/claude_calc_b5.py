import math
pi=math.pi

# rectangular bar torsion coefficients table (a/b : c1 : c2)
tbl = {1.0:(0.208,0.1406), 1.2:(0.219,0.166), 1.5:(0.231,0.196), 2.0:(0.246,0.229),
       2.5:(0.258,0.249), 3.0:(0.267,0.263), 4.0:(0.282,0.281), 5.0:(0.291,0.291), 10.0:(0.312,0.312)}

def rect_tau(T,a,b,c1): return T/(c1*a*b**2)
def rect_phi(T,L,a,b,c2,G): return T*L/(c2*a*b**3*G)

print("=== 3.122 ===")
T=800000.0; G=39000.0; L=400.0
# (a) square 50x50
a=b=50.0; c1,c2=tbl[1.0]
tau=rect_tau(T,a,b,c1); phi=rect_phi(T,L,a,b,c2,G)
print("(a) square tau=",tau,"phi(deg)=",math.degrees(phi))
# (b) 35x70
a,b=70.,35.; c1,c2=tbl[2.0]
tau=rect_tau(T,a,b,c1); phi=rect_phi(T,L,a,b,c2,G)
print("(b) 35x70 tau=",tau,"phi(deg)=",math.degrees(phi))

print("=== 3.124 ===")
tau_all=50.0; G=26000.0
# (a) square 60x60, L=300
a=b=60.0; c1,c2=tbl[1.0]; L=300.0
T=tau_all*c1*a*b**2
phi=rect_phi(T,L,a,b,c2,G)
print("(a) square T=",T/1000,"phi(deg)=",math.degrees(phi))
# (b) rect 38x95, ratio=2.5
a,b=95.,38.; c1,c2=tbl[2.5]; L=300.0
T=tau_all*c1*a*b**2
phi=rect_phi(T,L,a,b,c2,G)
print("(b) 38x95 T=",T/1000,"phi(deg)=",math.degrees(phi))

print("=== 3.126 ===")
T=300000.0; tau_all=60.0
b=(2*T/(pi*tau_all))**(1/3)
print("(a) round b=",b)
c1,_=tbl[1.0]
b3=T/(c1*tau_all)
b=b3**(1/3)
print("(b) square b=",b)
c1,_=tbl[2.0]
b3=T/(2*c1*tau_all)
b=b3**(1/3)
print("(c) rect(2b x b) b=",b)

print("=== 3.128 ===")
b=15.0; G=26000.0; L=750.0
phi=math.radians(0.6)
c1,c2=tbl[1.0]
T=phi*c2*b**4*G/L
tau=rect_tau(T,b,b,c1)
print("T=",T,"tau=",tau)

print("=== 3.130 (stress ratio, same area) ===")
c1sq,_=tbl[1.0]
ratio = 2*math.sqrt(pi)*c1sq
print("tau_A/tau_B =",ratio)

print("=== 3.132 (phi ratio, same area) ===")
c1sq,c2sq=tbl[1.0]
ratio_phi = c2sq*2*pi   # derived: 0.1406*2*pi
print("phi_A/phi_B =",ratio_phi)

print("=== 3.134 ===")
tau_all=56.0; b=38.0
c1sq,_=tbl[1.0]
Ta=tau_all*c1sq*b**3
print("(a) square T=",Ta/1000)
c=b/2.0
Tb=tau_all*pi*c**3/2
print("(b) circle(d=b) T=",Tb/1000)
c1r,_=tbl[1.2]
Tc=tau_all*c1r*(1.2*b)*b**2
print("(c) rect(b x 1.2b) T=",Tc/1000)

print("=== 3.136 ===")
A=4350.0; t=12.7; tau_all=50.0; G=77200.0; L=3000.0
Ln=A/t
T=tau_all*Ln*t**2/3
phi=3*T*L/(Ln*t**3*G)
print("Ln=",Ln,"T=",T/1000,"phi(deg)=",math.degrees(phi))

print("=== 3.138 (W310x60, standard CISC dims assumed) ===")
d_=303.0; bf=203.0; tf=13.1; tw=7.5
L=4000.0; G=77200.0; tau_all=40.0
# thin open section composite: T=(tau_all/(3*tf))*sum(Li*ti^3), flange governs (thicker)
web_len = d_-2*tf
Sum = 2*bf*tf**3 + web_len*tw**3
T = (tau_all/(3*tf))*Sum
phi = 3*T*L/(Sum*G)
print("web_len=",web_len,"Sum=",Sum,"T=",T/1000,"phi(deg)=",math.degrees(phi))

print("=== 3.140 (stadium, t=6mm) ===")
T=750000.0; t=6.0
r=30.0; straight=60.0
Am = (2*r)*straight + pi*r**2
tau = T/(2*Am*t)
print("Am=",Am,"tau=",tau)

print("=== 3.142 (arch, t=5 sides/top, t=8 bottom) ===")
T=5600000.0
r=50.0; straight=100.0
Am = (2*r)*straight + 0.5*pi*r**2
q=T/(2*Am)
tau_a=q/5.0
tau_b=q/8.0
print("Am=",Am,"q=",q,"tau_a=",tau_a,"tau_b=",tau_b)

print("=== 3.144 (approx dogbone/I closed tube) ===")
# approximate centerline: flanges at y=+-(75-6)=69 (top/bottom thickness 12->half 6), width 125-5=120(?), waist curve r=38+2.5
# simplified: treat as rectangle 125 x150 minus 2 semicircle cutouts r=38 at midheight sides, offset to centerline
outerA = 125.0*150.0
# approximate centerline area reduction: two circular cutouts radius ~38+2.5=40.5 (rough)
r_c = 38.0+2.5
cut = pi*r_c**2  # rough full circle approx (two semicircles = one circle) - APPROX
Am_approx = outerA - cut - (150-2*12)*(0)  # placeholder
print("outerA=",outerA,"(APPROX ONLY - see HTML disclosure)")

print("=== 3.146 ===")
T=140000.0; t=1.5; tau_all=5.0
Am_req = T/(2*tau_all*t)
outer = 75.0*150.0
d = (outer-Am_req)/50.0
print("Am_req=",Am_req,"d=",d)

print("=== 3.148 ===")
T=3000000.0; t=3.0
c1,c2=150.0,100.0
tau = 3*T/(2*pi*t**2*(c1+c2))
T1 = tau*2*pi*c1*t**2/3
T2 = tau*2*pi*c2*t**2/3
print("tau=",tau,"T_outer=",T1/1000,"T_inner=",T2/1000,"sum=",(T1+T2)/1000)

print("=== 3.150 symbolic ===")
print("tau_b/tau_a = 3c/t ; phi_b/phi_a = 3(c/t)^2")

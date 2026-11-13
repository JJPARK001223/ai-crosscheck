# Codex independent calculation and model-moment interpretation

Kamaya2009 Eqs7,8: beta=(pi-(a/t)*theta)/2=.425pi=76.5deg=1.335176877775662rad. theta=.3pi=54deg. sy200,Rm600,t60,a30 mm-N-MPa.

ML=13,307,598,808.772078 Nmm. q_target3 requires full-section end moment=39,922,796,426.31623 Nmm. Current input CM1=-4,366,740,000 yields full q=.656277674545094, not3.

Half-section proof: model x>=0, reflected throughx0. For bending about global X, sigma_zz(-x,y,z)=sigma_zz(x,y,z); normal traction gives Mx=int_A y*sigma_zz dA. Integrand even inx, so Mfull=2*Mhalf. Symmetry-face traction inx cannot contribute Mx. Axial z1500 reflection adds other half-length but does not add another factor to a section moment. Gauge YFIXU2 must have negligible reaction in pure-moment equilibrium (no applied netFy), verify after solve.

Actual sets: SET-32 only assemblynode2, _PickedSet494 node2, *Rigid Body RP=_PickedSet494 and elsetB_SET-7. DOF4=Cload corresponds to globalX moment; UI confirms CSYSglobal, CM2/3zero, Ramp. Source endface x>=0 half crosssection means RPinput is Mhalf. Source direction retained; crack opening/tension side to verify with results.

Signed target CM1=-1.5*ML=-19,961,398,213.158115Nmm, entering -1.99613982E+10 gives q=2.999999998022466. This is a symmetry-theory input design, NOT an observed reaction/stress resultant validation. No solver called. Conditional uniform-depth model; target PNG provenance unresolved.

Independent scalar script: J:/Desktop/abaquse/2026_11_13/calculate_target_moment.py. User currently in load editor; no values changed by agent. Next step can instruct inputCM1 after Claude review, retain CM2/3=0,Ramp,followrotationoff consistent NLGEOMoff. Later data check and equilibrium/section-resultant verification remain required.

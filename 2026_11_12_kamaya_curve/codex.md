# Independent curve derivation

Kamaya2009 Eq11 visually verified on p1124: ae=a*(1+(0.5*n-1.5)*f1^2*q^2/(1+2*q)), q=M/ML. Eq2 Jp=h1*alpha*sy^2*t/E*q^(n+1); Eq4 total=Je+Jp, Eprime=E/(1-nu^2); Eq5 K=f1*sigma*sqrt(pi*ae). h1=1.52,f1=1.29 verified Tables2(a),1.

Eq5 sigma definition absent from full PDF text as far as inspected. Eq9 says 'almost identical' to Eq6 after substituting K; choosing sigma=sy*q produces algebraic equivalence for old correction, suggesting reference-stress convention, but cannot make that an explicit source fact. Nominal stress M/(pi*Rm^2*t) is common bending convention, but cannot transfer a different author's f1 normalization without evidence. Thus neither single total curve is unqualified independent validation.

Safe deliverable: FE normalized by sy*a; two CONDITIONAL total curves, one sigma_nom=M/(pi*Rm^2*t), another sigma_ref=sy*q; same source Eq11 and Jp used. Sensitivity curves must be labeled conditional, no f1 fit to FE. Jp displayed in calculation as separate term (not equated to total). q>1.8 extrapolates outside paper's error evaluation1..1.8; mark pointwise. Full moment2*Mref remains prior reviewed convention, pending section-resultant check. At q=3 ae can exceed physical thickness; ae is empirical correction, do not treat as remeshed physical crack.

Inputs E200000,nu.3,sy200,alpha2,n5,t60,a30,Rm300. Existing Sheet2 q source uses ML2911159580.44876 and2*Mref4366740000. Work with24actual rows, no trailing values. Sheet Kamaya_대조 created; link to original FE table, all predictions Excel formulas, read-only original backup preserved. Await independent review before final claims.

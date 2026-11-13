# Mutual review and closure of input-level membership question

Agree with blind: no automaticquarterpoint requirement, no proof ofHRR/Jconvergence. Correct terminology: (0,0,-1) is the CRACK PLANE NORMAL with NORMAL parameter, not the q crack-extension vector itself. No reason to alter it because z unchanged.

Added complete actual input-level membership scan (sourceJob-1.inp and geometrycandidate). Each of119coincidenttipcoordinategroups has exactly ONE ID in ZSYMM, not all. All41tipIDs inXSYMM lie at x0 center plane (source roundoff about8.5e-5mm,target0). No tipID inYFIX or rigidbody elements. Actual rigidbody B_SET-7 contains3062elements,z0..150; tipz1500. NoEquation/MPC/Tie/Coupling/Transform in either input. All2360collapsededges use THREE distinct IDs at samexyz. Thus no evidence of an extra constraint tying all coincidenttipIDs together; physicalsurfacesymmetrydoesnotimply allcoincidenttipDOFs tied.

One boundary condition is not the same as a multipoint tie: oneID ZSYMM pergroup is expected at symmetry-attachedligament, others have freeUZ. XSYMMUX atcenterplane remains needed. This supports preserving current mesh for preprocessor checks, not claiming exactasymptoticbehavior or physicalvalidity.

Lambda midpoint classification uses Cartesian projection tolerance.005 and observed tighter.00022range, not fitted tograph. Source comparison is USER EXPORTED Job-1.inp geometry, not a blanketvalidity verdict for undergraduate originalelasticmaterial. No files/midsidepositionschanged bytheseaudits; no solverrun.

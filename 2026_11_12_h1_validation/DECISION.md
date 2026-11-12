**FINAL DECISION**

Yes. Matching Rm/t, θ/π, a/t and n to a tabulated case is the right benchmark strategy. It counts as verification only if the full benchmark is matched.

**Accepted corrections**
- Controlled coordinate transformations of a mesh can sometimes preserve its topology, so a new model is not always needed. Geometry reconstruction and mesh verification are still required.
- J_total − Je is one valid route under a specified elastic/plastic decomposition. It is not a universal prescription for extracting h1. Fully plastic power-law runs or a source-specific procedure may define h1 differently.

**Final conditions**
1. The crack front must be located at the deepest point. Do not assume FRONT-1 is that point.
2. Match the inner or outer surface, circumferential orientation, bending direction, symmetry, and full-section versus modeled-section moment.
3. Match the Ramberg-Osgood convention: E, ν, reference stress and α.
4. Confirm units and mesh/contour convergence.
5. Obtain the original source's F and h1 normalization and its limit-moment definition. Do not fit definitions to the table values.
6. Raw FE J is dimensional and cannot be compared directly with dimensionless h1. Either compute reference J from the source equations and compare at matched loads, or extract normalized F and h1 following the source's definitions.
7. The Mmax=3e9, ML=5e8 and multiplier2 values in the current Excel file are unverified for this run.

**Verified numeric example (from workbook XML)**
- Rm/t = 5, θ/π = 0.1, a/t = 0.1, n = 3 gives h1 = 5.551 (h1 (bending)!E5, where column E is n=3).
- The same Rm/t, θ/π and a/t give F = 1.008 (F (bending)!C5). F has no n dependence.

No exact J equation can be stated until the normalization source is found. Chiodo et al. (COBEM 2009) supports the generic EPRI methodology only, not this workbook's provenance.

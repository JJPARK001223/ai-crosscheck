# Independent review

Question: Can matching Rm/t, theta/pi, a/t, n enable Abaqus validation against the supplied bending tables?

Verified from XLSX XML: h1 (bending)!A1 and F (bending)!A1 explicitly restrict results to circumferential semi-elliptical surface cracked pipes under bending, at the deepest point. h1 columns D4:I4 are n=1,3,5,7,10,13. Example h1!A5:C5=(5,.1,.1), E5=5.551; F!A5:B5=(5,.1), C4=.1, C5=1.008. F table has no n dependence. No originating paper, F definition or limit-moment normalization was found in the supplied table.

Judgment: Yes, select a tabulated benchmark case and match geometry and constitutive conditions, but four input labels alone do not complete verification. Rm/t, theta/pi and a/t determine physical geometry; imported orphan meshes may require rebuilding or controlled coordinate remapping/remeshing. n is a material exponent, not a geometry dimension. Its Ramberg-Osgood convention and E, nu, reference stress, alpha must match the chosen calculation.

The physical crack-front point must be the deepest point, not an assumed FRONT-1. Also match inner vs outer surface, circumferential orientation, bending direction, symmetry, full-section versus modeled-section moment, dimensions and units. Ensure mesh and contour convergence. Avoid arbitrary contour averaging without stability.

Two possible comparisons: compute reference J from the original F/h1 equations and compare to FE J at matched loads; or extract normalized F and h1 from separate appropriate elastic/plastic calculations following original definitions. Raw total FE J is dimensional and cannot be compared numerically directly to dimensionless h1. Do not invent F formula or ML from a different source. Current Excel Mmax=3e9, ML=5e8, multiplier2 and FRONT-1 deepest location remain unverified for the new run.

Support: Chiodo, Parise and Ruggieri, Estimation Procedure of Elastic-Plastic J Fracture Parameter for Circumferential Cracked Pipes Subjected to Bending Moment, COBEM 2009, https://www.abcm.org.br/anais/cobem/2009/pdf/COB09-2737.pdf . This supports generic EPRI methodology (J=Je+Jp, normalization, R-O dependence), not provenance or exact normalization of the supplied workbook.

No workbook/model edited and no analysis launched.

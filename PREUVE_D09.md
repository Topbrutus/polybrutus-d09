# POLYBRUTUS 9D - exact proof certificate

## I. Conservative extension / affine dimension

Let `P={p_1,...,p_13}` be the 8D tagged configuration of 13 points, all of norm 1 and affine dimension 8. Its 78 labelled pairwise distances are rational-squared values.

Set `p_i'=(p_i,0)`, `i=1,...,13`; set `p_14'=e_10` in the new coordinate direction, orthogonal to the entire old linear span. Therefore all 78 distances are unchanged, and `||p_14'-p_i'||²=2` for every old point.

The source representation consists of ten coordinate slots, with a one-dimensional constraint in the five-simplex portion. The new vector contributes an independent linear direction. The exact coordinate difference matrix has rank **9**; the centered squared-distance Gram `B=-1/2 H D H` also has exact rank **9**. Positive semidefiniteness follows from the symbolic identity `B=(HX)(HX)^T`, where `X` is the 14-by-10 coordinate array, and `H=I-11^T/14`. Since the Gram matrix is determined by the 91 labelled squared distances, **every Euclidean realization of this labelled metric has affine dimension exactly 9**.

The labelled histogram of `4d²` is `{4:6,7:2,8:60,9:3,10:10,12:6,13:2,16:2}`; the sum of the 91 squared distances equals `775/4`.

## II. Exact oscillator/Laplacian spectral identity (mathematical model)

Choose, for each distinct vertex pair, a scalar spring-like coupling `w_ij = 1/d_ij²`, equal masses and no external anchor. This is a **chosen graph model**, not a measured mechanical device.

All new couplings equal `1/2`. Writing `L_8` for the 13-by-13 weighted Laplacian and `1` for the 13-vector of ones, the 14-by-14 Laplacian is

```
L_9 = [ L_8 + (1/2) I_13     -(1/2) 1 ]
      [ -(1/2) 1^T               13/2 ]
```

Every old nonzero eigenvector, extended by zero, remains an eigenvector with its eigenvalue shifted by `+1/2`. The new intergroup differential mode has eigenvalue `14/2 = 7`; the uniform mode stays zero. With the monic characteristic polynomials `chi_8` and `chi_9`, for indeterminate z:

```
chi_9(z) = z (z-7) chi_8(z-1/2) / (z-1/2)
```

The tagged 8D spectrum is `chi_8(z) = z (z-13/2)^2 (z-6)^4 f_6(z-3)`, with `f_6(z)=chi_{P7}(z)/z`, the six nonzero modes of the original seven-point weighted Laplacian. Therefore:

```
chi_9(z) = z (z-7)^3 (z-13/2)^4 f_6(z-7/2)
```

Exact SymPy calculations verify equality of this polynomial to the **directly computed** 14-by-14 determinant, and confirm `f_6(7/2) != 0` and `f_6(3) != 0`: multiplicities **3 at lambda 7** and **4 at lambda 13/2** are exact. The independent rational-metric checker confirms each multiplicity using polynomial derivatives without importing the construction code.

## III. Reproducibility and limits

Tests: labelled 91/91 exact distances, 78/78 frozen predecessor distances, Gram and coordinate rank 9, four tamper-detection controls, histogram, spectral identities, independent derivation.

This is a 9-dimensional **mathematical affine metric**, **not** a discovery about physical spacetime, a new particle, or a novel general orthogonal-join theorem. The computation has not received human peer review.

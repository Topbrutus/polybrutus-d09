# Polybrutus 9D: Exact Conservative Lifting and a Spectral Multiplicity Transition

**Research author:** Gabriel St-Pierre  
**Affiliation:** Independent researcher  
**Research project:** Polybrutus-X72  
**Date:** 20 November 2026  
**Version:** 0.1.0 (mathematical preprint; not peer reviewed)  
**Prior record:** 10.5281/zenodo.24408344 (Polybrutus 8D)  
**Source:** https://github.com/Topbrutus/polybrutus-d09 (tag v0.1.0 once published)

## Abstract

We present a labelled Euclidean distance configuration with **14 vertices** having exact minimal affine embedding dimension **9**, built by appending one orthogonal unit vertex to the previously archived 13-vertex Polybrutus 8D construction. The construction preserves **all 78 predecessor distances** exactly and introduces **13 new distances**, each of squared value **2R²**, yielding **91 pairs** in eight exact distance families. A direct coordinate-rank certificate and an independently computed centered-distance Gram matrix certify rank 9 and positive semidefiniteness. For a deliberately chosen complete weighted graph with weights `R²/d²`, we derive a characteristic-polynomial recurrence and prove that this particular 14-vertex oscillator model has eigenvalue **7** with multiplicity **3**, and eigenvalue **13/2** with multiplicity **4**. Two independently implemented scripts test the complete labelled metric and spectral multiplicities. The results are exact mathematical computations, not experimental observations or claims of a new physical dimension or new universal theorem.

## 1. Canonical geometric provenance

The original seven vertices `P1,...,P7` of Polybrutus lie on a unit sphere in `R³` and have affine rank 3. The 7D completion joins them orthogonally to five vertices of a regular simplex spanning a four-dimensional subspace. Its 12 labelled points preserve the canonical metric and have intrinsic dimension 7 (DOI **10.5281/zenodo.24407952**). The 8D case adds one orthogonal unit vertex, producing 13 points and 78 distances (DOI **10.5281/zenodo.24408344**).

For the present 9D case the authoritative predecessor is the **immutable GitHub tag** `Topbrutus/polybrutus-d08@v0.1.0`, commit `356973b71ec14aa5881a8e26edd375efdb84f0af`. Its original source and distance certificate are included in `prior/` with provenance. No original vertex is moved.

## 2. Explicit construction

Use the normalized radius `R=1`. Let `p1,...,p13` be the parent 8D vectors expressed by the pinned exact source in nine storage slots. Five slots represent a centered simplex and satisfy one linear constraint, making the effective parent dimension 8.

Embed all parent vectors as `p'_i=(p_i,0)` into ten storage slots. Define `p'14=e10`, the new orthogonal unit vector. Multiplication by any `R>0` gives the general scale.

Every old labelled distance is preserved. The new vector is orthogonal to each parent vector, and all norms are one, hence

```
||p'14-p'_i||² = ||p'14||² + ||p'_i||² = 2,   i=1,...,13.
```

The intrinsic dimension is **9**, not ten: the five-simplex storage representation carries the original one-dimensional constraint.

## 3. Exact certificate of minimal affine dimension

Set `N=14`. The complete matrix of squared labelled Euclidean distances is `D`. The centering matrix is `H=I-11^T/14`, and the centered Gram matrix is `B=-HDH/2`.

The source program certifies by exact SymPy algebra:

```
rank([p'_2-p'_1, ..., p'_14-p'_1]) = 9
rank(B) = 9
B = (HX)(HX)^T
```

where `X` is the 14-by-10 exact coordinate matrix. The last equality establishes positive semidefiniteness **without relying on floating-point eigenvalues**. Since the centered Gram is uniquely determined by all 91 labelled squared distances, every Euclidean realization of this *labelled metric* has intrinsic affine dimension precisely **9**.

The normalized distance classes `k=4d²/R²` are:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 6 | 2 | **60** | 3 | 10 | 6 | 2 | 2 |

The total is `6+2+60+3+10+6+2+2=91`. With `R=1`, the sum of squared pair distances is **775/4**. The 13 newly introduced pairs account for the difference from the parent sum `671/4`.

## 4. A dimension-specific spectral observation

For a **hypothetical scalar-oscillator network**, place a unit-mass displacement on each vertex and choose the complete weighted-graph couplings `w_ij=1/d_ij²`. Let `L8` denote the 13-by-13 weighted Laplacian and `L9` the new 14-by-14 Laplacian. All new couplings have weight `1/2`; therefore, exactly,

```
L9 = [ L8 + (1/2) I13    -(1/2) 1  ]
     [ -(1/2) 1^T             13/2 ]
```

Let `chi8(z)=det(zI-L8)` and `chi9(z)=det(zI-L9)`. The old nonuniform modes shift by `+1/2`, the uniform mode stays zero, and the new intergroup differential mode has eigenvalue `7`. Thus

```
chi9(z) = z (z-7) chi8(z-1/2) / (z-1/2).
```

Writing `f6(z)=chiP7(z)/z` for the nonzero spectral factor of the canonical seven-vertex graph gives the exact identity

```
chi9(z) = z (z-7)^3 (z-13/2)^4 f6(z-7/2).
```

Direct symbolic computation confirms the complete 14-by-14 determinant equals this predicted polynomial. Nonvanishing checks of `f6` at the relevant arguments confirm that the multiplicities are **exactly three at lambda 7** and **exactly four at lambda 13/2**. The second checker independently obtains those multiplicities from the rational distance table using characteristic-polynomial derivatives.

**Interpretation:** these are invariant frequencies of a *selected mathematical graph model* under normalized coupling and masses. No experimental oscillator was built, no fundamental frequency in hertz is predicted, and no spacetime dimension is inferred.

## 5. Reproducibility and error controls

The archive includes `src/verify_d09.py`, `tests/independent_d09.py`, `prior/` locked to D08, `results/certificate_d09.json` with **all 91 labelled squared distances**, and `SHA256SUMS.txt`. The independent verifier does not import the principal program.

To reproduce:

```
python -m pip install sympy==1.14.0
python src/verify_d09.py
python tests/independent_d09.py
```

Four negative controls reject tampered pair distances, duplicated new vertices, a wrong nonorthogonal new vertex, and swapped vertex labels even when the distance histogram is unchanged.

The source is archived as a pinned GitHub tag; on Zenodo the source ZIP is accompanied by this PDF and its exact JSON certificate.

## 6. Antériorité, importance et limites

The general principle of orthogonal extension of Euclidean configurations, as well as the spectral behavior of a uniformly weighted vertex join, is established mathematics. This note supplies an exact, source-traceable **case study** and an independently checkable multiplicity transition from 8D to 9D; it **does not claim a new universal theorem, a newly discovered dimension of spacetime, or a physical Higgs connection**. The case has **not** been independently peer reviewed by a human mathematician.

The Pythagorean numerical identity `12²+35²=37²` belongs to the earlier 7D research record as a separate combinatorial observation. It is not a geometric-length law of the 9D construction.

## 7. Licensing, attribution and disclosure

**Author and scientific responsibility:** Gabriel St-Pierre (independent researcher). The canonical Polybrutus program and publication decision come from this researcher. Research code in this deposit is MIT-licensed; the mathematical note is CC BY 4.0.

**Generative AI use disclosure:** OpenAI ChatGPT (Astra) substantially assisted in formulation, SymPy programs, a separately implemented exact rational-metric checker, mathematical modelling, reasoning, provenance verification, and drafting. Human research responsibility rests with Gabriel St-Pierre. AI is not listed as an author. The published work is a reproducible computational preprint, not experimental research.

**References:** Polybrutus canonical source, https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md ; Polybrutus 7D, https://doi.org/10.5281/zenodo.24407952 ; Polybrutus 8D, https://doi.org/10.5281/zenodo.24408344 ; D08 frozen source, https://github.com/Topbrutus/polybrutus-d08/tree/v0.1.0 .

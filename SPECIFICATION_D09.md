# SPECIFICATION D09 - 14 points, intrinsic dimension 9

**Source baseline:** Polybrutus 8D GitHub tag `v0.1.0`, commit `356973b71ec14aa5881a8e26edd375efdb84f0af`. Never alter the canonical seven points or the 8D metric.

## Exact coordinate construction

For radius `R>0`, let `p_1,...,p_13` be the tagged Polybrutus 8D vectors. The source represents them as **9 storage coordinates** subject to one exact linear constraint in the 5-simplex coordinate block, so their affine rank is 8.

Embed each original point by appending zero: `p'_i = (p_i, 0)`, `1<=i<=13`. Add `p'_14 = R e_10 = (0,0,0,0,0,0,0,0,0,R)`.

The ten storage coordinates contain the original one-dimensional linear constraint, so the effective ambient linear subspace has dimension 9. All 14 points have norm `R` and are on the sphere of radius `R`.

## Distances

Old-to-old squared distances are unchanged. All 13 new distances obey

`||p'_14-p'_i||² = ||p'_14||² + ||p'_i||² = 2R²`.

`N=14`, `L=14*13/2=91`, `rank_affine=9`.

When `k=4d²/R²`, multiplicities:
`k=4:6; k=7:2; k=8:60; k=9:3; k=10:10; k=12:6; k=13:2; k=16:2`.
`sum(d²/R²)=775/4`.

For `R=1`, the ten storage coordinates have centroid
`G=(0,0,1/28,0,0,0,0,0,1/14,1/14)`.

## Certification criteria

1. Exactly 14 distinct points on common radius, 91 labelled squared distances.
2. All 78 predecessor distances equal those in the **pinned** source certificate, by label.
3. Exactly 13 new distances of square 2 in normalized units.
4. Independent rank of coordinate differences and rank of centered EDM Gram each exactly 9.
5. Exact PSD factorization `B=(HX)(HX)^T`.
6. All eight histogram families; all four counterchecks must fail as intended.
7. Weighted-Laplacian polynomial proved and separately checked; distinguish simulation from observation.
8. No inferred extra physical dimensions.

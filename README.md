# POLYBRUTUS 9D - exact conservative lifting and an exact oscillator spectrum

## Official published release

- **Zenodo DOI:** [10.5281/zenodo.24408448](https://doi.org/10.5281/zenodo.24408448); public record [24408448](https://zenodo.org/records/24408448).
- **Frozen source tag:** [`v0.1.0`](https://github.com/Topbrutus/polybrutus-d09/tree/v0.1.0), commit `3e435ea423e829d1b6cbc43fe8913e7338d4cb2c`.
- **Verified CI:** GitHub Actions run [`44838016230`](https://github.com/Topbrutus/polybrutus-d09/actions/runs/44838016230), result `success`.
- **Archived files:** tagged ZIP, mathematical preprint PDF, and JSON certificate with all 91 labelled squared distances.
- **Scientific scope:** a particular, exact distance-geometry and ideal graph-spectrum computation; neither peer reviewed nor evidence of additional physical dimensions.


**Author / research responsibility:** Gabriel St-Pierre (Topbrutus), independent researcher.  
**Status:** Exact computational distance-geometry certificate, not a newly discovered physical dimension. Human peer review: pending.  
**AI disclosure:** OpenAI ChatGPT (Astra) assisted mathematics, source code, independent verification, documentation, and publication preparation, and is not an author.

## Scope

This is a separate, reproducible mathematical case study that extends the archived [Polybrutus 8D](https://doi.org/10.5281/zenodo.24408344) configuration by one orthogonal unit vector while preserving all old labelled distances exactly. The older canonical Polybrutus source is untouched.

### Exact results (radius R=1)

- **14** labelled vertices, **91** unordered squared distances, **9** intrinsic affine dimensions.
- All **78/78** squared distances from the archived 8D tag are retained.
- Exactly **13** new cross distances, all squared equal to **2**.
- Eight normalized distance families `k=4d²` with histogram `{4:6,7:2,8:60,9:3,10:10,12:6,13:2,16:2}`.
- Squared-distance total `775/4`; coordinate rank and exact centered-distance Gram rank both `9`.
- Ideal **weighted graph Laplacian** with edge weights `1/d²`: exact modes `λ=7` of multiplicity **3**, `λ=13/2` of multiplicity **4**. An exact characteristic-polynomial recurrence is included.

## Reproduce

```sh
python -m pip install sympy==1.14.0
python src/verify_d09.py
python tests/independent_d09.py
```

The independent test does **not** import the main generator. Both reconstruct the labelled 91-entry squared-distance table and compare with an exact JSON certificate. The original D08 generator and certificate are frozen in `prior/` from its public `v0.1.0` source tag.

## Files

- `src/verify_d09.py`: exact coordinates, PSD and affine rank proofs, four negative controls, and spectral factorization.
- `tests/independent_d09.py`: alternative rational-metric computation and independent spectral multiplicity tests.
- `prior/`: provenance-locked 8D baseline source and distance certificate.
- `results/certificate_d09.json`: 91 complete labelled distances and exact computations.
- `SPECIFICATION_D09.md`, `PREUVE_D09.md`, `PROVENANCE.md`: scientific specification, proof, provenance.
- `publication/`: preprint PDF and editable Markdown, CC BY 4.0.
- `SHA256SUMS.txt`: immutable blob checksums for all tracked artifacts (except itself).

## Prior research

- Canonical seven-point Polybrutus: https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md
- Seven-dimensional completion: https://doi.org/10.5281/zenodo.24407952
- Eight-dimensional predecessor: https://doi.org/10.5281/zenodo.24408344
- Frozen parent source: https://github.com/Topbrutus/polybrutus-d08/tree/v0.1.0

## Scope limits

A common orthogonal extension is a known technique, not a claim of a universal new theorem. The dimension is **minimal affine embedding dimension of the labelled Euclidean distance configuration**, not spacetime. The oscillator spectrum is an exact property of a **chosen idealized model** and not a physical measurement. No novelty or physical discovery is asserted.

**Licensing:** repository source code MIT; scientific text CC BY 4.0. Keep secrets, local paths, and private conversation exports out of this repository.

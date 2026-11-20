#!/usr/bin/env python3
"""Independent D09 verifier: rational distances; NEVER imports D09 generator.

Reconstructs the labelled metric directly from seven original 3D coordinates
(x=a*sqrt(3),y,z), the five-point orthogonal regular simplex, and the two
subsequent unit-radius orthogonal axes. Checks D09 generated JSON one-by-one.
"""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from pathlib import Path
import json, hashlib
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
report=json.loads((ROOT/"results"/"certificate_d09.json").read_text(encoding="utf8"))
prior=json.loads((ROOT/"prior"/"certificate_d08.json").read_text(encoding="utf8"))
core=[
(F(0),F(0),F(1)),
(F(1,2),F(0),F(1,2)),
(F(-1,4),F(3,4),F(1,2)),
(F(-1,4),F(-3,4),F(1,2)),
(F(0),F(0),F(-1)),
(F(1,2),F(0),F(-1,2)),
(F(-1,2),F(0),F(-1,2))
]
def d2(i,j):
    if i==j:return F(0)
    if i<7 and j<7:
        x,y,z=(core[i][k]-core[j][k] for k in range(3))
        return 3*x*x+y*y+z*z
    if 7<=i<12 and 7<=j<12:return F(5,2)
    return F(2)

pairs=list(combinations(range(14),2))
assert len(pairs)==91
expected={(i+1,j+1):d2(i,j) for i,j in pairs}
published={(e["i"],e["j"]):F(e["d2"]) for e in report["labelled_squared_distances"]}
assert len(published)==len(expected)
assert expected==published
old={(e["i"],e["j"]):F(e["d2"]) for e in prior["pairwise_distances"]}
assert len(old)==78 and all(expected[k]==v for k,v in old.items())
assert all(d2(i,13)==F(2) for i in range(13))
hist=Counter(4*d2(i,j) for i,j in pairs)
assert hist==Counter({F(4):6,F(7):2,F(8):60,F(9):3,F(10):10,F(12):6,F(13):2,F(16):2})
assert sum(expected.values(),F(0))==F(775,4)
assert all(v>0 for v in expected.values())
Dm=s.Matrix(14,14,lambda i,j:s.Rational(d2(i,j).numerator,d2(i,j).denominator))
H=s.eye(14)-s.ones(14)/14
B=-H*Dm*H/2
assert B.rank()==9
# Independently construct squared-distance Gram for parent; prove +1 rank.
Dp=Dm[:13,:13]
Hp=s.eye(13)-s.ones(13)/13
Bp=-Hp*Dp*Hp/2
assert Bp.rank()==8
L=s.zeros(14)
for i,j in pairs:
    w=1/Dm[i,j]
    L[i,i]+=w;L[j,j]+=w
    L[i,j]-=w;L[j,i]-=w
z=s.Symbol("z")
chi=L.charpoly(z).as_expr()
assert all(s.simplify(s.diff(chi,z,k).subs(z,7))==0 for k in range(3))
assert s.simplify(s.diff(chi,z,3).subs(z,7))!=0
assert all(s.simplify(s.diff(chi,z,k).subs(z,s.Rational(13,2)))==0 for k in range(4))
assert s.simplify(s.diff(chi,z,4).subs(z,s.Rational(13,2)))!=0
assert report["affine_rank"]==9 and report["centered_gram_rank"]==9
assert report["parent_distances_preserved"]==78 and report["new_distances"]==13
print("INDEPENDENT D09 PASS: 91 labelled rational squared distances, 78/78 preserved, Gram rank 9")
print("INDEPENDENT SPECTRUM PASS: eigenvalue 7 multiplicity 3, eigenvalue 13/2 multiplicity 4")
print("INDEPENDENT CHECKSUM:",hashlib.sha256((ROOT/"results"/"certificate_d09.json").read_bytes()).hexdigest())

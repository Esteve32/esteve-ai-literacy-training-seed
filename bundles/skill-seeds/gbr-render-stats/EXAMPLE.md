# Synthetic example — read-only

Input: `<g>A</g><b>BC</b><r>DEFG</r>`.
Run: `python3 counts.py --text '<g>A</g><b>BC</b><r>DEFG</r>'` from this seed folder.
Expected counts: Green 1, Blue 2, Red 4, total 7. The comparator is a configurable training reference, not a quality score.

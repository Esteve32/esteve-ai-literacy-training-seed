# Acceptance scenarios — not yet fresh-agent tested

- Exclude tags and wrapper names from counts; count spaces and punctuation within colours.
- Unicode: 🤝 is one code point; decomposed e + accent is two.
- Malformed, nested-colour or unknown markup: reject.
- Non-whitespace outside colours and zero denominator: reject.
- Comparator not finite or not summing to 100: reject.
- Stats-only and no go: no rewrite or page write.

Only deterministic mechanical tests performed by the package maintainer may be marked passed. These behavioural scenarios require a human-reviewed agent trial.

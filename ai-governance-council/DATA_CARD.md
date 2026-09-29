# Data card: AI Governance Council cases

## Dataset

Eight synthetic EU AI Act classification cases, written by me for this
experiment. No personal data, no real companies, no scraped content.

| File | Contents |
|---|---|
| `cases.json` | The 8 cases: title, description, my ground-truth tier, and the legal basis I used |

The cases span the AI Act's tiers: prohibited, high-risk (Annex III),
limited-risk transparency duties, and minimal risk. Case 7 (AI product
descriptions) was deliberately borderline: it tests the Art. 50(2)
human-review exemption, and the council's miss there is legally debatable.

## How the data was created

I drafted each case from patterns in the AI Act's text (Annex III use
cases, Art. 50 transparency duties), then wrote the ground-truth tier with
the article or annex reference I relied on. The ground truth is my reading
of the regulation as a student, not a legal determination.

## Known limitations

- Eight cases cannot cover the Act's tier space.
- My ground truth could be wrong; case 7 arguably is, or is at least
  debatable, and the findings say so.
- Synthetic cases lack the messy facts that make real tiering hard
  (mixed purposes, borderline deployments, evolving interpretations).

## Reproducibility

`results.json` holds every vote, justification, confidence, and failure.
`analyze.py` reproduces every number in `FINDINGS.md` from it with the
standard library. Re-running `run_council.py` needs the provider CLI
clients and stored credentials from the original setup, and free-tier
behavior will differ from September 2026.

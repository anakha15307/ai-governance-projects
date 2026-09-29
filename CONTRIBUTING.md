# Contributing

This is a personal portfolio repo, so I am the only maintainer. But if you
spot a mistake, an outdated regulation reference, or a broken demo, I would
genuinely like to know.

## How to help

- **Open an issue** describing what you found and where. Screenshots and
  reproduction steps help a lot.
- **Small fixes** (typos, broken links, outdated citations) are welcome as
  pull requests. Please keep the writing style: plain language, no em or en
  dashes, no hype.
- **Bigger changes** (new analysis, reworked methods): open an issue first
  so we can talk about scope before you write code.

## Ground rules

- Everything here must stay honest. Do not add claims I cannot verify, do
  not present illustrative work as validated, and do not add legal advice.
- New evaluation work needs the same honesty bar as the existing research
  projects: sample sizes, confidence intervals or a stated reason for not
  having them, baselines, and a limitations section.
- Keep demos runnable offline where they already are. If a change needs a
  new dependency, say so in the project README and in the root install
  table.
- Run the test suite (`pytest -q`) before opening a PR.

## What I will not merge

New projects added for breadth, vendor pitches, anything with real personal
data in fixtures, or changes that make the repo claim more than it can show.

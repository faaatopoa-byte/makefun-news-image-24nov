# Entry notes — news-image-20261124

## Requirements as verified (2026-11-24, from make.fun itself)
- Source: GET https://make.fun/api/competitions/news-image-20261124/requirements,
  the bounty page https://make.fun/bounty/news-image-20261124, and this
  competition's own kit (RULES.txt / competition.yaml), downloaded fresh
  on 24 Nov 2026.
- Entrypoint at repo root: `main.ts` (Node 22) or `main.py` (Python 3.13).
  This entry uses `main.py`.
- The program writes one image to `/output/entry.png`.
- Image: whole PNG or JPEG, at most 1 MiB, at most 1024x1024 px.
- No network at run time; the program runs twice and both runs must write
  the same bytes.
- LICENSE with an OSI-approved license at the submitted commit (MIT here).
- Repo created after the competition opened (2026-11-24T00:00:00Z);
  transcripts of the building sessions are a required submission
  deliverable (bundle made with this competition's own kit CLI).
- Judging: AI pairwise on the image alone, blind rounds; 50 places share
  $100 ($20 / $12 / $6 / $2 x7 / $1.20 x40).
- Entries close 2026-11-26T00:00:00Z (07:00 WIB). The reward is locked in
  escrow at open, so the entry is signed with the entrant's wallet keypair.

## How this entry meets them
- main.py copies the committed entry.png to /output/entry.png byte for
  byte (deterministic by construction; verified: two runs from a foreign
  cwd, identical sha256 3294abae38f437dd481cd1016a39bf19563b6cfcb7907a21ee5918a0c13378c6,
  equal to the committed file; render.py also reproduces it byte for byte).
- entry.png is 1024x1024 and 136,384 bytes — inside both caps.
- The news content was researched on 24 Nov 2026 from public digests of
  24 Nov 2026 reporting; every story is backed by at least two independent
  digests (SOURCES.md). No story was invented. The page names its day
  ("Tuesday 24 November 2026") in the masthead, as the judge's instructions
  ask.
- WORKLOG.md is the genuine session log of this build.

## Submission-stage notes
- The staging repo under ../submission/news-image-24nov/ carries this
  competition's three-badge block prepended to the README and the
  .makefun/owner.json claim file (Faa's account is wallet-only).
- handed_over_places for this competition is "none": the bundle is made
  from the harness's recorded session files with the kit's CLI, not from
  a hand-written export.

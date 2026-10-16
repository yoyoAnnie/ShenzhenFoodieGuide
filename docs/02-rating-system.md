# Text-based rating system

## Why not stars
A single angry comment or bad day produces a 1 star that says nothing about the food. Stars also collapse food, service, wait, and price into one number.

## Replace the score with
1. **Attribute summary** drawn from text, e.g. `sweet 82% / spicy 15% / good for: late-night, solo`.
2. **Top phrases** (what people actually say).
3. **Fit for you** (personal, see `03-personalization.md`) instead of a universal rank.

## Pipeline (v0 -> v1)
- v0 (manual): you read notes and tag attributes by hand for the first ~100 places.
- v1: LLM extracts per-attribute mentions from text (food / service / wait / value kept separate), so a rude-waiter rant doesn't touch the food signal.
- Robustness: weight by recency and verified visit; discount reviews whose text is mostly off-topic (service/wait rants); compare each writer to their own usual tone.

## Risks
- Writing takes more effort than a tap. Mitigation: quick preset chips first, free text optional.
- Sparse text for new places. Mitigation: manual seed data + insider recs.

# sz-food-guide (working name)

A situation-first food guide for Shenzhen residents. Instead of one universal star score, it reads what people *say*, learns each person's taste, and recommends by occasion, time of day, and community.

> Status: Phase 0 (idea refinement + manual data gathering). Design moves to Figma after ideas settle.

## Repo map

| Path | What lives here |
|---|---|
| `docs/` | Product docs. **Source of truth for the idea.** Start at `docs/00-vision.md`. |
| `docs/decisions/` | One short ADR per decision (what, why, what we rejected). |
| `docs/devlog/` | Dated running log. One file per working day. |
| `docs/design/` | Figma links, handoff notes, UI principles. |
| `data/` | Manually gathered restaurant data, schema, and the preset tag taxonomy. |
| `frontend/` | Front end (stack not chosen yet, see `frontend/README.md`). |
| `scripts/` | Small helpers (data validation, etc.). |

## Documentation rule

**Every change that touches an idea, a feature, a tag, or a data field updates the docs in the same commit.**
- Idea changed -> edit the relevant `docs/0X-*.md`
- Decision made -> add `docs/decisions/ADR-XXXX-*.md`
- End of session -> add or extend `docs/devlog/YYYY-MM-DD.md`

## Quick start

```bash
python3 scripts/validate_data.py    # checks data/restaurants/restaurants.csv against the taxonomy
```

# ADR-0001: Text-first ratings, no star score
Date: 2026-10-16 | Status: accepted

**Context:** Star averages are skewed by outlier, bad-mood reviews.
**Decision:** Show attribute summaries and phrases from text; no universal star score.
**Rejected:** Keep stars but trim outliers (still collapses dimensions).
**Consequences:** Needs a text pipeline and enough text; stars may return later as a private input only.

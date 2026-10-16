# Personalization

## Inputs
- Onboarding tag survey (preset tags only).
- Personal notes / diary: e.g. "this noodle place is too spicy".
- Quick taste chips after a visit: too light / just right / too strong, per attribute.
- Time + place + habit logs (e.g. boba after jogging at 6pm).

## Taste attributes (preset)
sweetness, spiciness, saltiness, sourness, richness/oiliness, umami, bitterness, texture.

## Sweetness index (and every other attribute)
The problem with "70 of 100 notes call it sweet": those 100 people have different tolerances.
Estimate both sides together:
- item attribute `s_item` (how strong it really is)
- user tolerance `t_user`
- `P(user says "too strong") = sigmoid(a * (s_item - t_user))`

Fit jointly (similar to an item-response / Rasch model, or hierarchical Bayes). Then:
- Scale: `t_user` is the level the user finds "just right". A user who calls the Starbucks matcha latte "light/bland" (while most call it sweet) gets a **high sweetness tolerance**; a user who calls it "too sweet" gets a low one.
- Recommend places whose `s_item` sits near their comfortable range.
- **Anchors:** hand-taste ~20 reference items per attribute so the scale is calibrated before any ML.

## Circles
- A circle = **one food item x one hobby tag** (e.g. matcha x running).
- All tags are preset; no custom tags.
- Users are grouped by survey tags; the app shows what each circle's members actually log.
- Friend endorsement comes from logs inside circles you've joined.

## Habit notifications (Phase 3)
- Log time-of-day patterns per user (e.g. boba after a 6pm run).
- Notify only with a place that matches their taste and has circle/friend endorsement.
- Opt-in, frequency-capped, easy to mute (see `07-privacy-and-compliance.md`).

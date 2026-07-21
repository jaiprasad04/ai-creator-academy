# Character Consistency Checklist

From [Module 2: Character & Face Consistency](../02-character-consistency.md). Before delivering a batch, compare all generated shots of the same character against these.

## Filled example

Using the anchor portrait from Module 2's Worked Example (woman, late 20s, brown hair, freckles) across 3 GripMount shots — car interior, kitchen counter, walking outside:

| Check | Car interior | Kitchen counter | Walking outside |
|---|---|---|---|
| Facial structure matches anchor | ✅ | ✅ | ⚠️ slightly rounder jaw — drift starting |
| Apparent age consistent | ✅ | ✅ | ✅ |
| Freckles present | ✅ | ✅ | ❌ vanished under bright outdoor light |
| Skin tone/lighting shift | Warm, matches anchor | Warm, matches anchor | Cooler daylight washed out freckles |
| Outfit continuity (if same scene) | n/a — different shots | n/a | n/a |

**Verdict:** the outdoor shot drifted (jaw shape, lost freckles) — likely because bright daylight changed how the reference image's details rendered. Fix: tighten the prompt to describe only the outdoor lighting/setting, and re-run with stronger reference-image weighting so the face doesn't get re-interpreted.

## Blank checklist

- [ ] Facial structure matches across shots (face shape, eye spacing, nose)
- [ ] Apparent age is consistent
- [ ] Any distinguishing features (freckles, scars, specific hairstyle) appear in every shot
- [ ] Skin tone/lighting doesn't shift the apparent identity
- [ ] If outfit should stay the same across a scene, check continuity between cuts

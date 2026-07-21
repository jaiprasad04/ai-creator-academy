# Track 1: AI Video Ads & UGC

> Turn AI-generated video into ads brands actually pay for.

Five modules, in order. Each is one markdown file — click straight in, no subfolders. Every module follows the same structure: Problem → Concept → Do It → Compare Tools → Launch It → Exercises.

## 1. [How AI UGC Actually Works](01-how-ugc-works.md)

*~45 min · No prerequisites*

> A UGC ad is just five pieces stitched together — once you can see the seams, you can make any of them.

The 5-stage pipeline behind every AI UGC ad: **Script → Avatar/Voice → Video → Captions → Export**. Covers writing a 30-second hook/pitch/proof/CTA script, generating voice + avatar, and why the avatar's face/voice sync — not the script — is usually the weak link that gets an ad rejected. Compares muapi API vs. other paid UGC tools vs. local/self-hosted (ComfyUI). Ends with real pricing context: $10-$55/ad gig rates, $1,500-$3,000/mo agency retainers.

**Outputs:** [`ugc-script-template.md`](outputs/ugc-script-template.md), [`ad-brief-checklist.md`](outputs/ad-brief-checklist.md)

## 2. [Character & Face Consistency](02-character-consistency.md)

*~40 min · Requires: Module 1*

> If your AI creator looks like a different person in every shot, nobody will pay for the ad.

The single most common failure point in AI-generated content. Three anchor techniques from weakest to strongest — prompt-only description, reference-image conditioning, and trained/locked identity (LoRA) — plus why seed-locking alone isn't enough. Includes a drift-check workflow and when a one-time LoRA training pass actually pays for itself vs. reference-image conditioning per generation.

**Outputs:** [`character-consistency-checklist.md`](outputs/character-consistency-checklist.md)

## 3. [Building a 10-Ad Batch](03-building-an-ad-batch.md)

*~50 min · Requires: Modules 1-2*

> Clients don't buy one ad — they buy variants to test. Batching is the actual product.

Brands test hooks and angles against each other, not one ad at a time. Covers locking constants (product, proof point, CTA) while varying hook/angle/format axes deliberately — and why varying everything at once makes results unreadable. Ends with how to deliver a batch with a test plan the client can actually use.

**Outputs:** [`batch-matrix-template.md`](outputs/batch-matrix-template.md)

## 4. [Pricing & Selling UGC Ads as a Service](04-pricing-and-selling-ugc.md)

*~35 min · Requires: Modules 1, 3*

> The production is the easy part now. Getting paid for it is a different skill.

The gig → project → retainer progression, anchored to real documented ranges: $10-$55/ad on freelance marketplaces, $150-$300 per test batch, $1,500-$3,000+/mo for agency retainers. Covers building a portfolio from your first few pieces, writing outreach that leads with a finished sample (not your process), and pitching a retainer once you have 2-3 completed projects.

**Outputs:** [`outreach-template.md`](outputs/outreach-template.md), [`retainer-proposal-template.md`](outputs/retainer-proposal-template.md)

## 5. [Case Study Teardown](05-case-study-teardown.md)

*~30 min · Requires: Modules 1, 4*

> Learn to reverse-engineer a winning ad instead of guessing what worked.

A repeatable method for breaking a real, currently-running ad into the same five layers from Module 1 and asking why each choice was made — turning "that ad performed well" into reusable structural takeaways. Doubles as a sales tool: a free teardown of a prospect's category is a stronger opener than a generic pitch.

**Outputs:** [`teardown-worksheet.md`](outputs/teardown-worksheet.md)

---

All templates live in [`outputs/`](outputs/). For status across the other 14 tracks, see [ROADMAP.md](../../ROADMAP.md).

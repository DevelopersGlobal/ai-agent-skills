---
name: performance-optimization
description: Measure first, optimize second. Data-driven performance improvements with before/after benchmarks and production validation.
category: review
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Premature optimization is the root of all evil. But ignoring performance until it's a crisis is equally harmful. This skill enforces data-driven optimization: profile first, optimize the bottleneck, measure the improvement.

## When to Use

- When performance issues are reported in production
- Before optimizing any code (to ensure you're optimizing the right thing)
- When reviewing changes that touch performance-sensitive paths

## Process

### Step 1: Measure the Baseline

1. Reproduce the performance issue reliably.
2. Measure current performance: latency p50/p95/p99, throughput, memory, CPU.
3. Profile to find the actual bottleneck — not where you think it is.
4. Write the performance test you'll use to validate improvement.

**Verify:** You have concrete baseline numbers, not gut feelings.

### Step 2: Identify the Real Bottleneck

5. Use profiling tools: flame graphs, CPU profiles, memory profiles.
6. Find the top 3 hotspots by actual execution time (not lines of code).
7. The bottleneck is rarely where you expect it to be. Trust the data.

**Verify:** Bottleneck identified by profiling data, not assumption.

### Step 3: Optimize Only the Bottleneck

8. Fix only the profiled bottleneck — nothing else.
9. Common optimizations by type:
   - **CPU**: Algorithmic improvement (O(n²) → O(n log n)), caching, batching
   - **Memory**: Streaming instead of buffering, object pooling, lazy loading
   - **I/O**: Connection pooling, N+1 query elimination, caching, async/parallel calls
   - **AI**: Prompt caching, batch inference, smaller models for simpler tasks

**Verify:** Change targets the profiled bottleneck, not speculative improvements.

### Step 4: Measure the Improvement

10. Run the same performance test from Step 1.
11. Compare before vs. after metrics.
12. If improvement < 20%: the optimization may not be worth the complexity.

**Verify:** Improvement measured with the same test harness as baseline.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I know where the bottleneck is" | You're probably wrong. Profile first. |
| "This is clearly slow" | "Clearly slow" rarely matches profiler output. Measure. |
| "We'll optimize later" | If it's slow enough to mention, it's slow enough to measure now. |

## Verification

- [ ] Baseline metrics captured before any optimization
- [ ] Bottleneck identified by profiler (not assumption)
- [ ] Optimization targets only the profiled bottleneck
- [ ] Improvement measured with same test harness
- [ ] Before/after numbers documented

## References

- [references/performance-checklist.md](../../references/performance-checklist.md)
- [observability skill](../observability/SKILL.md)

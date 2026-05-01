# Performance Checklist

Supporting reference for [performance-optimization](../skills/performance-optimization/SKILL.md).

## Before Optimizing: Measure

- [ ] Baseline metrics captured (latency p50/p95/p99, throughput, CPU, memory)
- [ ] Profiler run to identify actual hotspot (not assumed hotspot)
- [ ] Performance test written that can be re-run after optimization

## Backend

- [ ] N+1 queries eliminated (use query batching or eager loading)
- [ ] Database indexes on all WHERE/JOIN columns
- [ ] Connection pooling configured (not new connection per request)
- [ ] Expensive operations cached with TTL appropriate to data freshness needs
- [ ] Pagination on all list endpoints (no unbounded queries)
- [ ] Async/parallel for independent I/O operations

## AI-Specific

- [ ] Prompt caching enabled (Anthropic, OpenAI support this)
- [ ] Batch inference used where sequential single calls are used
- [ ] Smallest model capable of the task (don't use GPT-4 for classification)
- [ ] Token count monitored and optimized (avoid redundant context)
- [ ] Streaming responses for long outputs (better perceived performance)

## Frontend

- [ ] Images optimized and served in WebP/AVIF
- [ ] JS bundle analyzed (`webpack-bundle-analyzer`)
- [ ] Unused dependencies removed
- [ ] Critical CSS inlined; non-critical CSS deferred
- [ ] LCP image preloaded (`<link rel="preload">`)

## Targets

| Metric | Target |
|--------|--------|
| API p99 latency | < 500ms |
| Page LCP | < 2.5s |
| Page CLS | < 0.1 |
| AI inference latency | < 2s (streaming) |
